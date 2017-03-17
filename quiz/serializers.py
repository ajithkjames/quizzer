from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import User,Profile,Quiz,Question,Attempt,TestEntries


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name','username', 'email', 'password')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        depth = 2

class QuizSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(source='author.profile')
    class Meta:
        model = Quiz

        fields = ['id','author','title','start','end','profile']
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









