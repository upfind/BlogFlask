# encoding: utf-8
from flask import Flask, render_template, request, redirect, url_for, session
import config
from exts import db
from models import User

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        phone = request.form.get('phone')
        pwd = request.form.get('pwd')
        user = User.query.filter(User.phone == phone, User.password == pwd).first()
        if user:
            # 如果想在31天之内不需要重复登录
            session['user_id'] = user.id
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return u'手机号码或者密码错误！请确认后再操作'


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        #         做两部判断 1如果已注册将不能注册 2两个密码相同
        phone = request.form.get('phone')
        username = request.form.get('username')
        pwd = request.form.get('pwd')
        checkpwd = request.form.get('checkpwd')
        user = User.query.filter(User.phone == phone).first()
        if user:
            return u'该手机号码已被注册，请更换手机号码！'
        else:
            if pwd != checkpwd:
                return u'两次输入密码不相等'
            else:
                user = User(phone=phone, username=username, password=pwd)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))


@app.route('/test/')
def test():
    return "测试"


if __name__ == '__main__':
    app.run()
