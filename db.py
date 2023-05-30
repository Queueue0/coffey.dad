import pymysql
from sanic import Sanic


def get_db():
    app = Sanic.get_app('coffey_dad')
    if not hasattr(app.ctx, 'db') or not app.ctx.db.open:
        app.ctx.db = pymysql.connect(
            host=app.config['DB_HOST'],
            port=app.config['DB_PORT'],
            user=app.config['DB_USER'],
            password=app.config['DB_PASS'],
            db=app.config['DB_NAME'],
            cursorclass=pymysql.cursors.DictCursor,
        )

        app.ctx.db.cursor = app.ctx.db.cursor()
    return app.ctx.db
