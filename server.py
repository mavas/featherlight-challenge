from flask import Flask
app = Flask(__name__)


@app.route('/api/encode/', methods=['POST'])
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(port=23456, debug=True)
