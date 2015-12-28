# -*- coding: utf-8 -*-

import re

from server.render.jinja2 import default as defaultRender
from server import session
from server.config import conf
# RENDERS_JINJA2_IMPORTS_MARKER

class Render(defaultRender):
	def regex_replace(self, s, find, replace):
		return re.sub(find, replace, s)

	def regex_search(self, pattern, string, flags=0):
		return re.search(pattern, string, flags)

	def getEnv(self):
		if "env" not in dir(self):
			super(Render, self).getEnv()
			self.env.globals["regex_replace"] = self.regex_replace
			self.env.globals["regex_search"] = self.regex_search
			self.env.globals["update_session"] = self.update_session
			self.env.globals["get_languages"] = self.get_languages
			self.env.globals["get_language_names"] = self.get_language_names
			self.env.globals["isinstance"] = self.isinstance
			# RENDERS_JINJA2_ENV_MARKER
		return self.env

	def update_session(self, new_dict):
		"""Updates the current session key,values seen by jinja templates.

		Use this method if you have to update more than one session values per jinja template.
		:rtype : None
		:param new_dict:
		:type new_dict: dict
		"""

		current = session.current
		if not current.get("JinjaSpace"):
			current["JinjaSpace"] = new_dict
		else:
			jinja_space = current.get("JinjaSpace")
			jinja_space.update(new_dict)
		current.markChanged()

	def get_languages(self):
		return conf["provided_languages"]

	def get_language_names(self):
		return conf["language_names"]

	def isinstance(self, obj, _type):
		return isinstance(obj, _type)

		# RENDERS_JINJA2_METHOD_MARKER
