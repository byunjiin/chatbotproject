#데이터 입력(삽입)하기
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
    sql = '''
    INSERT tb_student(name, age, address) values('Kei', 35, 
    'Korea')
    '''
    with db.cursor() as cursor:
        cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e)
finally:
    if db is not None:
        db.close()