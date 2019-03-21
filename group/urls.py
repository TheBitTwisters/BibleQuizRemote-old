from django.urls import path
from . import views


app_name = 'group'
urlpatterns = [
    path('<str:group_name>', views.index, name='index'),
]
