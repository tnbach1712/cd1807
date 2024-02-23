from flask import Flask, jsonify
import logging

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! 1123'
    
@app.route('/app/<polo>')
def app_route(polo):
    logging.info(f"Hello, {polo}")
    return polo


@app.route('/users', methods=['GET'])
def get_users():
    logging.info(f"Get users")
    return jsonify([
        {'id': 546, 'username': 'John'},
        {'id': 894, 'username': 'Mary'},
        {'id': 326, 'username': 'Jane'}
    ])


@app.route('/users', methods=['DELETE'])
def delete_user():
    return jsonify({'result': 'success'})

if __name__ == "__main__":
   app.run()