import markdown as md
from markdown.extensions.extra import ExtraExtension
from models import post_model
from sanic import Blueprint, Request
from sanic_ext import render

bp = Blueprint("blog")


@bp.route("/", ["GET"], name="blog")
async def blog_root(request: Request):
    posts = post_model.get_all()

    for post in posts:
        post['body'] = md.markdown(post['body'], extensions=[ExtraExtension()])

    return await render(
        "blog/list.html",
        context={
            **locals(),
        },
    )
