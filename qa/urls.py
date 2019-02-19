from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.index, name='index'),
    #url('qa/login', views.login, name = 'login'),
]
