# -*- coding: utf-8 -*-
from server import exposed
from server.render.html import default

class index(default):

	@exposed
	def index(self, *args, **kwargs):
		template = self.getEnv().get_template("index.html")
		return template.render(start=True)

index.html = True
