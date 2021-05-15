#起動用ファイル

#mainディレクトリからapp変数をインポート
from main import app

#run.pyを直接実行した時だけappモジュールを起動
if __name__=="__main__":
    app.run(debug=True)