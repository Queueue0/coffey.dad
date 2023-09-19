import os
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
                filename = file[0].name.replace(' ', '_')
                with open(request.app.config['UPLOAD_PATH'] + '/' + filename, 'wb') as f:
                    f.write(file[0].body)
    return await render(
        "upload/upload.html",
        context={
            **locals(),
        },
    )


@bp.route('/choose-image', ["GET"], name='image_picker')
@auth.login_required()
async def image_picker(request: Request):
    urls = []
    upload_path = request.app.config['UPLOAD_PATH']
    paths = os.listdir(upload_path)
    if len(paths) > 0:
        print(paths)
        for path in paths:
            if os.path.isfile(upload_path + '/' + path):
                url = request.app.url_for(
                    'static', name='static', filename='uploads/' + path)
                urls.append(url)
    return await render(
        "upload/image_picker.html",
        context={
            'request': request,
            'images': urls,
        }
    )
