"""
    날짜 : 2020/06/24
    이름 : 오세훈
    내용 : 파이썬 데이터베이스 프로그래밍
"""
import pymysql as db

# Terminal에서 pip3 install pymysql 입력

# 데이터베이스 접속
conn = db.connect(host='192.168.44.46',
                  user='kkm',
                  password='1234',
                  db='kkm',
                  charset='utf8')

# 쿼리문 실행객체 생성
cur = conn.cursor()

# 쿼리문 실행
cur.execute("INSERT INTO `USER3` VALUES ('I101', '을파소', '010-2222-4156', 23)")

# 쿼리문 실행 확정
conn.commit()

# 데이터베이스 종료
cur.close()
