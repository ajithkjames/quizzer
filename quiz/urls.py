from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .apiviews import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'quizes', QuizViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'attempts', AttemptViewSet)
router.register(r'testentries', TestEntriesViewSet)


urlpatterns = [
   url(r'^api/', include(router.urls)),
   url(r'^api/quiz/(?P<pk>[0-9]+)/$', QuestionViewSet.as_view(), name='Questions'),
   url(r'^api/entries/(?P<pk>[0-9]+)/$', EntriesViewSet.as_view(), name='Questions'),
   
   url(r'^student-home/$', views.StudentHome.as_view(), name='student_home'),
   url(r'^(?P<pk>[0-9]+)/$',views.QuizDetailsView.as_view(), name='detail'),
   url(r'^progress/(?P<pk>[0-9]+)/$',views.testprogress.as_view(), name='progress'),
   url(r'^result/(?P<pk>[0-9]+)/$',views.result.as_view(), name='result'),
   url(r'^myresults/$',views.myresults.as_view(), name='myresults'),
   url(r'^teacher-home/$', views.TeacherHome.as_view(), name='teacher_home'),
   url(r'^allattempts/(?P<pk>[0-9]+)/$',views.AllAttempts.as_view(), name='allattempts'),
   url(r'^leader-board/city/(?P<city>[0-9]+)/quiz/(?P<pk>[0-9]+)/$', views.LeaderCity.as_view(), name='leader_city'),
   url(r'^leader-board/school/(?P<school>[0-9]+)//quiz/(?P<pk>[0-9]+)/$', views.LeaderSchool.as_view(), name='leader_school'),
   url(r'^leader-board/$', views.LeaderBoard.as_view(), name='leader_board'),
   url(r'^leader-board/(?P<pk>[0-9]+)/$', views.QuizLeaders.as_view(), name='leaders'),
   url(r'^leader-board/(?P<pk>[0-9]+)/cities/$', views.QuizLeadersCities.as_view(), name='leaderboardcities'),
   url(r'^leader-board/(?P<pk>[0-9]+)/schools/$', views.QuizLeadersSchools.as_view(), name='leaderboardschools'),
   url(r'^create-quiz/$', views.CreateQuiz, name='create-quiz'),
   url(r'^mystudents/$', views.MyStudents.as_view(), name='mystudents'),
   url(r'^students/(?P<pk>[0-9]+)/$',views.StudentDetails.as_view(), name='student'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)