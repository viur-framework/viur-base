#-*- coding: utf-8 -*-
from server.prototypes import List
from server import exposed

class Example(List):

	def listFilter(self, query):
		return query # everyone can see everything!

	@exposed
	def index(self, *args, **kwargs):
		# Return list function as default
		return self.list(*args, **kwargs)
