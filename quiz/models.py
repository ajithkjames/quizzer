from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import date
from datetime import datetime, timedelta

# Create your models here.
ACCOUNTS_TYPE_CHOICES = (
	(0, 'Student'),
	(1, 'Teacher'),

)

CITY_CHOICES = (
	(0, 'Kochi'),
	(1, 'Kannur'),

)

class ModelManager(models.Manager):
	def get_queryset(self, fetch_all=False):
		return super(ModelManager, self).get_queryset() if fetch_all \
			else super(ModelManager, self).get_queryset().filter(deleted_at__isnull=True)


class DateMixin(models.Model):

	objects = ModelManager()

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	deleted_at = models.DateTimeField(null=True, blank=True)

	class Meta:
		abstract = True

class School(DateMixin):

	name = models.CharField(max_length=1000)
	address= models.CharField(max_length=1000, null=True, blank=True)
	phone = models.CharField(max_length=20, null=True, blank=True)
	city = models.IntegerField(choices=CITY_CHOICES, default=0)
	
	def __str__(self):		 
		return self.name


		
class Profile(DateMixin):
	"""
	All common details for candidates, and teachers
	"""
	user = models.OneToOneField(User)
	account_type = models.IntegerField(choices=ACCOUNTS_TYPE_CHOICES, default=0)
	avatar = models.FileField(null=True, blank=True)
	school = models.ForeignKey(School, null=True, blank=True)
	phone = models.CharField(max_length=20, null=True, blank=True)
	
	def __str__(self):		 
		return self.user.username

class Quiz(DateMixin):

	author = models.ForeignKey(User)
	title = models.CharField(max_length=1000)
	start = models.DateTimeField()
	end = models.DateTimeField()

	def __str__(self):		 
		return self.title

class Question(DateMixin):

	quiz = models.ForeignKey(Quiz)
	content = models.CharField(max_length=1000)

	def __str__(self):		 
		return self.content

class Answer(DateMixin):

	question = models.ForeignKey(Question)
	content = models.CharField(max_length=1000)
	is_correct = models.BooleanField(default=False)

	def __str__(self):		 
		return self.content

class Attempt(DateMixin):

	user = models.ForeignKey(User)
	quiz = models.ForeignKey(Quiz)

	def __str__(self):		 
		return self.quiz.title

class TestEntries(DateMixin):

	attempt = models.ForeignKey(Attempt)
	question = models.ForeignKey(Question)
	answer = models.ForeignKey(Answer)

	def __str__(self):		 
		return self.attempt