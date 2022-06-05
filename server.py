from flask import Flask, render_template

from python_org_news import get_python_news
from weather import weather_by_city

app = Flask(__name__)


# the view function index() prepares the data for display
@app.route("/")  # browser requested main page
def index():  # handler of main page goes to server in a file 'weather' and returns weather
    title = 'News page'
    weather = weather_by_city("Amsterdam,Netherlands")
    news_list = get_python_news() # send templates 'news'
    return render_template('index.html', page_title= title, weather_text=weather, news=news_list) # flask searching dir 'templates' and then 'index.html


if __name__ == "__main__":
    app.run(debug=True)
