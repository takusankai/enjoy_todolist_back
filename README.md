# Enjoy_todolist
技育Camp マンスリーハッカソン vol.14 2024/2/2～2024/2/2

このリポジトリはEnjoy_todolistのバックエンド部分です。

todolistを登録し参照するだけでなく、自分のタスク達成を褒めてもらえたり他の人のタスク達成に評価が出来たりすることを目指した作品です。

以下は環境構築の備考です。<br><br><br>

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
