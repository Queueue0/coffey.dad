import markdown as md
from markdown.extensions.extra import ExtraExtension
from sanic import Blueprint, Request
from sanic_ext import render

from test_posts import posts

bp = Blueprint("blog")


@bp.route("/", ["GET"], name="blog")
async def blog_root(request: Request):
    extensions = [ExtraExtension()]

    for post in posts:
        post['text'] = md.markdown(post['text'], extensions=extensions)

    return await render(
        "blog/list.html",
        context={"app": request.app, "posts": posts},
    )
