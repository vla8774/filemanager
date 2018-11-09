from django.conf.urls import url

from file import views

urlpatterns = [
    url(r'^$', views.post_file, name='post_file'),
    url(r'^subject/(?P<fl>.+)/$', views.subject_detail, name='subject_detail'),
    url(r'^subject/$', views.subject_all, name='subject_all'),
    url(r'^file/(?P<url_post>.+)/$', views.file_detail, name='file_detail'),

    url(r'^file/$', views.post_all, name='file_all'),
    url(r'^file-new/$', views.file_new, name='file_new'),
    #url(r'^file-new/$', views.FileNew.as_view(), name='file_new'),
    url(r'^file-edit/(?P<url_post>.+)/$', views.file_edit, name='file_edit'),
   # url(r'^subject/$', views.subject_detail, name='subject_file'),
 #   url(r'^$', views.post_list, name='subject_file'),
]


