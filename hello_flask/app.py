
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Team Edge!'

@app.route('/about')
def about():
    return "<h1>About</h1><p>some other content</p>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
