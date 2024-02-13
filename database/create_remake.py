import sqlite3
import os

# 主キーがstringになったため、作成されるデータベースのデータ型が変更されています。

# 現在のファイルのディレクトリを取得
current_directory = os.path.dirname(__file__)
# 一つ上のディレクトリのパスを取得
parent_directory = os.path.dirname(current_directory)
# データベースファイルのパスを組み立て
database_path = os.path.join(parent_directory, "todoapp.db")

# データベース接続を作成 (ファイルが存在しない場合は新たに作成される)
conn = sqlite3.connect(database_path)

# カーソルオブジェクトを作成
c = conn.cursor()

# Userテーブルを作成するSQLクエリ
create_table_query1 = """
CREATE TABLE IF NOT EXISTS user (
    user_id TEXT PRIMARY KEY,
    GoogleID TEXT NOT NULL UNIQUE,
    USERNAME TEXT NOT NULL,
    CREATE_DATE TEXT NOT NULL
);
"""

# Userテーブルを作成
c.execute(create_table_query1)

# # Userテーブルを作成するSQLクエリ
create_table_query2 = """
CREATE TABLE IF NOT EXISTS TODO (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    TodoName TEXT NOT NULL,
    CreateTime TEXT NOT NULL,
    ClearTime TEXT,
    is_completed BOOLEAN DEFAULT FALSE
);
"""

# Userテーブルを作成
c.execute(create_table_query2)

# ユーザーデータを挿入するためのSQLクエリとデータ
insert_user_query = """
INSERT INTO user (GoogleID, USERNAME, CREATE_DATE)
VALUES (?, ?, ?)
"""

user_data = [
    ("google_id_1", "User 1", "2022-01-01"),
    ("google_id_2", "User 2", "2022-01-02"),
    ("XEwNDL0KAFckMLqUdfdTI9apOE42", "User 3", "2022-01-03"),
]

# ユーザーデータを挿入
c.execute("DELETE FROM user")
c.executemany(insert_user_query, user_data)

# Todoテーブルのレコードを作成するSQLクエリとデータ
insert_todo_query = """
INSERT INTO TODO (id, user_id, TodoName, CreateTime, ClearTime)
VALUES (?, ?, ?, ?, ?)
"""

todo_data = [
    ("a", "XEwNDL0KAFckMLqUdfdTI9apOE42", "データベースについて知る", "20220101120000", None),
    ("ab", "1", "Task 2", "20220101120000", None),
    ("abc", "2", "Task 3", "20220101120000", None),
    ("abcd", "2", "Task 4", "20220101120000", None),
    ("abcde", "3", "Task 5", "20220101120000", None),
    ("abcdef", "1", "Task 6", "20220101120000", "20220107120000"),
    ("abcdefg", "2", "Task 7", "20220101120000", "20220108120000"),
    ("abcdefgh", "XEwNDL0KAFckMLqUdfdTI9apOE42", "reactを書いてみる", "20220101120000", "20220109120000"),
    ("abcdefgha", "1", "Task 9", "20220101120000", "20220110120000"),
    ("abcdefghs", "2", "Task 10", "20220101120000", "20220111120000"),
    ("abcdefghd", "3", "Task 11", "20220101120000", "20220112120000"),
    ("abcdefghf", "1", "Task 12", "20220101120000", "20220113120000"),
    ("abcdefghas", "2", "Task 13", "20220101120000", "20220114120000"),
    ("abcdefghasd", "3", "Task 14", "20220101120000", "20220115120000"),
    ("abcdefghasdf", "XEwNDL0KAFckMLqUdfdTI9apOE42", "アプリケーションをデプロイする", "20220101120000", "20220116120000"),
]

# Todoテーブルのレコードを挿入
c.executemany(insert_todo_query, todo_data)
# 変更をコミット
conn.commit()
conn.close()

print("データベースとテーブルが正常に作成されました。")
