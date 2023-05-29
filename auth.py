from bcrypt import checkpw
from core import auth
from models import auth_user_model
from sanic import Blueprint, Request, response
from sanic_auth import User

bp = Blueprint('auth')

LOGIN_FORM = '''
<h2>Please sign in, you can try:</h2>
<dl>
<dt>Username</dt> <dd>demo</dd>
<dt>Password</dt> <dd>1234</dd>
</dl>
<p>{}</p>
<form action="" method="POST">
  <input class="username" id="name" name="username"
    placeholder="username" type="text" value=""><br>
  <input class="password" id="password" name="password"
    placeholder="password" type="password" value=""><br>
  <input id="submit" name="submit" type="submit" value="Sign In">
</form>
'''


@bp.route('/login', methods=['GET', 'POST'])
async def login(request: Request):
    message = ''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = auth_user_model.get_by_username('username')

        if user and checkpw(password, user['password']):
            user = User(id=1, name=username)
            auth.login_user(request, user)
            return response.redirect('/')
        message = 'invalid username or password'
    return response.html(LOGIN_FORM.format(message))


@bp.route('/logout')
@auth.login_required
async def logout(request: Request):
    auth.logout_user(request)
    return response.redirect('/')


@bp.route('/test')
@auth.login_required(user_keyword='user')
async def profile(request, user):
    return response.text('It works')
