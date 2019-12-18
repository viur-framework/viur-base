# -*- coding: utf-8 -*-
#
# This is the ViUR default module importer;
# If any other importing logic is wanted, please switch to manual import calls in this file, and remove
# the dynamic code provided below.
#

import os, logging
import viur.core.prototypes.basic

_viurModules = {}

for _module in os.listdir(os.path.dirname(__file__)):

	if _module == "__init__.py" or not _module.endswith(".py"):
		continue

	_module = _module[:-3]

	try:
		_import = __import__(_module, globals(), locals(), level=1)

		for _name in dir(_import):
			if _name.startswith("_"):
				continue

			_symbol = getattr(_import, _name)
			if (getattr(_symbol, "__module__", None) != "modules.%s" % _module
				or isinstance(_symbol, viur.core.prototypes.basic.BasicApplication)):
				continue

			_viurModules[_name.lower()] = _symbol
			logging.debug("Importing %s as %s" % (_symbol, _name.lower()))

	except:
		logging.error("Unable to import '%s'" % _module)
		raise

globals().update(_viurModules)
del _viurModules, _module, _import, _name, _symbol, os, logging, viur.core.prototypes.basic

#
# Manual imports can also be done here!
#

from viur.core.modules.site import Site as s
