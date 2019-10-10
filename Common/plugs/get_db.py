import pymysql


class MysqlConnect(object):
    # 魔术方法, 初始化, 构造函数
    def __init__(self, host, user, password, database):
        self.db = pymysql.connect(host=host, user=user, password=password, port=3306, database=database, charset='utf8')
        self.cursor = self.db.cursor()

    # 将要插入的数据写成元组传入
    def exec_data(self, sql, data=None):
        # 执行SQL语句
        self.cursor.execute(sql, data)
        # 提交到数据库执行
        self.db.commit()

    # sql拼接时使用repr()，将字符串原样输出
    def exec(self, sql):
        self.cursor.execute(sql)
        # 提交到数据库执行
        self.db.commit()

    def select(self, sql):
        self.cursor.execute(sql)
        # 获取所有记录列表
        return self.cursor.fetchall()

    # 魔术方法, 析构化 ,析构函数
    def __del__(self):
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    mc = MysqlConnect('127.0.0.1', 'root', '123456', 'itcast')
    # mc.exec('insert into test(id, text) values(%s, %s)' % (1, repr('哈送到附近')))
    # mc.exec_data('insert into test(id, text) values(%s, %s)' % (1, repr('哈送到附近')))
    # # mc.exec_data('insert into test(id, text) values(%s, %s)',(13, '哈送到附近'))
    ret = mc.select('select * from sp_manager where mg_name like "l%" ')
    # print(ret[0][0])
    print(ret)
