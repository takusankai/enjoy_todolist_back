from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
# datetime モジュールのインポート
from datetime import datetime  



app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Todo.db'



db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
     # User モデルの uid に対する外部キー
    user_id = db.Column(db.Integer, db.ForeignKey('user.uid'), nullable=False) 
    TodoName = db.Column(db.String(50), nullable=False)
    CreateTime = db.Column(db.String(50), nullable=False)
    ClearTime = db.Column(db.String(50), nullable=False)
    

class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    createday = db.Column(db.String(30))
    # User と Todo のリレーションを設定
    todos = db.relationship('Todo', backref='user', lazy=True)


# Firebaseからユーザー情報を検証し、新規ユーザーの時新しくデータベースに追加する処理
@app.route('/login', methods=['GET','POST'])
def login():
    uid = request.json.get('uid')
    username = request.json.get('username')
    
    # Firebaseでの認証情報検証は省略
    
    user = User.query.filter_by(uid=uid).first()
    if user is None:
        user = User(uid=uid, username=username)
        db.session.add(user)
        db.session.commit()
    return jsonify({'message': 'Logged in successfully', 'user': {'id': uid, 'username': username}})


#ログインしたユーザーのTodoリストを返す処理
@app.route('/todos', methods=['GET'])
def get_todos():
    uid = request.args.get('uid')
    # user_id を使用して Todo 項目を検索
    todos = Todo.query.filter_by(user_id=uid).all()
    return jsonify([{'uid': todo.id, 'TodoName': todo.TodoName, 'CreateTime': todo.CreateTime, 'ClearTime': todo.ClearTime} for todo in todos])

#最新10件のデータを返す処理
@app.route('/recent_todos', methods=['GET','POST'])
def get_recent_todos():
    recent_todos = Todo.query.order_by(Todo.CreateTime.desc()).limit(10).all()
    return jsonify([{'id': todo.id, 'TodoName': todo.TodoName, 'CreateTime': todo.CreateTime, 'ClearTime': todo.ClearTime} for todo in recent_todos])


#追加されたTodoをデータベースに入れる処理
@app.route('/add_todo', methods=['POST'])
def add_todo():
    uid = request.json.get('uid')
    todo_name = request.json.get('todo')
    # 現在の時間を取得
    create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    new_todo = Todo(user_id=uid, TodoName=todo_name, CreateTime=create_time, ClearTime='')
    db.session.add(new_todo)
    db.session.commit()
    
    return jsonify({'message': 'Todo added successfully'})

#達成ボタンが押された時クリア時間をデータベースに登録する
@app.route('/clear_todo/<int:todo_id>', methods=['PUT'])
def clear_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if todo:
        todo.ClearTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        db.session.commit()
        return jsonify({'message': 'Todo cleared time successfully'})
    else:
        return jsonify({'message': 'Todo not found'}), 404



# Todoの編集画面を表示します。


# Todoが更新されたときの処理です。


# Todoが削除されたときの処理です。
@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete(todo_id):
    # URLから渡されたIDに基づいて、該当するTodoをデータベースから取得
    todo = Todo.query.filter_by(id=todo_id).first()
    # 取得したTodoをデータベースセッションから削除
    db.session.delete(todo)
    # 変更をデータベースにコミット
    db.session.commit()


# アプリを実行する処理です。
if __name__ == '__main__':
    app.run(debug=True)