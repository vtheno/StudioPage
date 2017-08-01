#coding=utf-8
#+Author: Commoners
#+Email: a2550591@gmail.com
#+Date: <2017-07-27 星期四>
#TODO
from app import app
from flask import render_template
#from flask import request,redirect
def readh5file(filename):
    f = open(filename)
    StrBuffer = f.read()
    f.close()
    return StrBuffer
    
@app.route('/')
@app.route('/index')
def index():
    return "Hello Flask!"

    
@app.route('/test')
def test():
    #HtmlBuffer = readh5file('app/templates/index.html') 
    #return """{}""".format(HtmlBuffer)
    return render_template('index.html')
