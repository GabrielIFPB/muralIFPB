# -*- coding: UTF-8 -*-
from django.core.management.base import BaseCommand, CommandError

import feedparser

from muralifpb.models import News

class Command(BaseCommand):
	#BeautifulSoup
	#requests

	help = 'my test command!'

	def add_arguments(self, parser):

		parser.add_argument('link', nargs='+', type=str)
		pass

	def handle(self, *args, **options):
		if options['link'] is not None:
			for link in options['link']
				News.creating_news(link=link)
		else:
			raise CommandError(u'O link não pode se None!')
		pass