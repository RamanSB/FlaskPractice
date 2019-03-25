#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 22:20:52 2019

@author: RamanSB
"""

from app import app #from the app package import the app variable (the flask instance)


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"