# -*- coding: utf-8 -*-

from django.conf.urls import include,url
from blogs.views import blog_list, blog_show

urlpatterns = [
    url(r'^blog_list/$', blog_list),
    url(r'^blog/(?P<id>\w+)/$', blog_show, name='detailblog'),
]
