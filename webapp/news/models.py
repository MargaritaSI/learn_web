from flask import Blueprint

from webapp.db import db

class News(db.Model):  # atributs of our news
    id = db.Column(db.Integer, primary_key=True)  # first key object/
    title = db.Column(db.String, nullable=False)  # from our news: python_org_news.py
    url = db.Column(db.String, unique=True, nullable=False)  # from python_org_news (url-unique)
    published = db.Column(db.DateTime, nullable=False)  # news data from python_org_news.py
    text = db.Column(db.Text, nullable=True)  # news text (nullable true = text optional)

    def __repr__(self):  # self = each title and url of the news will have its own
        return '<News> {} {}>'.format(self.title, self.url)  # we could see what is it (news)