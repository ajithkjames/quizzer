from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name','username', 'email', 'password')

class QuizSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		depth = 1
		model = Quiz
		fields = ('id','title','start','end')

class QuestionSerializer(serializers.Serializer):
    class Meta:
    	depth = 1
        model = Question
        fields = ('quiz','content','choice1','choice2', 'choice3', 'choice4','answer')

     





