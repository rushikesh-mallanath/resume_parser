from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.http import HttpResponse
from django.conf import settings

urlpatterns = [
	path('', views.fileupload, name='upload'),
    path('jd/', views.jdview, name ='jdtemp'),
    path('jdinput/', views.jdinput, name="jdinput"),
    path('output/', views.output, name='output')
]