# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 14:18:52 2017

@author: Aditya
"""
# userSession is the class of the current active user

from time import sleep
from app import app
from flask import render_template, request, redirect, url_for, sessions
from app import db, models, userSession
from app import classes
#from app import views, models
userSession = []
@app.route('/')
def home():
    return render_template('home.html', user=request.args.get('user'))
"""login & signup"""
@app.route('/login', methods=['GET', 'POST']) #user login
def login():
    error = None
    flag = False
    if request.method == 'POST':
    	uname = request.form['username'].strip()
    	pword = request.form['password'].strip()
    	users = models.User.query.all()
    	for u in users:
    		if(uname == u.username) and (pword == u.password):
    			flag = True
    			return redirect(url_for(str.lower(u.userType)))
    	if not flag:
    		error = "Invalid Credentials."
    return render_template('login.html', error=error)

@app.route('/signup', methods=['GET', 'POST']) #general user signup
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
			newUser = models.User(username=uname, password=pword, age=age, userType="public")
			db.session.add(newUser)
			db.session.commit()
			return redirect(url_for('home', user=uname))
	return render_template('signup.html')


"""admin functions"""
@app.route('/adminLogin', methods=['GET', 'POST']) #admin login
def adminLogin():
	error = None
	if request.method == 'POST':
		uname=request.form['username']
		pword=request.form['password']
		if(uname=='admin' and pword=='admin'):
			global userSession
			userSession = classes.Admin()
			#sessions['currentUser'] = temp
			print (type(userSession))
			return redirect(url_for('adminDashboard'))
		else:
			return render_template('adminLogin.html', error="Invalid ID")
	return render_template('adminLogin.html')

@app.route('/adminDashboard', methods=['GET', 'POST']) #admin homepage
def adminDashboard():
	return render_template('adminDashboard.html')

@app.route('/createNewUserAdmin', methods=['GET', 'POST']) #admin create new user
def createNewUserAdmin():
	global userSession
	print (type(userSession))
	error = None
	if request.method == 'POST':
		uname = request.form['username']
		pword = request.form['password']
		userType = request.form['usertype']
		age=int(request.form['age'])
		print(uname, pword, userType, age)
		userSession.createUser(uname,pword,userType,age)
	return render_template('createNewUserAdmin.html')


"""Home pages for various users"""

@app.route('/publicHomePage', methods=['GET', 'POST'])
def public():
	return render_template('publicHomePage.html')

@app.route('/coachHomePage', methods=['GET', 'POST'])
def coach():
	return render_template('coachHomePage.html')

@app.route('/managementHomePage', methods=['GET', 'POST'])
def management():
	return render_template('managementHomePage.html')

@app.route('/playerHomePage', methods=['GET', 'POST'])
def player():
	return render_template('playerHomePage.html')

@app.route('/medicalHomePage', methods=['GET', 'POST'])
def medical():
	return render_template('medicalHomePage.html')

if __name__ == "__main__":
    app.run(debug=True)
