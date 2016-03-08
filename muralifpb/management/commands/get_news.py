# -*- coding: UTF-8 -*-
from django.core.management.base import BaseCommand, CommandError

from muralifpb.models import News

class NewsCommand(BaseCommand):

	def add_arguments(self):
		pass