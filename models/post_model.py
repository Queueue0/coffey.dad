from db import get_db


def get_all():
    db = get_db()
    db.cursor.execute('SELECT * FROM post ORDER BY created ASC')
    return db.cursor.fetchall()


def add(title, body):
    db = get_db()
    data = {
        'title': title,
        'body': body,
    }
    db.cursor.execute(
        'INSERT INTO post(title, body) VALUES (%(title)s, %(body)s)',
        data
    )
    return db.cursor.lastrowid


def get_by_id(id):
    db = get_db()
    data = {
        'id': id,
    }
    db.cursor.execute('SELECT * FROM post WHERE id=%(id)s', data)
    return db.cursor.fetchone()
