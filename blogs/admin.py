# -*- coding:utf-8 -*-

from django.contrib import admin
from blogs.models import Author, Blog, Tag


# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    """docstring for AuthorAdmin"""
    list_display = ('name', 'email', 'website')
    search_fields = ('name',)


class BlogAdmin(admin.ModelAdmin):
    """docstring for BlogAdmin"""
    list_display = ('caption', 'author', 'publish_time', 'updated_time')
    list_filter = ('publish_time',)
    date_hierarchy = 'publish_time'
    ordering = ('-publish_time',)
    filter_horizontal = ('tags',)
    fieldsets = (
        ['Main', {
            'fields': ('caption', 'author', 'summary', 'content'),
        }],
        ['Advance', {
            'classes': ('collapse',),
            'fields': ('tags', 'id'),
        }]
    )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)
