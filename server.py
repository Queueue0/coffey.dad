from sanic import Request, Sanic

app = Sanic("coffey_dad")

from blog import bp as blog_bp

app.static('/static', './static')

app.blueprint(blog_bp, url_prefix="/blog")


@app.get("/", name="home")
@app.ext.template("home.html")
async def hello_world(request: Request):
    return {"app": app}
