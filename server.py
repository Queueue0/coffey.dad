import os

from auth import bp as auth_bp
from blog import bp as blog_bp
from core import auth
from dotenv import load_dotenv
from sanic import Request, Sanic
from sanic_session import Session, InMemorySessionInterface

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

auth.setup(app)
session = Session(app, interface=InMemorySessionInterface())

app.static('/static', './static')

app.blueprint(blog_bp, url_prefix="/blog")
app.blueprint(auth_bp, url_prefix="/auth")


@app.get("/", name="home")
@app.ext.template("home.html")
async def hello_world(request: Request):
    return {
        "app": request.app,
        "logged_in": True if auth.current_user(request) else False
    }
