# -*- coding: utf-8 -*-

from django.conf.urls import include,url
from blogs.views import blog_index, blog_list, blog_show, blog_add, blog_update, blog_delete,blog_show_comment

urlpatterns = [
    url(r'^$', blog_index, name='blogindex'),
    url(r'^blog_list/$', blog_list, name='bloglist'),
    url(r'^blog/(?P<id>\w{10,60})/$', blog_show, name='detailblog'),
    url(r'^blog/add/$', blog_add, name='addblog'),
    url(r'^blog/(?P<id>\w{10,60})/update/$', blog_update, name='updateblog'),
    url(r'^blog/(?P<id>\w{10,60})/delete/$', blog_delete, name='deleteblog'),
    url(r'^blog/(?P<id>\w{10,60})/commentshow/$', blog_show_comment, name='showcomment'),
]
