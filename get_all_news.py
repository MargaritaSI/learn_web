# if we want use flask-sqlalchemy(make request to db) not from a flask application - creat file with that we will be takes news

from webapp import create_app
from webapp.python_org_news import get_python_news

app = create_app()
with app.app_context():
    get_python_news()