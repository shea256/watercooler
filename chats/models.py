from django.db import models
import datetime

class Chat(models.Model):
#	chatTime = models.DateTimeField('chat time')
	session_id = models.AutoField(primary_key = True)

class Interest(models.Model):
	topic = models.CharField(max_length = 200, unique=True)

	def __unicode__(self):
		return self.topic

class User(models.Model):
	chat = models.ForeignKey(Chat)
	email = models.CharField(max_length=200, unique=True)
	facebookId = models.IntegerField()
	interests = models.ManyToManyField(Interest)
	
	def __unicode__(self):
		return self.email


		
# class UserInterestPair(models.Model):
# 	user = models.ForeignKey(User)
# 	interest = models.ForeignKey(Interest)
# 	
# 	def __unicode__(self):
# 		return "(" + self.user.email + "," + self.interest.topic + ")";
		
# class UserChatPair(models.Model):
# 	user = models.ForeignKey(User)
# 	chat = models.ForeignKey(Chat)
# 	
# 	def __unicode__(self):
# 		return "(" + self.user.email + "," + self.chat.chatTime + ")";

