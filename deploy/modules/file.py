from viur.core import i18n, db, current
from viur.core.modules.file import File


class File(File):

    def getAvailableRootNodes(self, *args, **kwargs):
        # Any user who is logged in can see the root-node.
        if current.user.get():
            repository = self.ensureOwnModuleRootNode()

            return [{
                "name": i18n.translate("Files"),
                "key": repository.key
            }]

        return []
