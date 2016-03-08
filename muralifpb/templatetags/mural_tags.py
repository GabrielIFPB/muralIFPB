# -*- coding: UTF-8 -*-
from django import template
from django.contrib.auth.models import User

register = template.Library()

from muralifpb.models import News
from muralifpb.models import Post

@register.inclusion_tag('show_news.html')
def show_news():
	news = News.objects.select_related().filter(published=True)
	return { 'news': news }

@register.inclusion_tag('show_posts.html')
def show_posts():
	posts = Post.objects.select_related().filter(published=True)
	return { 'posts': posts }