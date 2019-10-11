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


    2019-10-11 10:15:07,693 - root - INFO - ==========开始 XX模块 执行测试===========
    2019-10-11 10:15:07,693 - root - INFO - ==========开始执行测试用例集===========
    2019-10-11 10:15:07,693 - root - INFO - 开始执行 ------- 正常登录测试 用例
    2019-10-11 10:15:07,693 - root - INFO - 准备发送 POST 请求
    2019-10-11 10:15:07,693 - root - INFO - 请求头: {'User-Agent': 'Mozilla/5.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Length': '30'}
    2019-10-11 10:15:07,693 - root - INFO - 接口地址: http://127.0.0.1:8888/api/private/v1/login
    2019-10-11 10:15:07,693 - root - INFO - 接口类型: POST
    2019-10-11 10:15:07,693 - root - INFO - 接口数据: {'username': 'admin', 'password': '123456'}
    2019-10-11 10:15:07,771 - root - INFO - 完成 POST 请求
    2019-10-11 10:15:07,771 - root - INFO - 响应结果json:{'data': {'id': 500, 'rid': 30, 'username': 'admin', 'mobile': '123456783231', 'email': 'adsfad@qq.com', 'token': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUwMCwicmlkIjozMCwiaWF0IjoxNTcwNzYwMTA3LCJleHAiOjE1NzA4NDY1MDh9.Mds-GPCrI8KRSb3quhlH1wyefZ7s8nvW5FoK3zqUZNk'}, 'meta': {'msg': '登录成功', 'status': 200}}
    2019-10-11 10:15:07,771 - root - INFO - 开始执行 ------- 添加用户， 正常用例 用例
    2019-10-11 10:15:07,771 - root - INFO - 准备发送 POST 请求
    2019-10-11 10:15:07,771 - root - INFO - 请求头: {'User-Agent': 'Mozilla/5.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Length': '30', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUwMCwicmlkIjozMCwiaWF0IjoxNTcwNzYwMTA3LCJleHAiOjE1NzA4NDY1MDh9.Mds-GPCrI8KRSb3quhlH1wyefZ7s8nvW5FoK3zqUZNk'}
    2019-10-11 10:15:07,771 - root - INFO - 接口地址: http://127.0.0.1:8888/api/private/v1/users
    2019-10-11 10:15:07,771 - root - INFO - 接口类型: POST
    2019-10-11 10:15:07,771 - root - INFO - 接口数据: {'username': 'wang', 'password': '123456', 'email': '123@qq.com', 'mobile': '13776765656'}
    2019-10-11 10:15:07,771 - root - INFO - 完成 POST 请求
    2019-10-11 10:15:07,771 - root - INFO - 响应结果json:{'data': None, 'meta': {'msg': '用户名已存在', 'status': 400}}
    2019-10-11 10:15:07,771 - root - INFO - 期望值：201
    2019-10-11 10:15:07,771 - root - INFO - 实际值：400
    2019-10-11 10:15:07,802 - root - ERROR - 断言失败：assert '201' == '400'
      - 201
      + 400
    2019-10-11 10:15:07,818 - root - INFO - 接口测试结果：Fail
    2019-10-11 10:15:07,881 - root - INFO - 开始执行 ------- 添加用户， 异常用例，用户名为空 用例
    2019-10-11 10:15:07,881 - root - INFO - 准备发送 POST 请求
    2019-10-11 10:15:07,881 - root - INFO - 请求头: {'User-Agent': 'Mozilla/5.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Length': '30', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUwMCwicmlkIjozMCwiaWF0IjoxNTcwNzYwMTA3LCJleHAiOjE1NzA4NDY1MDh9.Mds-GPCrI8KRSb3quhlH1wyefZ7s8nvW5FoK3zqUZNk'}
    2019-10-11 10:15:07,881 - root - INFO - 接口地址: http://127.0.0.1:8888/api/private/v1/users
    2019-10-11 10:15:07,881 - root - INFO - 接口类型: POST
    2019-10-11 10:15:07,881 - root - INFO - 接口数据: {'username': '', 'password': '123456'}
    2019-10-11 10:15:07,881 - root - INFO - 完成 POST 请求
    2019-10-11 10:15:07,881 - root - INFO - 响应结果json:{'data': None, 'meta': {'msg': '用户名不能为空', 'status': 400}}
    2019-10-11 10:15:07,881 - root - INFO - 期望值：400
    2019-10-11 10:15:07,881 - root - INFO - 实际值：400
    2019-10-11 10:15:07,896 - root - INFO - 接口测试结果：PASS
