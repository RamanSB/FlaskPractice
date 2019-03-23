#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 18:56:02 2019

@author: RamanSB
"""

from flask import Flask, redirect, url_for
app = Flask(__name__)



#Both examples below bind a function to a URL
@app.route('/hello') #This decorater matches the output of hello_world with the URL  'localhost/'
def hello_world():
    return 'Hello World'
#The above functions decorater is the same as the following:
'''
def hello_world():
    return 'Hello World'
app.add_url_rule('/', 'hello', hello_world)
'''


#Variable rules
@app.route('/bye/<name>')
def bye_name(name):
    return "Bye %s!" % name

@app.route('/admin')
def hello_admin():
    return "Hello Admin"

@app.route('/guest/<guest>')
def hello_guest(guest):
    return "Hello %s as guest." % guest

@app.route('/user/<name>')
def hello_user(name):
    if(name=='admin'):
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))

#if we access localhost/user/admin we will be redirected to the url bounded to the hello_admin function
# localhost/admin.

#if we access localhost/user/abcde, we will be redirected to the url bounded to the hello_guest function
# localhost/guest/abcde



if(__name__=='__main__'):
    app.run(debug=True) #app.run(host, port, debug, options) - All parameters are optional.