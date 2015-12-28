# -*- coding: utf-8 -*-
from server.modules.file import File
from server.bones import *
from server import utils


class file(File):
	def getAvailableRootNodes(self, name):
		thisuser = utils.getCurrentUser()
		if thisuser:
			repo = self.ensureOwnModulRootNode()
			res = [{"name": _("gemeinsame Dateien"), "key": str(repo.key())}]
			return res
		return []

	adminInfo = {"name": "Dateien",
	             "handler": "tree.simple.file",
	             "icon": "icons/modules/my_files.svg",
	             "sortIndex": 1
	}


file.jinja2 = True
file.xml = True
file.gherkin = True
file.json = True
