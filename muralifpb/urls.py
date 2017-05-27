# -*- coding: UTF-8 -*-
from django.conf.urls import url

from .views import (index, account, register, edit_password, edit_user, search,
add_category,
edit_category,
delete_category,
add_post,
edit_post,
delete_post,
add_portal,
edit_portal,
delete_portal,
)

urlpatterns = [#'muralifpb.views', #prefixo

	url(r'^$', index, name='index'),

	url(r'^register/$', register, name='register'),

	url(r'^add_category/$', add_category, name='add_category'),

	url(r'^edit_category/(?P<id>\d+)/$', edit_category, name='edit_category'),

	url(r'^delete_category/(?P<id>\d+)/$', delete_category, name='delete_category'),

	url(r'^add_post/$', add_post, name='add_post'),

	url(r'^edit_post/(?P<id>\d+)/$', edit_post, name='edit_post'),

	url(r'^delete_post/(?P<id>\d+)/$', delete_post, name='delete_post'),

	url(r'^add_portal/$', add_portal, name='add_portal'),

	url(r'^edit_portal/(?P<id>\d+)/$', edit_portal, name='edit_portal'),

	url(r'^edit_user/$', edit_user, name='edit_user'),

	url(r'^account/$', account, name='account'),

	url(r'^search/$', search, name='search'),

	url(r'^edit_password/$', edit_password, name='edit_password'),
]