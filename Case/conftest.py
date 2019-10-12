import pytest
import os
from Common.plugs.get_config import r_config
from Common.plugs.get_log import Log
from Common.plugs.get_db import MysqlConnect

BASE_DIR = os.path.dirname((os.path.dirname(__file__)))
conf_path = os.path.join(BASE_DIR, 'Common/conf/env_config.ini').replace('/', '\\')
log_path = r_config(conf_path, "log", "log_path")
database_info = r_config(conf_path, 'DB', 'database')

logger = Log(log_path)

mc = MysqlConnect(eval(database_info)['host'],
                  eval(database_info)['port'],
                  eval(database_info)['user'],
                  eval(database_info)['password'],
                  eval(database_info)['db'])

headers = {'User-Agent': 'Mozilla/5.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive',
           'Content-Length': '30'}


@pytest.fixture(scope='session')
def project_module_start():
    logger.info("==========开始 XX模块 执行测试===========")
    yield (headers, mc)
    mc.close_db()
    logger.info("==========结束 XX模块 测试===========")


def pytest_configure(config):
    # 标签名集合
    marker_list = ['p1', 'p2', 'p3']
    for markers in marker_list:
        config.addinivalue_line('markers', markers)
