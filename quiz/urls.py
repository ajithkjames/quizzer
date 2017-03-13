from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   url(r'^student-home/$', views.StudentHome.as_view(), name='student_home'),
   url(r'^(?P<pk>[0-9]+)/$',views.DetailsView.as_view(), name='detail'),
   url(r'^progress/(?P<pk>[0-9]+)/$',views.testprogress.as_view(), name='progress'),
   url(r'^result/(?P<pk>[0-9]+)/$',views.result.as_view(), name='result'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)