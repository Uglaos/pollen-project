from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from apscheduler.schedulers.background import BackgroundScheduler
import subprocess
from flask_marshmallow import Marshmallow


def call_crawl():
    subprocess.call(['scrapy', 'crawl', "thespider"], shell=True, cwd='../PollenSpider/PollenSpider')


# sched = BackgroundScheduler(daemon=True)
# sched.add_job(call_crawl, 'interval', days=1)
# sched.start()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:wolf330312@localhost/pollendb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

from pollenapp import routes
