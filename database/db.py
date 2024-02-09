import sqlite3
# SQLite3のデータベースに接続

def db_template():
    conn = sqlite3.connect('database.db')
    #カーソルを取得
    cursor = conn.cursor()
    #テーブル作成のSQL文
    create_table_sql = '''

    CREATE TABLE IF NOT EXISTS data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
    '''

    #SQL実行
    cursor.execute(sql)
    #データベースへの変更を保存
    conn.commit()
    #データベース接続を閉じる
    conn.close()

