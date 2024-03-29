import os

import aioredis
import markdown as md
from dotenv import load_dotenv
from markdown.extensions.extra import ExtraExtension
from sanic import Request, Sanic
from sanic_session import Session, AIORedisSessionInterface

from auth import bp as auth_bp
from blog import bp as blog_bp
from core import auth
from models import post_model
from upload import bp as upload_bp


load_dotenv()

app = Sanic("coffey_dad")

app.config.AUTH_LOGIN_ENDPOINT = 'auth.login'

db_settings = {
    'DB_HOST': os.getenv('DB_HOST'),
    'DB_PORT': int(os.getenv('DB_PORT')),
    'DB_USER': os.getenv('DB_USER'),
    'DB_PASS': os.getenv('DB_PASS'),
    'DB_NAME': os.getenv('DB_NAME'),
}
app.config.update(db_settings)

app.config['REDIS'] = os.getenv('REDIS_URL')
app.config['UPLOAD_PATH'] = os.getenv('UPLOAD_PATH')

auth.setup(app)
session = Session()


@app.listener('before_server_start')
async def server_init(app, loop):
    app.ctx.redis = aioredis.from_url(
        app.config['REDIS'], decode_responses=True)
    session.init_app(app, interface=AIORedisSessionInterface(app.ctx.redis))

app.static('/static', './static')

app.blueprint(blog_bp, url_prefix="/blog")
app.blueprint(auth_bp, url_prefix="/auth")
app.blueprint(upload_bp, url_prefix="/upload")


@app.get("/", name="home")
@app.ext.template("home.html")
async def hello_world(request: Request):
    posts = post_model.get_paginated(limit=5)
    for post in posts:
        post['body'] = md.markdown(post['body'], extensions=[ExtraExtension()])
    return {
        **locals(),
    }
