from flask import Flask, request
app = Flask(__name__, static_folder='public')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        return 'OKK'
    return 'OKK GET'
if __name__ == '__main__':
    app.run(debug=True)