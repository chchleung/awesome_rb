# -*- coding: utf-8 -*-

from django.conf.urls import include,url
from blogs.views import blog_list, blog_show, blog_add, blog_update, blog_delete

urlpatterns = [
    url(r'^blog_list/$', blog_list, name='bloglist'),
    url(r'^blog/(?P<id>\w{10,60})/$', blog_show, name='detailblog'),
    url(r'^blog/add/$', blog_add, name='addblog'),
    url(r'^blog/(?P<id>\w{10,60})/update/$', blog_update, name='updateblog'),
    url(r'^blog/(?P<id>\w{10,60})/delete/$', blog_delete, name='deleteblog'),

]
