from flask import Flask, render_template

app = Flask(__name__)

app.route('/index')
def myFun():
    return render_template('index.html')

app.run()