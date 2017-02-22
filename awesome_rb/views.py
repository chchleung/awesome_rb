#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.http import HttpResponse


def index(request):
    return HttpResponse("<p> 世界好 </P>")
