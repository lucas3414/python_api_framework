import requests


class BaseRequest:

    def __init__(self, method, url, data=None, cookies=None, headers=None):
        try:
            if method.upper() == 'GET':
                self.response = requests.get(url=url, params=data, cookies=cookies, headers=headers)
            elif method.upper() == 'POST':
                self.response = requests.post(url=url, data=data, cookies=cookies, headers=headers)
            elif method.upper() == 'DELETE':
                self.response = requests.delete(url=url, data=data, cookies=cookies, headers=headers)
        except Exception as e:
            raise e

    def get_status_code(self):
        return self.response.status_code

    def get_text(self):
        return self.response.text

    def get_json(self):
        return self.response.json()

    def get_cookies(self):
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
