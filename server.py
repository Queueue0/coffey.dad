from sanic import Sanic
from sanic_ext import render
from textwrap import dedent

app = Sanic("coffey_dad")

@app.get("/")
async def hello_world(request):
    template = dedent("""
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <title>coffey.dad</title>
            </head>

            <body>
                <h1>Under construction</h1>
                <p>Nothing to see here!</p>    
            </body>
        </html>
    """)

    return await render(
        template_source=template,
        app=app,
    )
