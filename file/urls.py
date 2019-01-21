from django.conf.urls import url

from file import views

urlpatterns = [
    url(r'^$', views.post_file, name='post_file'),
    url(r'^phone/$', views.post_phone, name='post_phone'),
    url(r'^subject/(?P<fl>.+)/$', views.subject_detail, name='subject_detail'),
    url(r'^subject/$', views.subject_all, name='subject_all'),
    url(r'^file/(?P<url_post>.+)/$', views.file_detail, name='file_detail'),

    url(r'^file/$', views.post_all, name='file_all'),
    #url(r'^file-new/$', views.file_new, name='file_new'),
    url(r'^file-new/$', views.FileNew.as_view(), name='file_new'),
    #url(r'^file-edit/(?P<url_post>.+)/$', views.file_edit, name='file_edit'),
    url(r'^file-edit/(?P<slug>.+)/$', views.FileEdit.as_view(), name='file_edit'),
    url(r'^phone-edit/(?P<pk>.+)/$', views.PhoneEdit.as_view(), name='phone_edit'),
    url(r'^file-delete/(?P<slug>.+)/$', views.FileDelete.as_view(), name='file_delete'),
    url(r'^file-read/(?P<slug>.+)/$', views.FileRead.as_view(), name='file_read'),
    url(r'^subject-new/$', views.SubjectNew.as_view(), name='subject_new'),
    url(r'^subject-edit/(?P<slug>.+)/$', views.SubjectEdit.as_view(), name='subject_edit'),
    url(r'^subject-delete/(?P<slug>.+)/$', views.SubjectDelete.as_view(), name='subject_delete'),
    url(r'^subject-read/(?P<slug>.+)/$', views.SubjectRead.as_view(), name='subject_read'),
   # url(r'^subject/$', views.subject_detail, name='subject_file'),
 #   url(r'^$', views.post_list, name='subject_file'),
]


