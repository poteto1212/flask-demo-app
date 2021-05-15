#データベース設定
import os

#右辺はherokuデータベースを使用
#左辺はローカル開発時のデータベース
SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL?sslmode=require') or "sqlite:///test.db"
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY="secret key"