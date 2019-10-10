import pytest
import os
from Common.plugs.get_config import r_config
from Common.plugs.get_log import Log

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
conf_path = os.path.join(BASE_DIR, 'Common/conf/env_config.ini').replace('/', '\\')
log_path = r_config(conf_path, "log", "log_path")

logger = Log(log_path)


@pytest.fixture(scope='class')
def start_module(project_module_start):
    logger.info("==========开始执行测试用例集===========")
    headers = project_module_start
    yield headers
    logger.info("==========结束执行测试用例集===========")
