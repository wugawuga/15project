from flask import Flask, render_template, jsonify, request, send_file

app = Flask(__name__)

from pymongo import MongoClient

#중요 별표 client = MongoClient('mongodb://test:test@localhost', 27017) 별표
client = MongoClient('localhost', 27017)

db = client.dbpractice


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('project.html')

# @app.route('/static')
# def kkk_mp3():
#     return send_file('kkk.mp3', attachment_filename='kkk.mp3')

@app.route('/login')
def index_html():
    return render_template('login.html')

@app.route('/join')
def index1_html():
    return render_template('join.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)