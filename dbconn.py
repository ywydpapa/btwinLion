import dotenv
import pymysql
import os


dotenv.load_dotenv()
host = os.getenv("host")
charset = os.getenv("charset")
database = os.getenv("db")
user = os.getenv("user")
password = os.getenv("password")


def getuserkey(uno):
    db = pymysql.connect(host=host,user=user,password=password,charset=charset,db=database)
    cursor = db.cursor()
    sql = "select apiKey1, apiKey2 from btUser where userNo = %s"
    cursor.execute(sql, uno)
    result = cursor.fetchone()
    db.close()
    return result

