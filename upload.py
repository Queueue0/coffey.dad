from sanic import Blueprint, Request, response
from sanic_ext import render
from core import auth


bp = Blueprint('upload')


@bp.route('/', ["GET", "POST"], name='upload')
@auth.login_required()
async def upload(request: Request):
    return await render(
        "upload/upload.html",
        context={
            **locals(),
        },
    )
