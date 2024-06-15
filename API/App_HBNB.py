from flask import Flask, request, jsonify
from Persistence.DataManager import DataManager
from Model.user import User

app = Flask(__name__)
data_manager = DataManager('users.json')

@app.route('/users', methods=['POST'])
def createuser():
    data = request.json

    user = User(
        email=data['email'],
        password=data['password'],
        firstname=data['first_name'],
        last_name=data['last_name']
    )

    DataManager.create(user.to_dict())

    return jsonify({'message': 'User created successfully!', 'user_id': user.user_id}), 201

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = DataManager.read(user_id)
    if user:
        return jsonify(user)
    return jsonify({'message': 'User not found'}), 404

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    if DataManager.update(user_id, data):
        return jsonify({'message': 'User updated successfully!'})
    return jsonify({'message': 'User not found'}), 404

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if DataManager.delete(user_id):
        return jsonify({'message': 'User deleted successfully!'})
    return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
