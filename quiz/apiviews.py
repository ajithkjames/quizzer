from django.contrib.auth.models import User, Group
from datetime import datetime
from rest_framework import viewsets,generics
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from quiz.models import User,Quiz,Profile,Attempt,TestEntries,Question
from quiz.serializers import UserSerializer,QuizSerializer,ProfileSerializer,QuestionSerializer,TestEntriesSerializer,AttemptSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class QuizViewSet(viewsets.ModelViewSet):

    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class ActiveQuizViewSet(viewsets.ModelViewSet):

    queryset = Quiz.objects.filter(start__lte=datetime.now(),end__gte=datetime.now())
    serializer_class = QuizSerializer

class ProfileViewSet(viewsets.ModelViewSet):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class QuestionViewSet(generics.ListAPIView):

    serializer_class = QuestionSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Question.objects.filter(quiz=pk)


class AttemptViewSet(viewsets.ModelViewSet):

    queryset = Attempt.objects.all()
    serializer_class = AttemptSerializer

class TestEntriesViewSet(viewsets.ModelViewSet):

    queryset = TestEntries.objects.all()
    serializer_class = TestEntriesSerializer

class EntriesViewSet(APIView):

    def get(self, request,pk, format=None):
        pk = self.kwargs['pk']
        entries = TestEntries.objects.filter(attempt=pk)
        serializer = TestEntriesSerializer(entries, many=True)
        return Response(serializer.data)

    def post(self, request,pk, format=None):
        serializer = TestEntriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)