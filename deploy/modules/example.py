from viur.core.prototypes import List


class Example(List):
	listTemplate = "example_list"

	def listFilter(self, query):
		return query  # everyone can see everything!
