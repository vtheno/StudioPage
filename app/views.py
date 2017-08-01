#coding=utf-8
#+Author: Commoners
#+Email: a2550591@gmail.com
#+Date: <2017-07-27 星期四>
#TODO
from app import app
#from flask import render_template
#from flask import request,redirect
@app.route('/')
@app.route('/index')
def index():
    return "Hello Flask!"
