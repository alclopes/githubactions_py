from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello'


@app.route('/status')
def status():
    return 'Ok'


if __name__ == '__main__':
    app.run()
