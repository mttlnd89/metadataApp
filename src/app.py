from flask import Flask, render_template, request
import datetime
from metadataAPI import apiQuery

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html',utc_dt=datetime.datetime.utcnow())


@app.route('/about',methods=['GET'])
def about():
    return render_template('about.html')

#if __name__ == "__main__":
#    app.run()



