#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 22:10:00 2019

@author: RamanSB
"""

from flask import Flask


app = Flask(__name__)


from app import routes