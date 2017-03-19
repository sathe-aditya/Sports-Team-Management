# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 14:18:52 2017

@author: Aditya
"""

from flask import Flask, render_template, redirect, url_for, request
import classes

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

if __name__ == "__main__":
    app.run(debug=True)