from flask import Flask, flash, render_template, redirect, url_for
''' flash-send messages between routes, redirect-redirects the user to another page, 
url_for-helps to get the url by the name of the function that processes this url  '''

from flask_login import LoginManager # LoginManager -managing login process

from webapp.db import db  # link model with flask
from webapp.admin.views import blueprint as admin_blueprint # for connect blueprint with application
from webapp.news.views import blueprint as news_blueprint
from webapp.user.models import User  # link model with flask
from webapp.user.views import blueprint as user_blueprint # for connect blueprint with application
from webapp.weatherhere import weather_by_city


def create_app():  # creat fabric function -creates and initializes flask application object
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_pyfile('config.py')  # take configureation file
    db.init_app(app)  # initializing the database, after steps #1 'app' must be created and #2 pick up 'app.configuration..'

    login_manager = LoginManager()  #
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'  # this is how will called function def 'login'
    app.register_blueprint(user_blueprint) # regisrtation blueprint for connection with application
    app.register_blueprint(admin_blueprint) # regisrtation blueprint
    app.register_blueprint(news_blueprint)

    @login_manager.user_loader  # every time on open page login_manager takes cookes user_id and send it to 'load_user'
    def load_user(user_id):  # take user with id
        return User.query.get(user_id)  # ask database with id_user - object user for work

    '''@app.route() регистрирует URL-адрес, по которому будет доступно соответствующее представление (расположенное под декоратором),
    а так же правила маршрутизации(механизм сопоставления URL-адреса непосредственно с кодом, который создает веб-страницу.) входящих запросов. Этот декоратор вызывает метод app.'''



    return app  # return flask application
