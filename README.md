# Enjoy_todolist_backend

## venvで仮想環境を構築
python -m venv env
// Linuxで仮想環境を有効化
env/bin/activate
// Windowsで仮想環境を有効化
env/scripts/activate
// pip commandのアップグレード
python.exe -m pip install --upgrade pip

## 仮想環境にrequirements.txtを使って開発に使うライブラリをインストール
pip install -r requirements.txt

## 新しくライブラリをインストールしたらrequirements.txtを更新する
pip freeze > requirements.txt

## Sqlite3のDBを作成
python database/create.py