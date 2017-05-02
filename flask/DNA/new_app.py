from flask import Flask
from flask import render_template
from flask import send_from_directory
from flask import url_for
from flask import request
import importlib.util

spec = importlib.util.spec_from_file_location("config_creation", '/Users/rarevalo/Developer/Python/config_creation.py')
cc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cc)

app = Flask(__name__)
app.debug=True

@app.route('/')
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