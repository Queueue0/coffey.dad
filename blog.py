import markdown as md
from markdown.extensions.extra import ExtraExtension
from sanic import Blueprint, Request, Sanic

from test_posts import posts

bp = Blueprint("blog")
app = Sanic.get_app("coffey_dad")


@bp.route("/", ["GET"], name="blog")
@app.ext.template("blog/list.html")
async def blog_root(request: Request):
    markdown = ""
    extensions = [ExtraExtension()]

    for post in posts:
        post['text'] = md.markdown(post['text'], extensions=extensions)
    return {"app": app, "posts": posts}
