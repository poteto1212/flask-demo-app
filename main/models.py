#sqlalchemyでモデル作成
from main import db
from flask_sqlalchemy import SQLAlchemy

class Entry(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.Text)
    text=db.Column(db.Text)
    
    #データ構造を定義する関数
    def __repr__(self):
        return "<Entry id={} title={!r}>".format(self.id, self.title)

#データベース作成処理
#db変数のメソッドを実行させる処理
def init():
    db.create_all()
    
        