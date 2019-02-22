from .views import SignUpView
from .views import HomePageView
from django.conf.urls import url,include

urlpatterns = [
    url('homes/$', HomePageView.as_view(), name = 'home'),
    url('homes/register/$',SignUpView.as_view(), name = 'signup' ),
]
