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
	url(r'^login/$', 'django.contrib.auth.views.login', {'template_name' : 'login.html'}, name='login'),
	url(r'^exit/$', 'django.contrib.auth.views.logout', {'template_name' : 'index.html'}, name='index'),
	url(r'^register/$', 'muralifpb.views.register', name='register'),
	url(r'^add_category/$', 'muralifpb.views.add_category', name='add_category'),
	url(r'^edit_category/(?P<id>\d+)/$', 'muralifpb.views.edit_category', name='edit_category'),
	url(r'^delete_category/(?P<id>\d+)/$', 'muralifpb.views.delete_category', name='delete_category'),
	url(r'^add_post/$', 'muralifpb.views.add_post', name='add_post'),
	url(r'^edit_post/(?P<id>\d+)/$', 'muralifpb.views.edit_post', name='edit_post'),
	url(r'^delete_post/(?P<id>\d+)/$', 'muralifpb.views.delete_post', name='delete_post'),
	url(r'^add_portal/$', 'muralifpb.views.add_portal', name='add_portal'),
	url(r'^edit_portal/(?P<id>\d+)/$', 'muralifpb.views.edit_portal', name='edit_portal'),
	url(r'^edit_user/$', 'muralifpb.views.edit_user', name='edit_user'),
	url(r'^account/$', 'muralifpb.views.account', name='account'),
	url(r'^search/$', 'muralifpb.views.search', name='search'),
]
