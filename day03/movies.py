# encoding=utf-8
import hashlib
import uuid

import werkzeug
from flask import Flask, request, make_response, jsonify, flash, Blueprint, render_template

app = Flask(__name__)

# 图书列表
MOVIES = (
    {"id": 1, "name": "肖申克的救赎"},
    {"id": 2, "name": "霸王别姬"},
    {"id": 3, "name": "这个杀手不太冷"},
    {"id": 4, "name": "阿甘正传"},
    {"id": 5, "name": "美丽人生"},
    {"id": 6, "name": "泰坦尼克号"},
    {"id": 7, "name": "千与千寻"},
    {"id": 8, "name": "辛德勒的名单"},
    {"id": 9, "name": "海上钢琴师"},
    {"id": 10, "name": "楚门的世界"}
)


def md5(_str):
    """
    md5 加密
    :param _str:
    :return:
    """
    return hashlib.md5(bytes(_str, encoding='utf-8')).hexdigest()


class BusinessException(werkzeug.exceptions.HTTPException):
    """
    业务异常定义类
    """

    def __init__(self, code: int, message: str):
        # Exception.__init__()
        self.code = code
        self.message = message
        self.response = jsonify({'code': code, 'message': message})


# 用户表


user_table = {
    "admin": md5("admin")
}
# 用户cookie 表
user_cookie_table = {}

# 用户电影表
user_movie_table = {}


@app.route('/user/register', methods=['POST'])
def user_register():
    """
    用户注册
    :return:
    """
    username = request.form.get('username')
    password = request.form.get('password')
    if not username:
        raise BusinessException(1, "用户名不能为空")
    if not password:
        raise BusinessException(2, "密码不能为空")
    if user_table.get(username):
        raise BusinessException(3, "用户已经注册")

    user_table[username] = md5(password)
    return success(message=f"用户:{username} 注册成功")


def success(content=None, message=None):
    """生成成功的响应"""
    return jsonify({'code': 200, 'content': content, 'message': message})


@app.route('/user/login', methods=['POST'])
def user_login():
    """
    用户登录
    :return:
    """
    username = request.form.get('username')
    password = request.form.get('password')
    if not username:
        raise BusinessException(1, "用户名不能为空")
    if not password:
        raise BusinessException(1, "密码不能为空")
    if user_table.get(username) is None:
        raise BusinessException(1, "用户名不存在，请注册")
    if not (user_table.get(username) == md5(password)):
        raise BusinessException(1, "密码不正确")

    # 生成一个uuid 随机字符串
    uid = str(uuid.uuid1())
    # 保存到cookies表中
    user_cookie_table[uid] = username
    # 给客户端返回响应
    resp = make_response(success(message="登录成功"))
    # 设置cookie
    resp.set_cookie('uid', uid)
    return resp


def _check_login():
    """
    检查登录
    :return:
    """
    uid = request.cookies.get('uid')
    if not uid:
        raise BusinessException(1, "没有登录")
    username = user_cookie_table.get(uid)
    if not username:
        raise BusinessException(1, "登录失效,请重新登录")
    return username


@app.route('/movie/list', methods=['GET'])
def list_movies():
    """
    获取全部的电影列表
    :return:
    """
    return success(content=MOVIES)

    # return json.dumps({"movies": MOVIES}, ensure_ascii=False)   # 解析工具认为这是字符串，无法识别json


@app.route('/user/movies', methods=['GET'])
def list_user_movies():
    """
    获取用户购买的全部电影
    :return:
    """
    username = _check_login()
    user_movie_table.setdefault(username, [])
    movies = user_movie_table.get(username)
    return success(content=movies)


@app.route("/movie/buy", methods=['post'])
def movie_buy():
    """
    购买电影
    :return:
    """
    username = _check_login()
    id = request.form.get('id')
    if not id:
        raise BusinessException(-1, "id 不能为空")
    for item in MOVIES:
        if id == str(item.get('id')):
            print(f'找到了要买的电影{item}')
            user_movie_table.setdefault(username, [])
            user_movie_table.get(username).append(item)
            return success(message="购买成功")

    print(f'找不要您要购买的电影，请检查id是否正确，id={id}')
    raise BusinessException(-1, "购买失败，找不要您要购买的电影，请检查id是否正确")


if __name__ == '__main__':
    # 启动flask web 服务

    app.run()
