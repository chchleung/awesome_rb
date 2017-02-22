from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template.context_processors import csrf
from blogs.models import Tag, Author, Blog
from django import forms


# Create your views here.


def blog_list(request):
    blogs = Blog.objects.all()
    ctx = {}
    ctx['blogs'] = blogs
    return render(request, "blog_list.html", ctx)


def blog_show(request, id=''):
    ctx = {}
    try:
        blog = Blog.objects.get(id=id)
        ctx['blog'] = blog
    except Blog.DoesNotExist:
        raise Http404
    return render(request, "blog_show.html", ctx)
