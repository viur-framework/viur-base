# -*- coding: utf-8 -*-
import datetime
from viur.core.modules.file import File
from viur.core import utils, db
from viur.core.prototypes.uniformtree import TreeType


class file(File):

	def getAvailableRootNodes(self, *args, **kwargs):
		if utils.getCurrentUser():
			repo = self.ensureOwnModuleRootNode()

			res = [{"name": "Files", "key": repo.key}]
			return res

		return []

	def ensureOwnModuleRootNode(self):
		"""
		Ensures, that general root-node for the current module exists.
		If no root-node exists yet, it will be created.

		:returns: The entity of the root-node.
		:rtype: :class:`server.db.Entity`
		"""
		key = "rep_module_repo"
		kindName = self.viewSkel(TreeType.Node).kindName
		return db.GetOrInsert(db.Key(kindName, key), creationdate=datetime.datetime.now(), rootNode=1)
