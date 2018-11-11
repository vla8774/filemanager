from urllib import request

from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    # previous login view
    # url(r'^login/$', views.user_login, name='login'),

    # login / logout urls
    url(r'^login/$', views.CustomLoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'signup/', views.SignUp.as_view(), name='signup'),
    url(r'change/', views.Change.as_view(), name='change'),
]
