from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello'


@app.route('/Ok')
def status():
    return 'ok'


if __name__ == '__main__':
    app.run()
