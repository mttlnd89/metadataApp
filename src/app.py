from flask import Flask, render_template, request, redirect, url_for
import datetime
from metadataAPI import apiQuery

app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def index():
    if request.method == 'POST':
        databaseSel = request.form['db']
        _wbList = apiQuery.workbookQuery(databaseSel)
        return _wbList
    elif request.method == 'GET':
        _dbList = apiQuery.databaseQuery()
        return render_template('index.html',dbList = _dbList)
    
@app.route('/table', methods=['GET'])
def table(database):
    return database


@app.route('/about',methods=['GET'])
def about():
    return render_template('about.html')

#if __name__ == "__main__":
#    app.run()



