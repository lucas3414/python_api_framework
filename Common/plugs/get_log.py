import os, time, logging, sys
from Common.plugs.get_config import r_config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
if sys.platform == "win32":
    ENV_CONF_DIR = os.path.join(BASE_DIR, 'Common/conf/env_config.ini').replace('/', '\\')
else:
    ENV_CONF_DIR = os.path.join(BASE_DIR, 'Common/conf/env_config.ini')
log_path = r_config(ENV_CONF_DIR, "log", "log_path")


class Log:

    def __init__(self, log_path):
        self.logName = os.path.join(log_path, '{0}.log'.format(time.strftime('%Y-%m-%d')))

    def console_log(self, level, message):
        # 创建一个logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于 debug 写入日志文件
        debug_file = logging.FileHandler(self.logName, 'a+', encoding='utf-8')
        debug_file.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        debug_file.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        logger.addHandler(debug_file)
        logger.addHandler(ch)

        # 记录一条日志
        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)

        logger.removeHandler(ch)
        logger.removeHandler(debug_file)
        debug_file.close()

    def debug(self, message):
        self.console_log('debug', message)

    def info(self, message):
        self.console_log('info', message)

    def warning(self, message):
        self.console_log('warning', message)

    def error(self, message):
        self.console_log('error', message)


if __name__ == '__main__':
    Log(log_path).info("adasd")
    Log(log_path).error("dsadasddasd")
