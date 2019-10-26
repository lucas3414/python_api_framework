import pymysql
import os
import sys
from Common.plugs.get_config import r_config
from Common.plugs.get_log import Log

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

if sys.platform == "win32":
    ENV_CONF_DIR = os.path.join(BASE_DIR, 'Common/conf/env_config.ini').replace('/', '\\')
else:
    ENV_CONF_DIR = os.path.join(BASE_DIR, 'Common/conf/env_config.ini')

log_path = r_config(ENV_CONF_DIR, "log", "log_path")
database_info = r_config(ENV_CONF_DIR, 'DB', 'database')

logger = Log(log_path)


class MysqlConnect:
    def __init__(self, host, port, user, password, database):
        try:
            logger.info("准备连接数据库")
            logger.info("连接信息：host:{0}, port:{1}, user:{2}, password:{3}, database:{4}".format(host, port, user, password,
                                                                                           database))
            self.db = pymysql.connect(host=host, user=user, password=password, port=port, database=database,
                                      charset='utf8')
            logger.info("连接数据库成功")
            self.cursor = self.db.cursor()
        except Exception as e:
            logger.error("连接数据库失败：{0}".format(str(e)))

    # 将要插入的数据写成元组传入
    def exec_data(self, sql, data=None):
        self.cursor.execute(sql, data)
        self.db.commit()
        self.cursor.close()
        self.db.close()

    # sql拼接时使用repr()，将字符串原样输出
    def exec(self, sql):
        self.cursor.execute(sql)
        self.db.commit()

    def select(self, sql):
        try:
            logger.info("开始查询数据")
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            logger.info("查询成功")
            return result
        except Exception as e:
            logger.error("查询数据失败：{0}".format(str(e)))


    # def __del__(self):
    #     self.cursor.close()
    #     self.db.close()

    def close_db(self):
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    # mc = MysqlConnect('127.0.0.1',3306 'root', '123456', 'itcast')
    # mc.exec('insert into test(id, text) values(%s, %s)' % (1, repr('哈送到附近')))
    # mc.exec_data('insert into test(id, text) values(%s, %s)' % (1, repr('哈送到附近')))
    # # mc.exec_data('insert into test(id, text) values(%s, %s)',(13, '哈送到附近'))
    # ret = mc.select('select * from sp_manager where mg_name like "l%" ')
    # print(ret[0][0])
    # print(ret)

    mc = MysqlConnect(eval(database_info)['host'],
                      eval(database_info)['port'],
                      eval(database_info)['user'],
                      eval(database_info)['password'],
                      eval(database_info)['db'])
    ret = mc.select('select * from sp_manager where mg_name = "admin" ')
    print(ret)
    print(type(ret))
    pass
