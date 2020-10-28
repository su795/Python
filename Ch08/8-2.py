import pymysql as db

conn = db.connect(host='192.168.44.46',
                  user='kkm',
                  password='1234',
                  db='kkm',
                  charset='utf8')

cur = conn.cursor()
cur.execute("SELECT * FROM `USER3`")

# fetchall() : db 전체를 가지고 오는 것

for row in cur.fetchall():
    print('---------------------------')
    print('아이디: ', row[0])
    print('이  름: ', row[1])
    print('휴대폰: ', row[2])
    print('나  이: ', row[3])
    print('---------------------------')

conn.close()
