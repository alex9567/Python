import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
#返回查询结果
print(cursor.execute('select * from user where id=?', ('1',)))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()