import flask
from flask import Flask
from flask import render_template
from flask import request
import config_creation as cc
import login_auth as la
import os

SECRET_KEY = os.urandom(100)

#app configs
app = Flask(__name__)
app.debug=True
app.secret_key = SECRET_KEY
app.config['SESSION_TYPE'] = 'filesystem'

# the login page in order to access the app


@app.route('/login')
def login():
    return render_template('login.html', button_auth=la.auth_uri)

@app.route('/oauth2callback')
def callback():
    print(request.url)
    code = flask.request.args.get('code')
    credentials = la.greatExchange(code)
    flask.session['credentials'] = credentials.to_json()
    return flask.redirect(flask.url_for('homepage'))

@app.route('/home')
def dna():
    # import ipdb;ipdb.set_trace()
    if 'credentials' not in flask.session:
        return flask.redirect(flask.url_for('login'))
    credentials = la.credentials.from_json(flask.session['credentials'])
    if credentials.access_token_expired:
        return flask.redirect(flask.url_for('login'))
    # elif:
    #     auth_code = flask.request.args.get('code')
    #     credentials = flow.step2_exchange(auth_code)
    #     flask.session['credentials'] = credentials.to_json()
    #     return flask.redirect(flask.url_for('index'))
    # else:
    #     http_auth = credentials.authorize(httplib2.Http())
    #     drive = discovery.build('drive', 'v2', http_auth)
    #     files = drive.files().list().execute()
    #     return json.dumps(files)

@app.route('/headers')
def headers():
    return "This is where to create custom headers"

@app.route('/main')
def homepage():
    return render_template("main.html", my_nav=["Home", "Configuration", "Headers", "Login"])

@app.route('/conf')
def config_creation_form():
    return render_template('form.html')

@app.route('/result', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        site = request.form['field1']
        header = request.form['field2']
        feed_source = request.form['field3']
        fpath = request.form['field4']
        cc.creation(site, header, feed_source, fpath)
        return render_template('result.html', site=site, header=header, feed_source=feed_source, fpath=fpath)


if __name__ == "__main__":
    app.run()