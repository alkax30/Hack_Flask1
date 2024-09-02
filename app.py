from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


# Hack 1
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'payload': 'success'})


# Hack 2
@app.route('/user', methods=['POST'])
def create_user():
    return jsonify({'payload': 'success'})


# Hack 3
@app.route('/user', methods=['DELETE'])
def delete_user():
    return jsonify({'payload': 'success'})


# Hack 4
@app.route('/user', methods=['PUT'])
def update_user():
    return jsonify({'payload': 'success', 'error': False})


# Hack 5
@app.route('/api/v1/users', methods=['GET'])
def get_api_users():
    return jsonify({'payload': []})


# Hack 6
@app.route('/api/v1/user', methods=['POST'])
def post_api_user():
    email = request.args.get('email')
    name = request.args.get('name')
    response = {
        'payload': {
            'email': email,
            'name': name
        }
    }
    return jsonify(response)


# Hack 7
@app.route('/api/v1/user/add', methods=['POST'])
def add_user():
    email = request.form.get('email')
    name = request.form.get('name')
    id = request.form.get('id')
    response = {
        'payload': {
            'email': email,
            'name': name,
            'id': id
        }
    }
    return jsonify(response)


# Hack 8:
@app.route('/api/v1/user/create', methods=['POST'])
def create_user2():
    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    id = data.get('id')
    response = {
        'payload': {
            'email': email,
            'name': name,
            'id': id
        }
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)