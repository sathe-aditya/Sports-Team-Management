from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
UPLOAD_FOLDER = '/upload'
ALLOWED_EXTENSIONS = set(['jpg','jpeg','png'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS
db = SQLAlchemy(app)
userSession = 0
flag = False

from app import views, models