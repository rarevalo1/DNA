from flask import Flask
from flask import render_template
from flask import request
import config_creation as cc
import login_auth as la

#app configs
app = Flask(__name__)
app.debug=True

# the login page in order to access the app


@app.route('/login')
def login():
    return render_template('login.html', button_auth=la.auth_uri)


@app.route('/oauth2callback')
def callback():
    print("wtf!!!")
    print(request.url)
    code = request.url.split('=')[1]
    print(code)
    print(la.greatExchange(code))
    return render_template('oauth2callback.html')


@app.route('/home')
def dna():
    return "This is the front end for DNA."

@app.route('/headers')
def headers():
    return "This is where to create custom headers"

@app.route('/conf')
def config_creation_form():
    return render_template('form.html')

@app.route('/result', methods=['POST', 'GET'])
def create():
    if request.method=='POST':
        site = request.form['field1']
        header = request.form['field2']
        feed_source = request.form['field3']
        fpath = request.form['field4']
        cc.creation(site, header, feed_source, fpath)
        return render_template('result.html', site=site, header=header, feed_source=feed_source, fpath=fpath)

