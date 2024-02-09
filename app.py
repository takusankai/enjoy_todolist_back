from flask import Flask, jsonify, request

app = Flask(__name__)

# サンプルのデータ
data = [
    {"id": 1, "name": "John Doe"},
    {"id": 2, "name": "Jane Smith"}
]
@app.route('/')
def index():
    return 'Hello World'

# GETリクエストの処理
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(data)

# POSTリクエストの処理
@app.route('/api/data', methods=['POST'])
def add_data():
    new_data = request.get_json()
    data.append(new_data)
    return jsonify(new_data), 201

# PUTリクエストの処理
@app.route('/api/data/<int:id>', methods=['PUT'])
def update_data(id):
    for item in data:
        if item['id'] == id:
            item['name'] = request.get_json().get('name')
            return jsonify(item)
    return jsonify({'message': 'Data not found'}), 404

# DELETEリクエストの処理
@app.route('/api/data/<int:id>', methods=['DELETE'])
def delete_data(id):
    for item in data:
        if item['id'] == id:
            data.remove(item)
            return jsonify({'message': 'Data deleted'})
    return jsonify({'message': 'Data not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)