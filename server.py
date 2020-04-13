from flask import Flask, request


app = Flask(__name__)


@app.route('/api/encode/', methods=['POST'])
def hello_world():
    data = request.data
    print(data)
    print(request.args)
    print(request.json)
    #print(dir(request))
    #rval = {'EncodedMessage': rval}
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(port=23456, debug=True)
