import string

from flask import Flask, request


app = Flask(__name__)


def caesar(plaintext, shift):
    """https://stackoverflow.com/questions/8886947/caesar-cipher-function-in-python"""
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)


@app.route('/api/encode/', methods=['POST'])
def hello_world():
    if request.is_json:
        data = request.json
        if 'Shift' in data and 'Message' in data:
            return caesar(data['Message'], data['Shift'])
    #rval = {'EncodedMessage': rval}
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(port=23456, debug=True)
