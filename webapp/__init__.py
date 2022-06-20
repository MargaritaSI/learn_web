from flask import Flask, render_template

from webapp.forms import LoginForm
from webapp.model import db, News # link model with flask
from webapp.weather import weather_by_city


def create_app(): # creat fabric function -creates and initializes flask application object
    app = Flask(__name__)
    app.config.from_pyfile('config.py') #take configureation file
    db.init_app(app) # initializing the database, after steps #1 'app' must be created and #2 pick up 'app.configuration..'

    '''@app.route() регистрирует URL-адрес, по которому будет доступно соответствующее представление (расположенное под декоратором),
    а так же правила маршрутизации(механизм сопоставления URL-адреса непосредственно с кодом, который создает веб-страницу.) входящих запросов. Этот декоратор вызывает метод app.'''
    @app.route("/")  # browser requested main page
    # the view function index() prepares the data for display
    def index():  # handler of main page goes to server in a file 'weather' and returns weather
        title = 'News page'
        weather = weather_by_city("app.config['WEATHER_DEFAULT_CITY']") # take city from config.py
        news_list = News.query.order_by(News.published.desc()).all() # take all news from database (don't use 'filter'), sorted with field News.published, desc=revers order
        return render_template('index.html', page_title= title, weather_text=weather, news=news_list) # flask searching dir 'templates' and then 'index.html

    @app.route('/login') #
    def login():
        title = 'Autorization'
        login_form = LoginForm() # create object of Class
        return render_template('login.html', page_title = title, form = login_form) # takes a template, substitutes data there and passes it to the browser

    return app # return flask application


