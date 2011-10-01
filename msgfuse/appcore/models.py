# this is an attempt of a model file

from django.db import models
from django import forms

class Messages(models.Model):
	content = models.TextField(default="No one ever inputed text in this msg, or if implmented, this is an error ==")
		# this is the content if the message
	#id = models.AutoField(primary_key=True)
		# do NOT un-comment the above line, this is to show the default automated pk generation
	#user = models.ForeignKey('User')
		# foreign key to link the user whic is to be implmented
		# uncomment if we ever decide to use the users table
		# but the this is a FK, so it has to be not null
	dateCreated = models.DateTimeField(null=True)
		# the date which the msg is created
	hashCode = models.CharField(max_length = 255)
		# the hash code of the msg used for the site, 
		# unqie key to be set late
	hashCodeAdmin = models.CharField(max_length = 255)
	    # the hash code for the user to manage the msg
	initDate = models.DateTimeField(null=True)
		# date which the message is enabled
	endDate = models.DateTimeField(null=True)
		# date which the message will be disabled
	requiredClickNumber = models.IntegerField(null=True, default=0)
		# required clicks to unlock a message
	closingClickNumber = models.IntegerField(null=True, default=-1)
		# amount of click which will disable a message
#	messages = models.ForeignKey('Messages')
		# foreign key to link the message and message conditions
	messageClicks = models.IntegerField(null=True, default=0)
		# the amount of clicks the msg has received.
		
# the following is not used...
# class User(models.Model):
#	userName = models.CharField(primary_key = True, max_length = 255)
		# this is a primary key of users, which is the user name
		# the user name have to be unique, this is to be validated in the code
#	userPass = models.CharField(max_length = 255)
		# this is the password storage of the users which is to be set to private or 
		# a different file later on for privacy/protection reasons
#	regDate = models.DateTimeField(max_length = max)
		# the registeration date of the user
