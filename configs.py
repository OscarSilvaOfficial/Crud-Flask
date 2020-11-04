import MySQLdb

conn = MySQLdb.connect(
    user='root',
    passwd='',
    db='flask',
    host='127.0.0.1',
)

cursor = conn.cursor()

cursor.execute('SELECT * ')