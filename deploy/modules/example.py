from viur.core.prototypes import List


class Example(List):
    listTemplate = "example_list"

    def listFilter(self, query):
        return query  # This content is public!


Example.html = True  # enable for HTML-rendering
Example.json = True  # enable for JSON-rendering
