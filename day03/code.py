# encoding=utf-8
import json

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


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


@app.route('/user/register', methods=['POST'])
def user_register():
    """
    用户注册
    :return:
    """
    username = request.form['username']
    password = request.form['password']
    return username + "," + password


@app.route('/user/login', methods=['POST'])
def user_login():
    """
    用户登录
    :return:
    """
    username = request.form['username']
    password = request.form['password']
    return username + "," + password


def check_login():
    username = request.cookies.get('username')
    if username is None:
        raise Exception("没有登录")


@app.route('/movie/list', methods=['GET'])
def list_movies():
    """
    获取全部的电影列表
    :return:
    """
    return json.dumps({"movies": MOVIES}, ensure_ascii=False)


if __name__ == '__main__':
    # 启动flask web 服务
    app.run()
