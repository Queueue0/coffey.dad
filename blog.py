import markdown as md
from markdown.extensions.extra import ExtraExtension
from sanic import Blueprint, Request, response
from sanic_auth import User
from sanic_ext import render

from core import auth
from models import post_model


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


@bp.route("/new", ["GET", "POST"], name="add_post")
@auth.login_required(user_keyword='user')
async def add_post(request: Request, user: User):
    if request.method == "POST":
        title = request.form.get("title")
        body = request.form.get("body")
        print(post_model.add(title, body))
        return response.redirect("/blog")
    return await render(
        "blog/add.html",
        context={
            **locals(),
        },
    )