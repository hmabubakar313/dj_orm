
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('test/', views.test, name='test'),
    path('test2/', views.test2, name='test2'),
    # path('debug/',include("debug_toolbar.urls")),
]
