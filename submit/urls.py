from django.urls import path
from . import views


app_name = 'submit'
urlpatterns = [
    path('<str:group_name>', views.index, name='index'),
]
