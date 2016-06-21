# -*- coding: utf-8 -*-
from server.modules.file import File
from server import utils

class file(File):

	adminInfo = {
		"name": u"My Files",
	    "handler": "tree.simple.file",
	    "icon": "icons/modules/my_files.svg"
	}

	def getAvailableRootNodes(self, name):
		if utils.getCurrentUser():
			repo = self.ensureOwnModuleRootNode()
			res = [{"name": _("My Files"), "key": str(repo.key())}]
			return res

		return []

file.jinja2 = True
file.xml = True
file.json = True
