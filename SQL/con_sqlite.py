import sqlite3

# 连接数据库
conn = sqlite3.connect('scrapy.db')

# 创建corosr对象，用来执行SQL语句
cur = conn.cursor()

# 创建数据表
cur.execute('CREATE TABLE person(name VARCHAR(32), age INT, sex char(1))')

# 插入一条数据
cur.execute('INSERT INTO person VALUES  (?, ?, ?)', ('陈浩', 25, 'M'))

# 保存变更，提交保存
conn.commit()

# 关闭连接
conn.close()