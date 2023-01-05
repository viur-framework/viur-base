from viur.core.render import html


@html.utils.jinjaGlobalFilter
def isList(render, val):
    return isinstance(val, list)


@html.utils.jinjaGlobalFilter
def isDict(render, val):
    return isinstance(val, dict)
