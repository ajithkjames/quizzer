from django.contrib.auth.models import User, Group
from rest_framework import viewsets,generics
from rest_framework import generics
from .serializers import *
from .models import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class QuizViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuestionViewSet(generics.ListAPIView):

    serializer_class = QuestionSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Question.objects.filter(quiz=pk)