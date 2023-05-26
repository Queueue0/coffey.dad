from sanic import Request, Sanic

app = Sanic("coffey_dad")
app.static('/static', './static')

@app.get("/", name="home")
@app.ext.template("home.html")
async def hello_world(request: Request):
    return {"app": app}
