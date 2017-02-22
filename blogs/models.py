from django.db import models
import time
import uuid

# Create your models here.


def next_id():
    return '%015d%s000' % (int(time.time()*1000), uuid.uuid4().hex)


class Tag(models.Model):
    """docstring for Tags"""
    tag_name = models.CharField(max_length=20, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag_name


class Author(models.Model):
    """docstring for Author"""
    id = models.CharField(primary_key=True, default=next_id, max_length=200)
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    image = models.CharField(max_length=500, default=None)

    def __str__(self):
        return self.name


class Blog(models.Model):
    """docstring for Blog"""
    id = models.CharField(primary_key=True, default=next_id, max_length=200)
    caption = models.CharField(max_length=50)
    author = models.ForeignKey(Author)
    tags = models.ManyToManyField(Tag, blank=True)
    summary = models.CharField(max_length=500)
    content = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.caption

    class Meta:
        ordering = ['-publish_time']  # set default sort

