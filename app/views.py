# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 14:18:52 2017

@author: Aditya
"""
from time import sleep
from app import app
from flask import render_template, request, redirect, url_for
from app import db, models

#from app import views, models

@app.route('/')
def home():
    return render_template('home.html', user=request.args.get('user'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
    	uname = request.form['username']
    	pword = request.form['password']
    	users = models.User.query.all()
    	for u in users:
        	if((uname == u.username) and (pword == u.password)):
        		return redirect(url_for('home', user=u.username))
        	else:
        		return "Error."
    return render_template('login.html', error=error)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	error = None
	if request.method == 'POST':
		uname=request.form['username']
		pword=request.form['password']
		age=int(request.form['age'])
		flag = False

		users = models.User.query.all()
		for u in users:
			if(uname == u.username):
				flag = True

		if flag:
			error="Username already exists!"
			return render_template('signup.html', error=error)
		else:
			newUser = models.User(username=uname, password=pword, age=age)
			db.session.add(newUser)
			db.session.commit()
			return redirect(url_for('home', user=uname))
	return render_template('signup.html')

if __name__ == "__main__":
    app.run(debug=True)
