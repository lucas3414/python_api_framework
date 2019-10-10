import pytest
import os
from Common.plugs.get_config import r_config
from Common.plugs.http_requests import BaseRequest
from Common.plugs.get_excle import DoExcle, split_list
from Common.plugs.get_log import Log

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
conf_path = os.path.join(BASE_DIR, 'Common/conf/env_config.ini').replace('/', '\\')
log_path = r_config(conf_path, "log", "log_path")
test_case_path = r_config(conf_path, "test_case", "test_case_path")

DE = DoExcle(test_case_path, 'login')
caseList = split_list(DE.read_data())[0][0]

logger = Log(log_path)


@pytest.fixture(scope='class')
def start_module(project_module_start):
    logger.info("==========开始执行测试用例集===========")
    headers = project_module_start
    logger.info("开始执行 ------- {0} 用例".format(caseList['description']))
    ret = BaseRequest(url=caseList['url'], headers=project_module_start, method=caseList['method'],
                      data=eval(caseList['parm'])).get_json()
    # 将 token 加入到请求投中
    if ret['data'] != None and 'token' in ret['data']:
        headers['Authorization'] = ret['data']['token']
    yield headers
    logger.info("==========结束执行测试用例集===========")
