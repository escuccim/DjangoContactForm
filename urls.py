from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from . import views

app_name = 'contact'

urlpatterns = [
    url(r'^', views.Contact, name='contact'),
]