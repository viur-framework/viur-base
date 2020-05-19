#-*- coding: utf-8 -*-
from viur.core.prototypes import List
from viur.core import exposed

class vicolor(List):

	def listFilter(self, query):
		return query # everyone can see everything!

	@exposed
	def index(self, *args, **kwargs):
		# Return list function as default
		return self.list(*args, **kwargs)
