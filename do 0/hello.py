from flask import Flask

app = Flask(__name__)
@app.route('/hello')
@app.route("/hello/<nome>")
def hello(nome=''):
    return '<h1>hello {} </h1>'.format(nome)

@app.route('/blog/')
@app.route('/blog/<int:postID>')
def blog(postID=-1):
    if postID >= 0:
        return 'Blog info {}'.format(postID)
    else:
        return 'blog todo'

@app.route('/blog/<float:postID>')
def blog2(postID=-1):
    if postID >= 0:
        return 'Blog float {}'.format(postID)
    else:
        return 'blog float todo'


if __name__ == "__main__":
    app.run(debug=True, port='3000')
