# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 22:55:46 2017

@author: Aditya
"""
"""Code for all the users"""
from app import models, db
class User(object):
    def __init__(self, name, age, username, password):
        self.name = name
        self.age = int(age)
        self.username = username
        self.password = password
    
    def getUserName(self):
        return self.username
    
    def getAge(self):
        return self.age
        
    def getName(self):
        return self.name

class Public(User):
    def __init__(self, name, age, username, password):
        User.__init__(self, name, age, username, password)
    
    def bookTickets(someParameters):
        print('lol')
        #code goes here
    def viewPlayerInfo(self):
        temp = models.Player.query.all()
        return temp
    def viewMatches(self):
        temp = models.Match.query.all()
        return temp
        
class Coach(User):
    def __init__(self, name, age, username, password):
        User.__init__(self, name, age, username, password)
        
    def chooseSquad(someParameters):
        print('lol')
        #code goes here
    
    def scheduleTraining(someParameters):
        print('lol')
        #code goes here
        
    def manageContracts(someParameters):
        print('lol')
        #code goes here
    
    def viewMatches(self):
        temp = models.Match.query.all()
        return temp

class Management(User):
    def __init__(self, name, age, username, password):
        User.__init__(self, name, age, username, password)
    
    def manageContracts(someParameters):
        print('lol')
        #code goes here
    
    def scheduleMatch(self, opponent, date, time):
        temp = models.Match(opponent=opponent,date=date,time=time)
        db.session.add(temp)
        db.session.commit()
    
class Player(User):
    def __init__(self, name, age, username, password):
        User.__init__(self, name, age, username, password)
    
    def viewGames(someParameters):
        print('lol')
        #code goes here
    
    def addPlayerInfo(self, name, weight, height, jersey, position, uname):
        temp = models.Player(name=name, weight=int(weight), jersey=int(jersey), position=position, height=int(height), uname=uname)
        db.session.add(temp)
        db.session.commit()
        #code goes here
        
    def viewTrainingSchedule(someParameters):
        print('lol')
        #code goes here
        
    def viewMatches(self):
        temp = models.Match.query.all()
        return temp
        
class Medical(User):
    def __init__(self, name, age, username, password):
        User.__init__(self, name, age, username, password)
    
    def decideDiets(someParameters):
        print('lol')
        #code goes here
    
class Admin(object):
    def __init__(self):
        self.name = 'Admin'
    def createUser(self, username, password, userType, age):
        temp = models.User(username=username, password=password, userType=userType, age=age)
        db.session.add(temp)
        db.session.commit()