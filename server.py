from sanic import Sanic, exceptions, response
from sanic.response import text

app = Sanic("coffey_dad")
redirect = Sanic("http")

redirect.static("/.well-known", "/var/www/.well-known", resource_type="dir")

@redirect.exception(exceptions.NotFound, exceptions.MethodNotSupported)
def redirect_everything_else(request, exception):
    server, path = request.server_name, request.path
    if server and path.startswith("/"):
        return response.redirect(f"https://{server}{path}", status=308)
    return response.text("Bad Request. Please use HTTPS!", status=400)


@app.get("/")
async def hello_world(request):
    return text("Under construction, nothing to see here")


@app.before_server_start
async def start(app, _):
    app.ctx.redirect = await redirect.create_server(
        port=8080, return_asyncio_server=True
    )
    app.add_task(runner(redirect, app.ctx.redirect))


@app.before_server_stop
async def stop(app, _):
    await app.ctx.redirect.close()


async def runner(app, app_server):
    app.state.is_running = True
    try:
        app.signalize()
        app.finalize()
        app.state.is_started = True
        await app_server.serve_forever()
    finally:
        app.state.is_running = False
        app.state.is_stopping = True
