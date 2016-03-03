# -*- coding: UTF-8 -*-
"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Add an import:  from blog import urls as blog_urls
	2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'muralifpb.views.index', name='index'),
	url(r'^login/$', 'django.contrib.auth.views.login', {'template_name' : 'login.html'}),
	url(r'^exit/$', 'django.contrib.auth.views.logout', name='index'),
	url(r'^settings/$', 'muralifpb.views.settings', name='settings'),
	url(r'^register/$', 'muralifpb.views.register', name='register'),
	#url(r'^edit/$', 'muralifpb.views.search', name='search'),
	#url(r'^edit/(?P<id>\d+)/$', 'muralifpb.views.edit', name='edit_id'),
	url(r'^addcategory/$', 'muralifpb.views.add_category', name='addcategory'),
	url(r'^addpost/$', 'muralifpb.views.add_post', name='addpost'),
	url(r'^addportal/$', 'muralifpb.views.add_portal', name='addportal'),
]
