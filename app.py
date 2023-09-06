from flask import Flask
from markupsafe import escape
# url_for（）函数
from flask import url_for
# http方法
from flask import request
# 渲染模板
from flask import render_template
# 请求对象
from flask import request
# 文件上传的安全文件名函数
from werkzeug.utils import secure_filename

app = Flask(__name__)


# flask run --debug
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!hhhhhh'


# html转义
# @app.route('/<name>')
# def hello_name(name):  # put application's code here
#     return f'Hello,{escape(name)}!'


# 变量规则
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


# 唯一的URL/重定向行为
@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


# url_for()函数
@app.route('/')
def index():
    return 'index'


@app.route('/login')
def login():
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    # 静态文件
    print(url_for('static', filename='style.css'))


# http方法  get和post方法分别处理
@app.route('/login_http/', methods=['GET', 'POST'])
def login_http():
    if request.method == 'POST':
        return "do login post"
    else:
        return "show_the_login_form()  get"


@app.get('/login_http')
def login_get():
    return "show_the_login_form"


@app.post('/login_http')
def login_post():
    return "do_the_login"


# 渲染模板
@app.route('/hello_template/')
@app.route('/hello_template/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/login', methods=['POST', 'GET'])
def login_request():
    error = None
    if request.method == 'POST':
        pass
        # 如果是post方式就判断登陆的合法性
        # if valid_login(request.form['username'],
        #                request.form['password']):
        #     return log_the_user_in(request.form['username'])
        # else:
        #     error = 'Invalid username/password'
    # the code below is executed if the request method was GET or the credentials were invalid
    return render_template('login.html', error=error)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['the_file']
        file.save(f"/var/www/uploads/{secure_filename(file.filename)}")


if __name__ == '__main__':
    app.run()
