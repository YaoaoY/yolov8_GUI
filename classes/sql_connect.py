# -*- coding: utf-8 -*-
# @Author : pan
# @Description : 本模块为数据库操作模块，包括连接参数及增删查改功能（还未对接）
# @Date : 2023年7月27日10:28:50
import string
from pprint import pprint
import pymysql

# DB_CONFIG = {
# 	"host": "127.0.0.1",
# 	"port": 3306,
# 	"user": "root",
# 	"passwd": "123456",
# 	"db": "test",
# 	"charset": "utf8"
# }

class SQLManager(object):

	# 初始化实例方法
	def __init__(self,
				 host:str="127.0.0.1", port:int=3306, user:str="root",
				 passwd:str="123456", db:str="yolo", charset:str="utf8"):
		self.conn = None
		self.cursor = None

		# 数据库配置
		self.host = host
		self.port = port
		self.user = user
		self.passwd = passwd
		self.db = db
		self.charset = charset

		# 连接数据库
		self.connect()

	# 连接数据库
	def connect(self):
		self.conn = pymysql.connect(
			host=self.host,
			port=self.port,
			user=self.user,
			passwd=self.passwd,
			db=self.db,
			charset=self.charset
		)
		self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

	# 查询多条数据
	def get_list(self, sql, args=None)->list:
		self.cursor.execute(sql, args)
		result = self.cursor.fetchall()
		return result

	# 查询单条数据
	def get_one(self, sql, args=None) ->dict:
		self.cursor.execute(sql, args)
		result = self.cursor.fetchone()
		return result

	# 执行单条SQL语句
	def modify(self, sql, args=None):
		self.cursor.execute(sql, args)
		self.conn.commit()

	# 我如果要批量执行多个创建操作，虽然只建立了一次数据库连接但是还是会多次提交，可不可以改成一次连接，一次提交呢？
	# 可以，只需要用上pymysql的executemany()方法就可以了。

	# 执行多条SQL语句
	def multi_modify(self, sql, args=None):
		self.cursor.executemany(sql, args)
		self.conn.commit()

	# 创建单条记录的语句
	def create(self, sql, args=None):
		self.cursor.execute(sql, args)
		self.conn.commit()
		last_id = self.cursor.lastrowid
		return last_id

	# 关闭数据库cursor和连接
	def close(self):
		self.cursor.close()
		self.conn.close()

	# 最后，我们每次操作完数据库之后都要手动关闭，可不可以写成自动关闭的呢？
	# 联想到我们之前学过的文件操作，使用with语句可以实现缩进结束自动关闭文件句柄的例子。
	# 我们来把我们的数据库连接类SQLManager类再优化下，使其支持with语句操作。
	# 进入with语句自动执行
	def __enter__(self):
		return self

	# 退出with语句块自动执行
	def __exit__(self, exc_type, exc_val, exc_tb):
		self.close()

if __name__ == "__main__":
	# 方法1：
	#如果你的应用程序需要频繁地进行数据库操作且要求高效率，可以选择使用全局对象的方式
	db = SQLManager()
	show_data_db1 = db.get_list('select * from user ')
	pprint(show_data_db1)
	show_data_db1 = db.get_list('select * from auto ')
	pprint(show_data_db1)


	# 方法2：
	# 如果你的应用程序只偶尔需要进行数据库操作或者需要更加严谨的资源管理，可以选择使用 with 语句的方式。
	with SQLManager() as sql_manager:
		# 执行数据库操作
		result = sql_manager.get_list("SELECT * FROM user")
		pprint(result)
		# 其他数据库操作...
	# 在with语句块结束时，会自动调用__exit__方法关闭数据库连接