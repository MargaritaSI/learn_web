from flask import Flask, render_template

from webapp.python_org_news import get_python_news
from webapp.weather import weather_by_city

def create_app(): # creat fabric function -creates and initializes flask application object
    app = Flask(__name__)
    app.config.from_pyfile('config.py') #take configureation file
# the view function index() prepares the data for display
    @app.route("/")  # browser requested main page
    def index():  # handler of main page goes to server in a file 'weather' and returns weather
        title = 'News page'
        weather = weather_by_city("app.config['WEATHER_DEFAULT_CITY']") # take city from config.py
        news_list = get_python_news() # send templates 'news'
        return render_template('index.html', page_title= title, weather_text=weather, news=news_list) # flask searching dir 'templates' and then 'index.html

    return app # return flask application


