from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#フラスククラスのインスタンス生成しapp変数に格納
app=Flask(__name__)
#Config {... 'DATABASE': '/tmp/flaskr.db', 'DEBUG': True, 'SECRET_KEY': 'development key', 'USERNAME': 'admin', 'PASSWORD': 'default'}
#config辞書に含まれるデータをconfig.pyで一括管理
app.config.from_object("main.config")

#app変数を代入してSQLalchemyインスタンスを生成。db変数に格納
db=SQLAlchemy(app)
import main.views

