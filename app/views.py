from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from django.db.models import Prefetch

def test(request):
    comments = BlogPost.objects.all().prefetch_related('comments')
    query = comments.query
    return render(request, 'templates/index.html', {'comments': comments})


def test2(request):
    user_groups = User_groups.objects.all().select_related('user').select_related('group')
    query = user_groups.query
    return HttpResponse(query)
