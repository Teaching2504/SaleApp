import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import cloudinary

app = Flask(__name__)

app.secret_key = "adfshgjksjsakhgkshg"
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:root@localhost/saledb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"]=3

db = SQLAlchemy(app)
#Cloudynary acc gmail cua tuyetrinhnguyenthi25042005@gmail.com
cloudinary.config(cloud_name= 'dczz59gpu',
                  api_key='869438865392334',
                  api_secret='fMGWJrAEn9SB4r-5xzKi9bLiTME',)

login = LoginManager(app)