from flask import Flask, render_template

app = Flask(__name__)

messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/create', methods=('GET','POST'))
def create():
    return render_template('create.html')

#if __name__ == "__main__":
#    app.run()



