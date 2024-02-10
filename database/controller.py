import sqlite3
import os

# 現在のファイルのディレクトリを取得
current_directory = os.path.dirname(__file__)
# 一つ上のディレクトリのパスを取得
parent_directory = os.path.dirname(current_directory)
# データベースファイルのパスを組み立て
database_path = os.path.join(parent_directory, "todoapp.db")
# データベースファイルのパスを指定

# データベース接続を作成
conn = sqlite3.connect(database_path)
c = conn.cursor()

# ユーザーテーブルとTODOテーブルを結合してデータを取得するSQLクエリ
select_query = """
SELECT u.USERID, u.USERNAME, t.TOID, t.TODONAME, t.CREATE_TIME, t.FINISH_TIME
FROM user u
JOIN TODO t ON u.USERID = t.USERID
"""

# データを取得
c.execute(select_query)
result = c.fetchall()

# 結果を出力
for row in result:
    print(
        f"USERID: {row[0]}, USERNAME: {row[1]}, TOID: {row[2]}, TODONAME: {row[3]}, "
        f"CREATE_TIME: {row[4]}, FINISH_TIME: {row[5]}"
    )

conn.close()
