#데이터 삭제하기

import pymysql
db = None
try:
    db = pymysql.connect(
        host='127.0.0.1',
        port=3307,
        user='root',
        passwd='1234',
        db='homestead',
        charset='utf8'
    )
    id = 1 # 데이터 id (PK)
    sql = '''
        DELETE from tb_student where id=%d
        ''' % id
    with db.cursor() as cursor:
        cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e)
finally:
    if db is not None:
        db.close()