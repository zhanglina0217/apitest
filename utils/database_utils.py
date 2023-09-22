import pymysql


def get_conn():
    conn = pymysql.connect(
        host="performance.beta-test.rishiqing.com",
        port=443,
        j_username="13811111111",
        j_password="123456",
        database="performance",
        charset="utf8mb4"
    )