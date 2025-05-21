# aula 4 contrução de URL
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/admin")
def admin():
    return "<h1>admin, pivas</h1>"
@app.route("/guest/<guest>")

def guest(guest):
    return '<p>ola guest  se louco <b>%s</b></p>' % guest
@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest', guest=name))
if __name__ == '__main__':
    app.run(debug=True)