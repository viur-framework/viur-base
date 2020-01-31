# -*- coding: utf-8 -*-
from viur.core.modules.file import File

class file(File):

	def getAvailableRootNodes(self, *args, **kwargs):
		if utils.getCurrentUser():
			repo = self.ensureOwnModuleRootNode()

			res = [{"name": "Files", "key": repo.key.id_or_name}]
			return res

		return []
