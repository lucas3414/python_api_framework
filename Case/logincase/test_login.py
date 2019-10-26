import pytest
import os
import sys
from Common.plugs.get_config import r_config
from Common.plugs.http_requests import BaseRequest
from Common.plugs.get_excle import DoExcle, split_list
from Common.plugs.get_log import Log

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

if sys.platform == "win32":
    conf_path = os.path.join(BASE_DIR, 'Common/conf/env_config.ini').replace('/', '\\')
else:
    conf_path = os.path.join(BASE_DIR, 'Common/conf/env_config.ini')

log_path = r_config(conf_path, "log", "log_path")
logger = Log(log_path)
test_case_path = r_config(conf_path, "test_case", "test_case_path")

DE = DoExcle(test_case_path, 'login')
caseList = split_list(DE.read_data())


@pytest.mark.usefixtures('start_module')
class TestLogin:

    @pytest.mark.p1
    @pytest.mark.parametrize('item', caseList[0])
    def test_P1_login(self, start_module, item):
        logger.info("开始执行 ------- {0}".format(item['description']))

        ret = BaseRequest(url=item['url'], headers=start_module[0], method=item['method'],
                          data=eval(item['parm'])).get_json()

        try:
            logger.info("期望值：{0}".format(str(item['excepted'])))
            logger.info("实际值：{0}".format(str(ret['meta']['status'])))
            assert str(item['excepted']) == str(ret['meta']['status'])
            TestResult = 'PASS'
            DE.write_data(item['sheetname'], item['id'] + 1, 11, str(ret))
            logger.info("接口测试结果：{0}".format(TestResult))
            DE.write_data(item['sheetname'], item['id'] + 1, 12, TestResult)
        except AssertionError as e:
            TestResult = 'Fail'
            DE.write_data(item['sheetname'], item['id'] + 1, 13, str(e))
            logger.error("断言失败：{0}".format(str(e)))
            DE.write_data(item['sheetname'], item['id'] + 1, 11, str(ret))
            logger.info("接口测试结果：{0}".format(TestResult))
            DE.write_data(item['sheetname'], item['id'] + 1, 12, TestResult)
            raise

    @pytest.mark.p2
    @pytest.mark.parametrize('item', caseList[1])
    def test_P2_login(self, start_module, item):
        logger.info("开始执行 ------- {0}".format(item['description']))
        ret = BaseRequest(url=item['url'], headers=start_module[0], method=item['method'],
                          data=eval(item['parm'])).get_json()

        try:
            logger.info("期望值：{0}".format(str(item['excepted'])))
            logger.info("实际值：{0}".format(str(ret['meta']['status'])))
            assert str(item['excepted']) == str(ret['meta']['status'])
            TestResult = 'PASS'
            DE.write_data(item['sheetname'], item['id'] + 1, 11, str(ret))
            logger.info("接口测试结果：{0}".format(TestResult))
            DE.write_data(item['sheetname'], item['id'] + 1, 12, TestResult)
        except AssertionError as e:
            TestResult = 'Fail'
            DE.write_data(item['sheetname'], item['id'] + 1, 13, str(e))
            logger.error("断言失败：{0}".format(str(e)))
            DE.write_data(item['sheetname'], item['id'] + 1, 11, str(ret))
            logger.info("接口测试结果：{0}".format(TestResult))
            DE.write_data(item['sheetname'], item['id'] + 1, 12, TestResult)
            raise e

    @pytest.mark.p3
    @pytest.mark.parametrize('item', caseList[2])
    def test_P3_login(self, start_module, item):
        logger.info("开始执行 ------- {0}".format(item['description']))
        ret = BaseRequest(url=item['url'], headers=start_module[0], method=item['method'],
                          data=eval(item['parm'])).get_json()

        try:
            logger.info("期望值：{0}".format(str(item['excepted'])))
            logger.info("实际值：{0}".format(str(ret['meta']['status'])))
            assert str(item['excepted']) == str(ret['meta']['status'])
            TestResult = 'PASS'
            DE.write_data(item['sheetname'], item['id'] + 1, 11, str(ret))
            logger.info("接口测试结果：{0}".format(TestResult))
            DE.write_data(item['sheetname'], item['id'] + 1, 12, TestResult)
        except AssertionError as e:
            TestResult = 'Fail'
            DE.write_data(item['sheetname'], item['id'] + 1, 13, str(e))
            logger.error("断言失败：{0}".format(str(e)))
            DE.write_data(item['sheetname'], item['id'] + 1, 11, str(ret))
            logger.info("接口测试结果：{0}".format(TestResult))
            DE.write_data(item['sheetname'], item['id'] + 1, 12, TestResult)
            raise
