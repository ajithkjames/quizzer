from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import date
from datetime import datetime, timedelta
from django.core.urlresolvers import reverse


ACCOUNTS_TYPE_CHOICES = (
	(0, 'Student'),
	(1, 'Teacher'),

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

class City(DateMixin):

	name = models.CharField(max_length=1000)
	
	
	def __str__(self):		 
		return self.name


class Standard(DateMixin):

	name = models.CharField(max_length=1000)
	
	def __str__(self):		 
		return self.name


class School(DateMixin):

	name = models.CharField(max_length=1000)
	address= models.CharField(max_length=1000, null=True, blank=True)
	phone = models.CharField(max_length=20, null=True, blank=True)
	city = models.ForeignKey(City, null=True, blank=True)
	classes= models.ManyToManyField(Standard)

	def __str__(self):		 
		return self.name


class Profile(DateMixin):
	"""
	All common details for students, and teachers
	"""
	user = models.OneToOneField(User)
	account_type = models.IntegerField(choices=ACCOUNTS_TYPE_CHOICES, default=0)
	avatar = models.FileField(null=True, blank=True)
	school = models.ForeignKey(School, null=True, blank=True)
	standard = models.ForeignKey(Standard, null=True, blank=True)
	phone = models.CharField(max_length=20, null=True, blank=True)

	def get_absolute_url(self):
		return reverse('profile')

	def __str__(self):		 
		return self.user.username

class Quiz(DateMixin):

	author = models.ForeignKey(User)
	title = models.CharField(max_length=1000,null=True, blank=True)
	start = models.DateField(null=True, blank=True)
	end = models.DateField(null=True, blank=True)

	def questions(self):
		return Question.objects.filter(quiz=self)

	def get_absolute_url(self):
		return reverse('detail', kwargs={ 'pk': self.pk })

	def __str__(self):		 
		return self.title

class Question(DateMixin):

	quiz = models.ForeignKey(Quiz)
	content = models.CharField(max_length=1000)
	choice1 = models.CharField(max_length=1000,null=True, blank=True)
	choice2 = models.CharField(max_length=1000,null=True, blank=True)
	choice3= models.CharField(max_length=1000,null=True, blank=True)
	choice4 = models.CharField(max_length=1000,null=True, blank=True)
	answer = models.CharField(max_length=1000,null=True, blank=True)


	def __str__(self):		 
		return self.content

class Choice(DateMixin):

	question = models.ForeignKey(Question)
	content = models.CharField(max_length=1000)
	is_correct = models.BooleanField(default=False)

	def __str__(self):		 
		return self.content

class Attempt(DateMixin):

	user = models.ForeignKey(User)
	quiz = models.ForeignKey(Quiz)

	@property
	def marks(self):
		entries=TestEntries.objects.filter(attempt=self)
		mark=0
		for entry in entries:
			if entry.is_correct==True:
				mark+=1
		entries=self.testentries_set.all()
		return mark

	class Meta:
		unique_together = ["user", "quiz"]

	def __str__(self):		 
		return self.quiz.title

class TestEntries(DateMixin):

	attempt = models.ForeignKey(Attempt)
	question = models.ForeignKey(Question)
	answer = models.CharField(max_length=1000,null=True, blank=True)
	is_correct = models.BooleanField(default=False)

	class Meta:
		unique_together = ["attempt", "question"]

	def __str__(self):		 
		return self.attempt.quiz.title