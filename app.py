from flask import Flask, render_template, request, redirect, url_for,  jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, auth


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Todo.db'



db = SQLAlchemy(app)

class Todo(db.Model):
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    TodoName = db.Column(db.String(50), nullable=False)
    CreateTime = db.Column(db.string(50), nullable=False)
    ClearTime = db.Column(db.string(50), nullable=False)

class User(UserMixin, db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    createday = db.Column(db.String(30))

# 仮のTodoリストを作成します
todos = []

# Firebaseからユーザー情報を検証し、データベースに追加する処理
@app.route('/login', methods=['POST'])
def login():
    uid = request.json.get('uid')
    username = request.json.get('username')
    
    # Firebaseでの認証情報検証は省略
    
    user = User.query.filter_by(id=uid).first()
    if user is None:
        user = User(id=uid, username=username)
        db.session.add(user)
        db.session.commit()
    
    return jsonify({'message': 'Logged in successfully', 'user': {'id': uid, 'username': username}})

# Todoリストの画面を表示します。
@app.route('/')
def index():
    return render_template('index.html', todos=todos)

# 追加されたTodoをTodoリストに加えます。
@app.route('/add', methods=['POST'])
def add_todo():
    todo = request.form.get('todo')
    todos.append(todo)
    return redirect(url_for('index'))

# Todoの編集画面を表示します。
@app.route('/edit/<int:todo_id>')
def edit_todo(todo_id):
    # Todoがあるときは編集画面に、そうではないときはTodoリストへ画面遷移します。
    if 1 <= todo_id <= len(todos):
        return render_template('edit.html', todo=todos[todo_id - 1], todo_id=todo_id)
    else:
        return redirect(url_for('index'))

# Todoが更新されたときの処理です。
@app.route('/update/<int:todo_id>', methods=['POST'])
def update_todo(todo_id):
    # 変更されたTodoがある場合はTodoリストに追加する。
    if 1 <= todo_id <= len(todos):
        todo = request.form.get('todo')
        todos[todo_id - 1] = todo
    return redirect(url_for('index'))

# Todoが削除されたときの処理です。
@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    # Todoがあるときは削除する。
    if 1 <= todo_id <= len(todos):
        del todos[todo_id - 1]
    return redirect(url_for('index'))

# アプリを実行する処理です。
if __name__ == '__main__':
    app.run(debug=True)