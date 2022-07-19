from flask import Blueprint, current_app, render_template  # link model with flask
from webapp.news.models import News
from webapp.weatherhere import weather_by_city

blueprint = Blueprint('news', __name__) # name Blueprint, modul name, main page without prefix(start of all urls)

@blueprint.route('/')  # browser requested main page
# the view function index() prepares the data for display
def index():  # handler of main page goes to server in a file 'weather' and returns weather
    title = 'News page'
    weather = weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'])  # take city from config.py
    print(weather)
    news_list = News.query.order_by(
        News.published.desc()).all()  # take all news from database (don't use 'filter'), sorted with field News.published, desc=revers order
    return render_template('news/index.html', page_title=title, weather_text=weather,
                           news=news_list) # flask searching dir 'templates' and then 'index.html
