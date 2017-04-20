# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 14:18:52 2017

@author: Aditya
"""
# userSession is the class of the current active user

from time import sleep
from app import app
from flask import render_template, request, redirect, url_for, session, jsonify, make_response
from app import db, models, userSession
from app import classes
import json, datetime
#from app import views, models
userSession = []
@app.route('/')
def home():
	session.clear()
	return render_template('home.html', user=request.args.get('user'))



@app.route('/someFunc', methods=['POST', 'GET'])
def someFunc():
	return render_template('login.html')


"""login & signup"""
@app.route('/login', methods=['GET', 'POST']) #user login
def login():
	error = None
	flag = False
	global userSession
	if request.method == 'POST':
		try:
			uname = request.form['username'].strip()
			pword = request.form['password'].strip()
			users = models.User.query.all()
			for u in users:
				if(uname == u.username) and (pword == u.password):
					flag = True
					session['user'] = str.lower(u.userType)
					if str.lower(u.userType) == 'coach':
						userSession = classes.Coach(u.username, u.age, u.username, u.password)
					elif str.lower(u.userType) == 'player':
						userSession = classes.Player(u.username, u.age, u.username, u.password)
					elif str.lower(u.userType) == 'medical':
						userSession = classes.Medical(u.username, u.age, u.username, u.password)
					elif str.lower(u.userType) == 'management':
						userSession = classes.Management(u.username, u.age, u.username, u.password)
					else:
						userSession = classes.Public(u.username, u.age, u.username, u.password)
					return redirect(url_for(str.lower(u.userType)))
			if not flag:
				error = "Invalid Credentials."
		except Exception:
			pass
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


@app.route('/verifyUserName', methods=['POST'])
def verifyUserName():
	temp = request.form['username']
	users = models.User.query.all()
	flag = False
	for u in users:
		if temp == u.username:
			flag = True
	if flag:
		return "Invalid"
	else:
		return "Valid"





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
	global userSession
	if session['user'] == 'public':
		print (type(userSession))
		uname = userSession.getName()
		if uname in request.cookies:
			resp = make_response(render_template('publicHomePage.html', user=uname, cookie=request.cookies.get(uname)))
			resp.set_cookie(uname, str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M")))
			return resp
		else:
			resp = make_response(render_template('publicHomePage.html', user=uname))
			resp.set_cookie(uname, str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M")))
			return resp
	else:
		return redirect(url_for('home'))


@app.route('/playerHomePage', methods=['GET', 'POST'])
def player():
	global userSession
	if session['user'] == 'player':
		print (type(userSession))
		uname = userSession.getName()
		if uname in request.cookies:
			resp = make_response(render_template('playerHomePage.html', user=uname, cookie=request.cookies.get(uname)))
			resp.set_cookie(uname, str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M")))
			return resp
		else:
			resp = make_response(render_template('playerHomePage.html', user=uname))
			resp.set_cookie(uname, str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M")))
			return resp
	else:
		return redirect(url_for('home'))


@app.route('/medicalHomePage', methods=['GET', 'POST'])
def medical():
	global userSession
	if session['user'] == 'medical':
		print (type(userSession))
		uname = userSession.getName()
		if uname in request.cookies:
			resp = make_response(render_template('medicalHomePage.html', user=uname, cookie=request.cookies.get(uname)))
			resp.set_cookie(uname, str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M")))
			return resp
		else:
			resp = make_response(render_template('medicalHomePage.html', user=uname))
			resp.set_cookie(uname, str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M")))
			return resp
	else:
		return redirect(url_for('home'))



"""Coach functions"""

@app.route('/coachHomePage', methods=['GET', 'POST'])
def coach():
	global userSession
	if session['user'] == 'coach':
		print (type(userSession))
		uname = userSession.getName()
		if uname in request.cookies:
			resp = make_response(render_template('coachHomePage.html', user=uname, cookie=request.cookies.get(uname)))
			resp.set_cookie(uname, str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M")))
			return resp
		else:
			resp = make_response(render_template('coachHomePage.html', user=uname))
			resp.set_cookie(uname, str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M")))
			return resp
	else:
		return redirect(url_for('home'))


@app.route('/viewMatches', methods=['GET', 'POST'])
def viewMatches():
	if session['user'] == 'coach':
		global userSession
		matches = userSession.viewMatches()
		return render_template('viewMatches.html', matches=matches, user=userSession.getName())
	else:
		return redirect(url_for('home'))

"""Management functions"""


@app.route('/managementHomePage', methods=['GET', 'POST'])
def management():
	global userSession
	if session['user'] == 'management':
		print (type(userSession))
		uname = userSession.getName()
		if uname in request.cookies:
			resp = make_response(render_template('managementHomePage.html', user=uname, cookie=request.cookies.get(uname)))
			resp.set_cookie(uname, str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M")))
			return resp
		else:
			resp = make_response(render_template('managementHomePage.html', user=uname))
			resp.set_cookie(uname, str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M")))
			return resp
	else:
		return redirect(url_for('home'))

@app.route('/scheduleMatch', methods=['GET', 'POST'])
def scheduleMatch():
	global userSession
	print(type(userSession))
	if session['user'] == 'management':
		if request.method == 'POST':
			opponent = request.form['opponent']
			#temp = request.form['date'].split('-')
			#date = datetime.date(int(temp[0]),int(temp[1]),int(temp[2]))
			date = request.form['date']
			time = request.form['time']
			userSession.scheduleMatch(opponent,date,time)
		return render_template('scheduleMatch.html', user=userSession.getName())
	else:
		return redirect(url_for('home'))



if __name__ == "__main__":
	app.run(debug=True)
