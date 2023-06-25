import pymysql
import pandas as pd

db = None
try:
    #db연결
    db = pymysql.connect(
        host='127.0.0.1',
        port=3307,
        user='root',
        passwd='1234',
        db='homestead',
        charset='utf8'
    )
    #테이블생성
    sql = '''
    CREATE TABLE user-info (
        id int primary key auto_increment not null,
        이름 varchar(32),
        성별 varchar(32),
        나이 int,
        전화번호 varchar(32),
        국적 varchar(32),
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    '''
    with db.cursor() as cursor:
        cursor.execute(sql)
    db.commit()
    
    #데이터 넣기
    info = [
        {'이름': '김철수', '성별':'남자', '나이': 15, '전화번호':'010-1234-5678', '국적':'한국'},
        {'이름': '홍길동', '성별':'남자', '나이': 35, '전화번호':'010-2222-3333', '국적':'한국'},
        {'이름': 'Jason', '성별':'남자', '나이': 21, '전화번호':'010-1212-2323', '국적':'미국'},
        {'이름': '이영희', '성별':'여자', '나이': 22, '전화번호':'010-9876-1234', '국적':'한국'},
        {'이름': 'emma', '성별': '여자','나이': 27, '전화번호':'010-4567-7890', '국적':'스페인'},
    ]
    for s in info:
        with db.cursor() as cursor:
            sql = '''
                insert user-info(이름, 성별, 나이, 전화번호, 국적) 
                values("%s","%s",%d,"%s","%s")
            ''' % (s['이름'], s['성별'], s['나이'], s['전화번호'], s['국적'])
        cursor.execute(sql)
    db.commit()

except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()
