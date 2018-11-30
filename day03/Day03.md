# 写个假服务器程序，帮助大家了解一下，后台服务的基本原理
功能
* 用户注册
* 用户登录
* 查看电影列表
* 购买电影
* 查看自己已购的电影列表

使用的框架: flask
参考文档:
 * https://github.com/pallets/flask
 * http://flask.pocoo.org/docs/1.0/quickstart
 * http://docs.jinkan.org/docs/flask/quickstart.html#redirects-and-errors
 
 
知识点:
* 网络请求的流程
  客户端->DNS解析->网卡->中间的各种路由-> 服务器网卡->服务器程序
* http:
    * get
    * post
    * head
    * session
    * contentType



功能实现的方式，仅供参考，学习，实验，真实的后端开发功能比这个复杂很多倍，但是基本原理是这样。


其他:
 * 关于一个方法的返回结果是应该抛异常，还是应该返回一个错误的值。https://stackoverflow.com/questions/77127/when-to-throw-an-exception