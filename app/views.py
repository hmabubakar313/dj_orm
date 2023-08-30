from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from django.db.models import Prefetch

def test(request):
    comments = BlogPost.objects.all().prefetch_related('comments')
    # return query set on the page
    return HttpResponse('test')
