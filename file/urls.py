from django.conf.urls import url

from file import views

urlpatterns = [
    url(r'^$', views.post_file, name='post_file'),
    url(r'^subject/(?P<pk>\d+)/$', views.subject_detail, name='subject_detail'),
    url(r'^subject/$', views.subject_all, name='subject_detail'),
   # url(r'^subject/$', views.subject_detail, name='subject_file'),
 #   url(r'^$', views.post_list, name='subject_file'),
]


