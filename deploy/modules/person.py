#-*- coding: utf-8 -*-
from server.prototypes import List

class Person(List):
	viewTemplate = "person_view" # Name of the template to view one entry
	listTemplate = "person_list" # Name of the template to list entries

	def listFilter(self, query):
		return query # everyone can see everything!
