from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^$', views.ask_question, name='ask_question'),
    url('ask_question/$', views.ask_question, name = 'ask_question'),
    url('create/$', views.product_create_view, name = 'product_create_view'),
    #url('qa/login', views.login, name = 'login'),
]
