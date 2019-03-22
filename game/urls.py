from django.urls import path
from . import views


app_name = 'game'
urlpatterns = [
    path('', views.index, name='index'),
    path('monitor', views.monitor, name='monitor'),
    path('submit', views.submit, name='submit'),
    path('<str:group_name>', views.index, name='group'),
]
