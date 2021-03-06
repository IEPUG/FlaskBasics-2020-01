from flask import Flask, Response, url_for, request, redirect
import flask_login
from werkzeug.security import check_password_hash
import os

# from werkzeug.security import generate_password_hash
# secret_password = generate_password_hash('123')
SECRET_PASSWORD = 'pbkdf2:sha256:150000$YIRjKdAf$8b7d1252ce5c1b9a8889856ffc34ebaec52a6c76e251aef275d071c1de75bca9'
MY_USER = 'john'

app = Flask(__name__)

login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
app.config['SECRET_KEY'] = os.urandom(16)


class User(flask_login.UserMixin):
    def __init__(self, userid):
        self.id = userid


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for('login'), 302)


html_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>Flask Demo</title>
    </head>
    <body>
"""

html_footer = """
    </body>
</html>
"""


@app.route('/')
def index():
    image_url = url_for('static', filename='python.png')
    login_url = url_for('login')
    html_body = """
    <h1>This is Python!!!</h1>
    <img src="{0}">
    <div><a href="{1}">Login</a></div>
    """.format(image_url, login_url)
    response = ''.join([html_header, html_body, html_footer])

    return Response(response, 200)


@app.route('/about')
@flask_login.login_required
def about():
    return Response('This is my flask app!', 200)


@app.route('/login')
def login():
    login_url = url_for('do_login')
    html_body = """
        <form action="{0}" method="POST">
            <div>
                <div>
                    <label>User Name:</label>
                    <input type="text" value="" placeholder="username" name="username">
                </div>
                <div class="control-group">
                    <label>Password:</label>
                    <input type="password" value="" placeholder="password" name="password">
                </div>
                <input type="submit" value="Log in">
            </div>
        </form
    """.format(login_url)
    response = ''.join([html_header, html_body, html_footer])

    return Response(response, 200)


@app.route('/do_login/', methods=['POST'])
def do_login():
    username = request.form['username'].lower()
    pwd = request.form['password']
    if username == MY_USER and check_password_hash(SECRET_PASSWORD, pwd):
        flask_login.login_user(User(username))
        return redirect(url_for('about'), 302)
    else:
        flask_login.logout_user()
        return redirect(url_for('login'), 302)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
