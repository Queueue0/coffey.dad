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
@auth.login_required()
async def add_post(request: Request):
    if request.method == "POST":
        title = request.form.get("title")
        body = request.form.get("body")
        post_model.add(title, body)
        return response.redirect("/blog")
    return await render(
        "blog/add.html",
        context={
            **locals(),
        },
    )


@bp.route("/edit/<post_id>", ["GET", "POST"], name="edit_post")
@auth.login_required()
async def edit_post(request: Request, post_id: int):
    if request.method == "POST":
        title = request.form.get("title")
        body = request.form.get("body")
        post_model.update(post_id, title, body)
        return response.redirect(request.app.url_for('blog.post', post_id=post_id))
    post = post_model.get_by_id(post_id)
    return await render(
        "blog/edit.html",
        context={
            **locals(),
        },
    )


@bp.route("/post/<post_id>", name="post")
async def view_post(request: Request, post_id: int):
    post = post_model.get_by_id(post_id)
    post['body'] = md.markdown(post['body'], extensions=[ExtraExtension()])
    return await render(
        "blog/post.html",
        context={
            **locals(),
        },
    )
