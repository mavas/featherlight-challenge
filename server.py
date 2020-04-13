import string

from flask import Flask, request, Response, render_template


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
            encoded = caesar(data['Message'], data['Shift'])
            with open("/tmp/featherlight", 'w') as fh:
                fh.write(encoded)
            return Response({'EncodedMessage': encoded}, status=200, mimetype='application/json')
    return Response('', status=500)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('./home.html')


if __name__ == '__main__':
    app.run(port=23456, debug=True)
