from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "123"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project01:project01password@localhost/project01"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
#Upload files will be stored here
app.config['UPLOAD_FOLDER'] = "./app/static/uploads"
db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views

