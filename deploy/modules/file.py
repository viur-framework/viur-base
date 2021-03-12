import datetime
from typing import Dict, List

from viur.core import db, utils
from viur.core.modules.file import File as _File


class File(_File):

	def getAvailableRootNodes(self, *args, **kwargs) -> List[Dict]:
		if utils.getCurrentUser():
			repo: db.Entity = self.ensureOwnModuleRootNode()

			res = [{"name": "Files", "key": repo.key}]
			return res

		return []

	def ensureOwnModuleRootNode(self) -> db.Entity:
		"""
		Ensures, that general root-node for the current module exists.
		If no root-node exists yet, it will be created.

		:returns: The entity of the root-node.
		"""
		key = "rep_module_repo"
		kindName = self.viewSkel("node").kindName
		return db.GetOrInsert(db.Key(kindName, key), creationdate=datetime.datetime.now(), rootNode=1)
