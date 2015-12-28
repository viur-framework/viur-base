# -*- coding: utf-8 -*-

from server.render.jinja2 import default as html_default_renderer


class index(html_default_renderer):
	def index(self, *args, **kwargs):
		template = self.getEnv().get_template("index.html")
		return template.render(start=True)

	index.exposed = True


index.jinja2 = True
