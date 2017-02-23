from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template.context_processors import csrf
from blogs.models import Tag, Author, Blog
from django import forms
from blogs.form import BlogForm, TagForm
from django.template import RequestContext


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


def blog_filter(request, id=''):
    tags = Tag.objects.all()
    tag = Tag.objects.get(id=id)
    blogs = tag.blog_set.all()
    ctx = {}
    ctx['blogs'] = blogs
    ctx['tag'] = tag
    ctx['tags'] = tags
    return render(request, 'blog_filter.html', ctx)


def blog_add(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        tag = TagForm(request.POST)
        if form.is_valid() and tag.is_valid():
            cd = form.cleaned_data
            cdtag = tag.cleaned_data
            tagname = cdtag['tag_name']
            for taglist in tagname.split():  # 将得到的tag字符串用空格分割开 并删除多余空格
                Tag.objects.get_or_create(tag_name=taglist.strip())  # get_or_create表示首先获取tag_name 如果存在就不操作，不存在就创建
            title = cd['caption']
            author = Author.objects.order_by('id')[0]
            content = cd['content']
            blog = Blog(caption=title, author=author, content=content)
            blog.save()
            for taglist in tagname.split():
                blog.tags.add(Tag.objects.get(tag_name=taglist.strip()))
                blog.save()
            id = Blog.objects.order_by('-publish_time')[0].id
            return HttpResponseRedirect('/blogs/blog/%s' % id)
    else:
        form = BlogForm
        tag = TagForm(initial={'tag_name': ''})
        ctx = {}
        ctx.update(csrf(request))
        ctx['form'] = form
        ctx['tag'] = tag
        return render(request, 'blog_add.html', ctx)


def blog_update(request, id=""):
    id = id
    if request.method == 'POST':
        form = BlogForm(request.POST)
        tag = TagForm(request.POST)
        if form.is_valid() and tag.is_valid():
            cd = form.cleaned_data
            cdtag = tag.cleaned_data
            new_tagname = cdtag['tag_name']  # 用空格分开的tag
            new_tagnamelist = new_tagname.split()  # 各个tag组成数组
            for taglist in new_tagnamelist:
                Tag.objects.get_or_create(tag_name=taglist.strip())
            title = cd['caption']
            content = cd['content']
            blog = Blog.objects.get(id=id)
            if blog:
                blog.caption = title
                blog.content = content
                blog.save()
                for taglist in new_tagnamelist:
                    blog.tags.add(Tag.objects.get(tag_name=taglist.strip()))
                    blog.save()
                all_tags = blog.tags.all()
                for tagname in all_tags:
                    if tagname.tag_name not in new_tagnamelist:
                        notag = blog.tags.get(tag_name=tagname)
                        blog.tags.remove(notag)
            else:
                blog = Blog(caption=blog.caption, content=blog.content)
                blog.save()
            return HttpResponseRedirect('/blogs/blog/%s' % id)
    else:
        try:
            blog = Blog.objects.get(id=id)
        except Exception:
            raise Http404
        form = BlogForm(initial={'caption': blog.caption, 'content': blog.content}, auto_id=False)
        tags = blog.tags.all()
        if tags:
            taginit = ''
            for x in tags:
                taginit += str(x) + ' '
            tag = TagForm(initial={'tag_name': taginit})
        else:
            tag = TagForm()
        ctx={}
        ctx['blog'] = blog
        ctx['form'] = form
        ctx['tag'] = tag
        ctx['id'] = id
        return render(request, 'blog_add.html', ctx)


def blog_delete(request, id=""):
    try:
        blog = Blog.objects.get(id=id)
    except Exception:
        raise Http404
    if blog:
        blog.delete()
        return HttpResponseRedirect("/blogs/blog_list/")
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {"blogs": blogs})