      # python_api_framework
      这是一个关于python的接口API自动化测试的项目，之前用的是unittest测试框架，现在改成pytest测试框架:Python+Excle+Pytest
      目前大体功能，按照版本测试需要支持，执行全部用例，按照用例等级按需执行， 设置用例标识按需执行,

      目前只是将 unittest 改成pytest了， 
        1、用例之间的依赖，数据依赖，过几天更新
        2、DB数据库校验等目前还没有做，已完成
        3、断言优化，过几天更新
        4、参数化时代码优化，日志优化，全部利用装饰器来做， 过几天更新
      .
      |-- Case
      |   |-- conftest.py
      |   |-- __init__.py
      |   |-- logincase
      |   |   |-- conftest.py
      |   |   |-- __init__.py
      |   |   `-- test_login.py
      |   `-- usercase
      |       |-- conftest.py
      |       |-- __init__.py
      |       `-- test_user.py
      |-- Common
      |   |-- conf
      |   |   |-- env_config.ini
      |   |   `-- __init__.py
      |   |-- __init__.py
      |   `-- plugs
      |       |-- get_config.py
      |       |-- get_db.py
      |       |-- get_excle.py
      |       |-- get_globals_data.py
      |       |-- get_log.py
      |       |-- http_requests.py
      |       `-- __init__.py
      |-- OutPut
      |   `-- log
      |       `-- 2019-10-11.log
      `-- TestData
          |-- case.xlsx
          `-- __init__.py


        2019-10-12 01:45:17,687 - root - INFO - ==========开始执行测试用例集===========
        2019-10-12 01:45:17,687 - root - INFO - 开始执行 ------- 正常登录测试 用例
        2019-10-12 01:45:17,687 - root - INFO - 准备发送 POST 请求
        2019-10-12 01:45:17,687 - root - INFO - 请求头: {'User-Agent': 'Mozilla/5.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Length': '30'}
        2019-10-12 01:45:17,688 - root - INFO - 接口地址: http://127.0.0.1:8888/api/private/v1/login
        2019-10-12 01:45:17,688 - root - INFO - 接口类型: POST
        2019-10-12 01:45:17,688 - root - INFO - 接口数据: {'username': 'admin', 'password': '123456'}
        2019-10-12 01:45:17,753 - root - INFO - 完成 POST 请求
        2019-10-12 01:45:17,754 - root - INFO - 响应结果json:{'data': {'id': 500, 'rid': 30, 'username': 'admin', 'mobile': '123456783231', 'email': 'adsfad@qq.com', 'token': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUwMCwicmlkIjozMCwiaWF0IjoxNTcwODE1OTE3LCJleHAiOjE1NzA5MDIzMTh9.GrwL3_RbcSRbUkLfIZ_Il64_MCmdBEqPesIVLuQDog8'}, 'meta': {'msg': '登录成功', 'status': 200}}
        2019-10-12 01:45:17,754 - root - INFO - 开始执行 ------- 添加用户， 正常用例 用例
        2019-10-12 01:45:17,755 - root - INFO -  请求发送前，开始进行 mysql 数据库检查
        2019-10-12 01:45:17,755 - root - INFO - sql：['SELECT * FROM sp_manager where mg_name = "wang"']
        2019-10-12 01:45:17,756 - root - INFO - sql返回结果 ((672, 'wang', '$2y$10$QW8G0omb4ee67UAMUSSlgukeC2/MK35qBU0HL5SOeTJiuV1JYVmle', 1570815605, -1, '13776765656', '123@qq.com', None),)
        2019-10-12 01:45:17,756 - root - INFO - 请求前数据库校验正常, sql : SELECT * FROM sp_manager where mg_name = "wang" 结果： (672, 'wang', '$2y$10$QW8G0omb4ee67UAMUSSlgukeC2/MK35qBU0HL5SOeTJiuV1JYVmle', 1570815605, -1, '13776765656', '123@qq.com', None)
        2019-10-12 01:45:17,775 - root - INFO - 准备发送 POST 请求
        2019-10-12 01:45:17,775 - root - INFO - 请求头: {'User-Agent': 'Mozilla/5.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Length': '30', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUwMCwicmlkIjozMCwiaWF0IjoxNTcwODE1OTE3LCJleHAiOjE1NzA5MDIzMTh9.GrwL3_RbcSRbUkLfIZ_Il64_MCmdBEqPesIVLuQDog8'}
        2019-10-12 01:45:17,776 - root - INFO - 接口地址: http://127.0.0.1:8888/api/private/v1/users
        2019-10-12 01:45:17,776 - root - INFO - 接口类型: POST
        2019-10-12 01:45:17,776 - root - INFO - 接口数据: {'username': 'wang', 'password': '123456', 'email': '123@qq.com', 'mobile': '13776765656'}
        2019-10-12 01:45:17,782 - root - INFO - 完成 POST 请求
        2019-10-12 01:45:17,782 - root - INFO - 响应结果json:{'data': None, 'meta': {'msg': '用户名已存在', 'status': 400}}
        2019-10-12 01:45:17,783 - root - INFO -  请求发送后，开始进行 mysql 数据库检查
        2019-10-12 01:45:17,783 - root - INFO - sql：['SELECT * FROM sp_manager where mg_name = "wang"']
        2019-10-12 01:45:17,783 - root - INFO - sql返回结果 ((672, 'wang', '$2y$10$QW8G0omb4ee67UAMUSSlgukeC2/MK35qBU0HL5SOeTJiuV1JYVmle', 1570815605, -1, '13776765656', '123@qq.com', None),)
        2019-10-12 01:45:17,784 - root - INFO - 请求后数据库校验正常, sql : SELECT * FROM sp_manager where mg_name = "wang" 结果： (672, 'wang', '$2y$10$QW8G0omb4ee67UAMUSSlgukeC2/MK35qBU0HL5SOeTJiuV1JYVmle', 1570815605, -1, '13776765656', '123@qq.com', None)
        2019-10-12 01:45:17,804 - root - INFO - 期望值：201
        2019-10-12 01:45:17,804 - root - INFO - 实际值：400
        2019-10-12 01:45:17,823 - root - ERROR - 断言失败：assert '201' == '400'
          - 201
          + 400
        2019-10-12 01:45:17,841 - root - INFO - 接口测试结果：Fail
        2019-10-12 01:45:17,860 - root - INFO - 开始执行 ------- 添加用户， 异常用例，用户名为空 用例
        2019-10-12 01:45:17,861 - root - INFO - 准备发送 POST 请求
        2019-10-12 01:45:17,861 - root - INFO - 请求头: {'User-Agent': 'Mozilla/5.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Length': '30', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUwMCwicmlkIjozMCwiaWF0IjoxNTcwODE1OTE3LCJleHAiOjE1NzA5MDIzMTh9.GrwL3_RbcSRbUkLfIZ_Il64_MCmdBEqPesIVLuQDog8'}
        2019-10-12 01:45:17,861 - root - INFO - 接口地址: http://127.0.0.1:8888/api/private/v1/users
        2019-10-12 01:45:17,861 - root - INFO - 接口类型: POST
        2019-10-12 01:45:17,862 - root - INFO - 接口数据: {'username': '', 'password': '123456'}
        2019-10-12 01:45:17,864 - root - INFO - 完成 POST 请求
        2019-10-12 01:45:17,864 - root - INFO - 响应结果json:{'data': None, 'meta': {'msg': '用户名不能为空', 'status': 400}}
        2019-10-12 01:45:17,864 - root - INFO - 期望值：400
        2019-10-12 01:45:17,865 - root - INFO - 实际值：400
        2019-10-12 01:45:17,885 - root - INFO - 接口测试结果：PASS
        2019-10-12 01:45:17,905 - root - INFO - 开始执行 ------- 添加用户， 异常用例，密码为空 用例
        2019-10-12 01:45:17,906 - root - INFO - 准备发送 POST 请求
        2019-10-12 01:45:17,906 - root - INFO - 请求头: {'User-Agent': 'Mozilla/5.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Length': '30', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUwMCwicmlkIjozMCwiaWF0IjoxNTcwODE1OTE3LCJleHAiOjE1NzA5MDIzMTh9.GrwL3_RbcSRbUkLfIZ_Il64_MCmdBEqPesIVLuQDog8'}
        2019-10-12 01:45:17,906 - root - INFO - 接口地址: http://127.0.0.1:8888/api/private/v1/users
        2019-10-12 01:45:17,906 - root - INFO - 接口类型: POST
        2019-10-12 01:45:17,907 - root - INFO - 接口数据: {'username': 'wang1', 'password': ''}
        2019-10-12 01:45:17,909 - root - INFO - 完成 POST 请求
        2019-10-12 01:45:17,909 - root - INFO - 响应结果json:{'data': None, 'meta': {'msg': '密码不能为空', 'status': 400}}
        2019-10-12 01:45:17,910 - root - INFO - 期望值：400
        2019-10-12 01:45:17,910 - root - INFO - 实际值：400
        2019-10-12 01:45:17,928 - root - INFO - 接口测试结果：PASS
        2019-10-12 01:45:17,948 - root - INFO - 开始执行 ------- 添加用户， 异常用例，邮箱为空 用例
        2019-10-12 01:45:17,948 - root - INFO - 准备发送 POST 请求
        2019-10-12 01:45:17,948 - root - INFO - 请求头: {'User-Agent': 'Mozilla/5.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Length': '30', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUwMCwicmlkIjozMCwiaWF0IjoxNTcwODE1OTE3LCJleHAiOjE1NzA5MDIzMTh9.GrwL3_RbcSRbUkLfIZ_Il64_MCmdBEqPesIVLuQDog8'}
        2019-10-12 01:45:17,949 - root - INFO - 接口地址: http://127.0.0.1:8888/api/private/v1/users
        2019-10-12 01:45:17,949 - root - INFO - 接口类型: POST
        2019-10-12 01:45:17,949 - root - INFO - 接口数据: {'username': 'wang2', 'password': '123456', 'email': '', 'mobile': '13776765656'}
        2019-10-12 01:45:17,957 - root - INFO - 完成 POST 请求
        2019-10-12 01:45:17,957 - root - INFO - 响应结果json:{'data': None, 'meta': {'msg': '用户名已存在', 'status': 400}}
        2019-10-12 01:45:17,958 - root - INFO - 期望值：201
        2019-10-12 01:45:17,958 - root - INFO - 实际值：400
        2019-10-12 01:45:17,977 - root - ERROR - 断言失败：assert '201' == '400'
          - 201
          + 400
        2019-10-12 01:45:17,996 - root - INFO - 接口测试结果：Fail
        2019-10-12 01:45:18,015 - root - INFO - 开始执行 ------- 添加用户， 异常用例，手机号空 用例
        2019-10-12 01:45:18,016 - root - INFO - 准备发送 POST 请求
        2019-10-12 01:45:18,016 - root - INFO - 请求头: {'User-Agent': 'Mozilla/5.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Length': '30', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUwMCwicmlkIjozMCwiaWF0IjoxNTcwODE1OTE3LCJleHAiOjE1NzA5MDIzMTh9.GrwL3_RbcSRbUkLfIZ_Il64_MCmdBEqPesIVLuQDog8'}
        2019-10-12 01:45:18,016 - root - INFO - 接口地址: http://127.0.0.1:8888/api/private/v1/users
        2019-10-12 01:45:18,016 - root - INFO - 接口类型: POST
        2019-10-12 01:45:18,017 - root - INFO - 接口数据: {'username': 'wang3', 'password': '123456', 'email': '123@qq.com', 'mobile': ''}
        2019-10-12 01:45:18,024 - root - INFO - 完成 POST 请求
        2019-10-12 01:45:18,024 - root - INFO - 响应结果json:{'data': None, 'meta': {'msg': '用户名已存在', 'status': 400}}
        2019-10-12 01:45:18,025 - root - INFO - 期望值：201
        2019-10-12 01:45:18,025 - root - INFO - 实际值：400
        2019-10-12 01:45:18,044 - root - ERROR - 断言失败：assert '201' == '400'
          - 201
          + 400
        2019-10-12 01:45:18,063 - root - INFO - 接口测试结果：Fail
        2019-10-12 01:45:18,084 - root - INFO - 开始执行 ------- 获取所有用户列表 用例
        2019-10-12 01:45:18,085 - root - INFO - 准备发送 GET 请求
        2019-10-12 01:45:18,085 - root - INFO - 请求头: {'User-Agent': 'Mozilla/5.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Length': '30', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUwMCwicmlkIjozMCwiaWF0IjoxNTcwODE1OTE3LCJleHAiOjE1NzA5MDIzMTh9.GrwL3_RbcSRbUkLfIZ_Il64_MCmdBEqPesIVLuQDog8'}
        2019-10-12 01:45:18,085 - root - INFO - 接口地址: http://127.0.0.1:8888/api/private/v1/users
        2019-10-12 01:45:18,085 - root - INFO - 接口类型: GET
        2019-10-12 01:45:18,085 - root - INFO - 接口数据: {'query': '', 'pagenum': 1, 'pagesize': 10}
        2019-10-12 01:45:18,093 - root - INFO - 完成 GET 请求
        2019-10-12 01:45:18,094 - root - INFO - 响应结果json:{'data': {'total': 9, 'pagenum': 1, 'users': [{'id': 500, 'role_name': '主管', 'username': 'admin', 'create_time': 1486720211, 'mobile': '123456783231', 'email': 'adsfad@qq.com', 'mg_state': True}, {'id': 502, 'role_name': '主管', 'username': 'linken', 'create_time': 1486720211, 'mobile': '120', 'email': '123@qq.com', 'mg_state': True}, {'id': 508, 'role_name': '测试角色', 'username': 'asdf1', 'create_time': 1511853015, 'mobile': '1231231', 'email': 'adfsa@qq.com', 'mg_state': True}, {'id': 574, 'role_name': '测试角色2', 'username': '12333', 'create_time': 1560799836, 'mobile': '13', 'email': '123', 'mg_state': False}, {'id': 597, 'role_name': '主管', 'username': 'luhy', 'create_time': 1565776785, 'mobile': '137722321878767611111233', 'email': '11111123@qq.com231', 'mg_state': True}, {'id': 623, 'role_name': '超级管理员', 'username': 'haha', 'create_time': 1568824982, 'mobile': '13776787676', 'email': '123@qq.com', 'mg_state': False}, {'id': 655, 'role_name': '超级管理员', 'username': 'wang2', 'create_time': 1570712763, 'mobile': '13776765656', 'email': '', 'mg_state': False}, {'id': 656, 'role_name': '超级管理员', 'username': 'wang3', 'create_time': 1570712763, 'mobile': '', 'email': '123@qq.com', 'mg_state': False}, {'id': 672, 'role_name': '超级管理员', 'username': 'wang', 'create_time': 1570815605, 'mobile': '13776765656', 'email': '123@qq.com', 'mg_state': False}]}, 'meta': {'msg': '获取管理员列表成功', 'status': 200}}
        2019-10-12 01:45:18,094 - root - INFO - 期望值：200
        2019-10-12 01:45:18,094 - root - INFO - 实际值：200
        2019-10-12 01:45:18,113 - root - INFO - 接口测试结果：PASS
        2019-10-12 01:45:18,133 - root - INFO - ==========结束执行测试用例集===========
        2019-10-12 01:45:18,133 - root - INFO - ==========结束 XX模块 测试===========
