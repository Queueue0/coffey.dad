from db import get_db


def get_by_username(username):
    db = get_db()
    sql = f'SELECT * FROM user WHERE username={username}'
    db.cursor.execute(sql)
    return db.cursor.fetchone()
