import requests
import os
from Common.plugs.get_config import r_config
from Common.plugs.get_log import Log

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
conf_path = os.path.join(BASE_DIR, 'Common/conf/env_config.ini').replace('/', '\\')
log_path = r_config(conf_path, "log", "log_path")

logger = Log(log_path)


class BaseRequest:

    def __init__(self, method, url, data=None, cookies=None, headers=None):
        logger.info("准备发送 {0} 请求".format(method.upper()))
        logger.info("请求头: {0}".format(headers))
        logger.info("接口地址: {0}".format(url))
        logger.info("接口类型: {0}".format(method.upper()))
        logger.info("接口数据: {0}".format(data))
        try:
            if method.upper() == 'GET':
                self.response = requests.get(url=url, params=data, cookies=cookies, headers=headers)
                logger.info("完成 GET 请求")
            elif method.upper() == 'POST':
                self.response = requests.post(url=url, data=data, cookies=cookies, headers=headers)
                logger.info("完成 POST 请求")
            elif method.upper() == 'DELETE':
                self.response = requests.delete(url=url, data=data, cookies=cookies, headers=headers)
                logger.info("完成 DELETE 请求")
        except Exception as e:
            logger.error("请求报错：{0}".format(str(e)))
            raise e

    def get_status_code(self):
        logger.info("响应结果状态码:{0}".format(self.response.json()))
        return self.response.status_code

    def get_text(self):
        logger.info("响应结text:{0}".format(self.response.json()))
        return self.response.text

    def get_json(self):
        logger.info("响应结果json:{0}".format(self.response.json()))
        return self.response.json()

    def get_cookies(self):
        logger.info("响应结果cookie:{0}".format(self.response.json()))
        return self.response.cookies


if __name__ == '__main__':
    cookies = None
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'http://127.0.0.1:8888/api/private/v1/login'
    url1 = 'http://127.0.0.1:8888/api/private/v1/users'
    data = {'username': 'admin', 'password': '123456'}
    data1 = {'query': '', 'pagenum': 1, 'pagesize': 10}

    ret = BaseRequest('post', url=url, data=data, cookies=cookies, headers=headers)
    # print(ret.get_json())

    headers['Authorization'] = ret.get_json()['data']['token']
    ret1 = BaseRequest('get', url=url1, data=data1, cookies=cookies, headers=headers)
    print(ret1.get_json())
