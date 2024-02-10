import sqlite3
import os

# 現在のファイルのディレクトリを取得
current_directory = os.path.dirname(__file__)
# 一つ上のディレクトリのパスを取得
parent_directory = os.path.dirname(current_directory)
# データベースファイルのパスを組み立て
database_path = os.path.join(parent_directory, 'todoapp.db')

# データベース接続を作成 (ファイルが存在しない場合は新たに作成される)
conn = sqlite3.connect(database_path)

# カーソルオブジェクトを作成
c = conn.cursor()

# Userテーブルを作成するSQLクエリ
create_table_query1 = '''
CREATE TABLE IF NOT EXISTS user (
    USERID INTEGER PRIMARY KEY AUTOINCREMENT,
    GoogleID TEXT NOT NULL UNIQUE,
    USERNAME TEXT NOT NULL,
    CREATE_DATE TEXT NOT NULL
);
'''

# Userテーブルを作成
c.execute(create_table_query1)

# Userテーブルを作成するSQLクエリ
create_table_query2 = '''
CREATE TABLE IF NOT EXISTS TODO (
    TOID INTEGER PRIMARY KEY AUTOINCREMENT,
    USERID INTEGER NOT NULL,
    TODONAME TEXT NOT NULL,
    CREATE_TIME TEXT NOT NULL,
    FINISH_TIME TEXT
);
'''

# Userテーブルを作成
c.execute(create_table_query2)

# ユーザーデータを挿入するためのSQLクエリとデータ

# 変更をコミット
conn.commit()

# データベース接続を閉じる
conn.close()

print('データベースとテーブルが正常に作成されました。')
