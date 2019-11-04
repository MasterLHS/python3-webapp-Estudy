import MySQLdb

username = "' OR 1=1 #"
password = 'pbkdf2_sha256$150000$T1lKrRBruX7x$gN0vnJvQ0Y4j4pns8MeSLI8XxhZEUs8vCY8RuzXyhcQ='
conn = MySQLdb.connect(host='127.0.0.1', user='root', password='lhsxyfzzh520', db='estudy', charset='utf8')
cursor = conn.cursor()

sql = "select * from users_userprofile where username='{}' and password='{}'".format(username,password)
cursor.execute(sql)

for row in cursor.fetchall():
    print(row)


#1.