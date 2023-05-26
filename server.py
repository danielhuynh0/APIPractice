from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return {'content':'Hello, World!'}

@app.route('/get-owner', methods=['GET'])
def get_owner():
    return {'content':'Daniel'}

if __name__ == '__main__':
    app.run()