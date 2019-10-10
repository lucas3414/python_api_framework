import pytest
import os
from Common.plugs.get_config import r_config
from Common.plugs.get_log import Log

BASE_DIR = os.path.dirname((os.path.dirname(__file__)))
conf_path = os.path.join(BASE_DIR, 'Common/conf/env_config.ini').replace('/', '\\')
log_path = r_config(conf_path, "log", "log_path")

logger = Log(log_path)

headers = {'User-Agent': 'Mozilla/5.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive',
           'Content-Length': '30'}


@pytest.fixture(scope='module')
def project_module_start():
    logger.info("==========开始 XX模块 执行测试===========")
    yield headers
    logger.info("==========结束 XX模块 测试===========")
