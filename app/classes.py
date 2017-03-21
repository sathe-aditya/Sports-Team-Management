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
    
    def viewGames(someParameters):
        print('lol')
        #code goes here

class Management(User):
    def __init__(self, name, age, username, password):
        User.__init__(self, name, age, username, password)
    
    def manageContracts(someParameters):
        print('lol')
        #code goes here
    
    def scheduleGames(someParameters):
        print('lol')
        #code goes here
    
class Player(User):
    def __init__(self, name, age, username, password):
        User.__init__(self, name, age, username, password)
    
    def viewGames(someParameters):
        print('lol')
        #code goes here
    
    def viewDiets(someParameters):
        print('lol')
        #code goes here
        
    def viewTrainingSchedule(someParameters):
        print('lol')
        #code goes here
        
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