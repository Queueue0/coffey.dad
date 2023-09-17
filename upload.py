from sanic import Blueprint, Request
from sanic_ext import render
from core import auth

bp = Blueprint('upload')


@bp.route('/', ["GET", "POST"], name='upload')
@auth.login_required()
async def upload(request: Request):
    if request.method == "POST":
        for file in request.files.values():
            if file[0].name and file[0].body:
                with open(request.app.config['UPLOAD_PATH'] + '/' + file[0].name, 'wb') as f:
                    f.write(file[0].body)
    return await render(
        "upload/upload.html",
        context={
            **locals(),
        },
    )
