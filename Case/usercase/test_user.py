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

DE = DoExcle(test_case_path, 'user')
caseList = split_list(DE.read_data())
logger = Log(log_path)


@pytest.mark.usefixtures('start_module')
class TestUser:

    @pytest.mark.p1
    @pytest.mark.parametrize('item', caseList[0])
    def test_P1_AddUser(self, start_module, item):
        logger.info("开始执行 ------- {0} 用例".format(item['description']))
        ret = BaseRequest(url=item['url'], headers=start_module, method=item['method'],
                          data=eval(item['parm'])).get_json()

        try:
            logger.info("期望值：{0}".format(str(item['excepted'])))
            logger.info("实际值：{0}".format(str(ret['meta']['status'])))
            assert str(item['excepted']) == str(ret['meta']['status'])
            TestResult = 'PASS'
        except AssertionError as e:
            TestResult = 'Fail'
            DE.write_data(item['sheetname'], item['id'] + 1, 11, str(e))
            logger.error("断言失败：{0}".format(str(e)))
            raise e
        finally:
            logger.info("接口响应值：{0}".format(str(ret)))
            DE.write_data(item['sheetname'], item['id'] + 1, 9, str(ret))
            logger.info("接口测试结果：{0}".format(TestResult))
            DE.write_data(item['sheetname'], item['id'] + 1, 10, TestResult)

    @pytest.mark.p2
    @pytest.mark.parametrize('item', caseList[1])
    def test_P2_AddUser(self, start_module, item):
        logger.info("开始执行 ------- {0} 用例".format(item['description']))
        ret = BaseRequest(url=item['url'], headers=start_module, method=item['method'],
                          data=eval(item['parm'])).get_json()

        try:
            logger.info("期望值：{0}".format(str(item['excepted'])))
            logger.info("实际值：{0}".format(str(ret['meta']['status'])))
            assert str(item['excepted']) == str(ret['meta']['status'])
            TestResult = 'PASS'
        except AssertionError as e:
            TestResult = 'Fail'
            DE.write_data(item['sheetname'], item['id'] + 1, 11, str(e))
            logger.error("断言失败：{0}".format(str(e)))
            raise e
        finally:
            logger.info("接口响应值：{0}".format(str(ret)))
            DE.write_data(item['sheetname'], item['id'] + 1, 9, str(ret))
            logger.info("接口测试结果：{0}".format(TestResult))
            DE.write_data(item['sheetname'], item['id'] + 1, 10, TestResult)

    @pytest.mark.p3
    @pytest.mark.parametrize('item', caseList[2])
    def test_P3_AddUser(self, start_module, item):
        logger.info("开始执行 ------- {0} 用例".format(item['description']))
        ret = BaseRequest(url=item['url'], headers=start_module, method=item['method'],
                          data=eval(item['parm'])).get_json()

        try:
            logger.info("期望值：{0}".format(str(item['excepted'])))
            logger.info("实际值：{0}".format(str(ret['meta']['status'])))
            assert str(item['excepted']) == str(ret['meta']['status'])
            TestResult = 'PASS'
        except AssertionError as e:
            TestResult = 'Fail'
            DE.write_data(item['sheetname'], item['id'] + 1, 11, str(e))
            logger.error("断言失败：{0}".format(str(e)))
            raise e
        finally:
            logger.info("接口响应值：{0}".format(str(ret)))
            DE.write_data(item['sheetname'], item['id'] + 1, 9, str(ret))
            logger.info("接口测试结果：{0}".format(TestResult))
            DE.write_data(item['sheetname'], item['id'] + 1, 10, TestResult)
