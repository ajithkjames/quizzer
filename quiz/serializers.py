from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name','username', 'email', 'password')

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz

        fields = ['id','author','title','start','end']
        depth = 1

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        depth = 2

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class AttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attempt
        fields = '__all__'

class TestEntriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestEntries
        fields = ('id','attempt','question','answer','is_correct')









