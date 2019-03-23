#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 22:07:51 2019

@author: RamanSB
"""

from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)


@app.route('/results/<int:score>')
def results_report(score):
    return render_template('scores.html', marks=score)

if(__name__=='__main__'):
    app.run(debug=True)