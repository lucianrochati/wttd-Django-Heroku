# coding: utf-8
__author__ = 'lucianrocha'
from django.conf.urls import patterns,include,url

urlpatterns = patterns('eventex.core.views',
                       url(r'^$','home', name='home'))