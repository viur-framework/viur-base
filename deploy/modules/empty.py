from viur.core.prototypes import List


class Empty(List):
    listTemplate = "empty_list"

    def listFilter(self, query):
        return query  # This content is public!


Empty.html = True  # enable for HTML-rendering
Empty.json = True  # enable for JSON-rendering
