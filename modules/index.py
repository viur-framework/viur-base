# -*- coding: utf-8 -*-
from server import exposed
from server.render.jinja2 import defaultRenderer

class index(defaultRenderer):

	@exposed
	def index(self, *args, **kwargs):
		template = self.getEnv().get_template("index.html")
		return template.render(start=True)

index.jinja2 = True
