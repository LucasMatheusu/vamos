from flask import Flask

app = Flask(__name__, static_folder='static')

if __name__ == '__name__':
    app.run(debug=True)