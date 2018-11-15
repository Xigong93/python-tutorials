# encoding=utf-8
import openpyxl
import requests

# 网络请求接口
# get请求
response = requests.get('http://api.douban.com/v2/movie/top250')
# 响应转json,这个库自动解决编码的问题
result = response.json()
print(f'结果:{result}')

# 创建一个excel 表格
workbook = openpyxl.Workbook()
# 创建一个sheet 页
# 添加表头
sheet = workbook.create_sheet('豆瓣电影TOP250')
sheet.append(["电影", "原名", "年份", "主演", "题材", "链接"])
# 获取电影列表
subjects = result["subjects"]
for subject in subjects:
    # 遍历电影列表，添加行
    sheet.append([
        subject["title"],
        subject["original_title"],
        subject["year"],
        " ".join([actor["name"] for actor in subject["casts"]]),
        " ".join(subject["genres"]),
        subject['alt']
    ])
# 把内存中的表，存到硬盘上
workbook.save('douban-top250.xlsx')
