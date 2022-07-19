from datetime import timedelta # Duration of saving the authorization status
import os  # path module

# specifies the full path to config.py
basedir = os.path.abspath(os.path.dirname(__file__))  # config in this folder (absolute path) -set path to file without prescribing it "manually"
WEATHER_DEFAULT_CITY = ("Amsterdam,Netherlands")  # capslock = permanet varaeble -don't change
WEATHER_API_KEY = "f1a03b96797b126f6a94ca5a8099947e"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
# configuration where our database is located (if we don't have sqlite) set path to database
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join( basedir, "..", "webapp.db")  # path for db/ 1 directory upper(lear_nweb) where our db/ name for db

SECRET_KEY = 'OISDH:KJB:BEhkjds'

REMEMBER_COOKIE_DURATION= timedelta(days=5)