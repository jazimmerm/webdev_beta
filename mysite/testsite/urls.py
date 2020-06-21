from django.urls import path, include
from . import views

app_name = 'testsite'

urlpatterns = [path('', views.index, name = 'test'),
               path('testlink/', views.link, name = 'link'),
               ]