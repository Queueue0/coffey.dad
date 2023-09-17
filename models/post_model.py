from db import get_db


def get_all():
    db = get_db()
    db.cursor.execute('SELECT * FROM post ORDER BY created DESC')
    return db.cursor.fetchall()


def get_paginated(offset=0, limit=10):
    db = get_db()
    data = {
        'offset': offset,
        'limit': limit,
    }
    db.cursor.execute(
        'SELECT * FROM post ORDER BY created DESC LIMIT %(offset)s, %(limit)s',
        data
    )
    return db.cursor.fetchall()


def add(title, body):
    db = get_db()
    data = {
        'title': title,
        'body': body,
    }
    db.cursor.execute(
        'INSERT INTO post (title, body) VALUES (%(title)s, %(body)s)',
        data
    )
    db.commit()
    return db.cursor.lastrowid


def update(id, title, body):
    db = get_db()
    data = {
        'id': id,
        'title': title,
        'body': body,
    }
    db.cursor.execute(
        'UPDATE post SET title=%(title)s, body=%(body)s WHERE id=%(id)s',
        data
    )
    db.commit()
    return db.cursor.lastrowid


def get_by_id(id):
    db = get_db()
    data = {
        'id': id,
    }
    db.cursor.execute('SELECT * FROM post WHERE id=%(id)s', data)
    return db.cursor.fetchone()
