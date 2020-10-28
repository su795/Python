from flask import Blueprint, render_template
import pymysql as db

list_blueprint = Blueprint('list', __name__)


@list_blueprint.route('/list')
def list():

    # 데이터 베이스 접속
    conn = db.connect(host='192.168.44.46',
                      user='kkm',
                      password='1234',
                      db='kkm',
                      charset='utf8')

    # 쿼리문 실행 객체 생성
    cur = conn.cursor()

    # 쿼리문 실행
    cur.execute("SELECT * FROM `USER3`")
    conn.commit()

    # fetchall() : db 전체를 가지고 오는 것
    users = []
    for row in cur.fetchall():
        user = {
            'uid': row[0],
            'name': row[1],
            'hp': row[2],
            'age': row[3]
        }
        users.append(user)

    # 데이터베이스 종료
    conn.close()

    return render_template('/list.html', users=users)