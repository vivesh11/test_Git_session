# app.py

from flask import Flask, jsonify, request

app = Flask(__name__)

# Example in-memory data (for simplicity)
data = {
    1: {"name": "Alice", "age": 30},
    2: {"name": "Bob", "age": 25},
}


@app.route('/')
def hello():
    return "Welcome to the Flask API!"


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(data)


@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = data.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/user', methods=['POST'])
def create_user():
    new_user = request.get_json()
    if 'name' not in new_user or 'age' not in new_user:
        return jsonify({"error": "Bad request, 'name' and 'age' required"}), 400

    user_id = max(data.keys()) + 1
    data[user_id] = new_user
    return jsonify({"id": user_id, **new_user}), 201


if __name__ == '__main__':
    app.run(debug=True, port=8000)
