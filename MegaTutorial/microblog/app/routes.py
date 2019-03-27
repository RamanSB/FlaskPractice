#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 22:20:52 2019

@author: RamanSB
"""

from flask import render_template, flash, redirect
from app import app #from the app package import the app variable (the flask instance)
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Galeilo Galeilili'},
            'body': 'Eureka, the weight of the gold crown is equal to the fluid displaced!'
        }
    ]
    
    return render_template('index.html', title='Home', user=user, posts=posts)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if(form.validate_on_submit()):
        flash('Login requested for user {}, remeber_me={}'.format(
                form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)