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

	adminInfo = {
		"name": u"My Files",
	    "handler": "tree.simple.file",
	    "icon": "icons/modules/my_files.svg"
	}

file.jinja2 = True
file.xml = True
file.json = True
