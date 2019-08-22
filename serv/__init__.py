from flask import Flask
from config import Config
from serv.db_cross import DBConnector

app = Flask(__name__)
app.config.from_object(Config)

db = DBConnector(app.config)

from serv import routes
