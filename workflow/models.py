from django.db import models
from django.contrib.auth.models import User
from mainsite.models import Article,Editor,Maker,Section,Photo
from django.utils import timezone
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User)
	POSITIONS_CHOICES= (
		('ChiefEditor','Chief Editor'),
		('CopyEditor','Copy Editor'),
		)
	position = models.CharField(choices=POSITIONS_CHOICES,max_length=50,default='Editor')
	def is_author():
		return self.user.author != None
	def is_photographer():
		return self.user.photographer != None
	def is_editor():
		return self.editor != None
	def display_name(self):
		return self.user.first_name+" "+self.user.last_name

class WArticle(models.Model):
	date = models.DateTimeField(default = timezone.now)
	article = models.OneToOneField(Article)
	status = models.TextField()
	locker = models.ForeignKey(User,blank=True)
	def locked(self):
		return self.locker != None
	def __str__(self):
		return self.article.title

class Review(models.Model):
	date = models.DateTimeField(default = timezone.now)
	article = models.ForeignKey(Article)
	reviewer = models.CharField(max_length=50)
	comment = models.TextField(blank=True)

class Revision(models.Model):
	date = models.DateTimeField(default = timezone.now)
	article = models.ForeignKey(Article)
	editor = models.ForeignKey(Editor)
	body = models.TextField()

class Assignment(models.Model):
	sender = models.ForeignKey(Editor)
	receiver = models.ForeignKey(Maker,default=None)
	title = models.CharField(max_length=200)
	content = models.TextField()
	section = models.ForeignKey(Section)
	created_date = models.DateTimeField(default = timezone.now)
	due_date = models.DateTimeField()

class Article_Assignment(Assignment):
	article = models.ForeignKey(Article,default=None)
	def is_article(self):
		return True
	def finished(self):
		self.article != None

class Photo_assignment(Assignment):
	photo = models.ForeignKey(Photo,default=None)
	def finished(self):
		self.article != None
	def is_article(self):
		return False







