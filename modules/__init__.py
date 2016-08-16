# -*- coding: utf-8 -*-
#
# This is the ViUR default module importer;
# If any other importing logic is wanted, please switch to manual import calls in this file, and remove
# the dynamic code provided below.
#

import os, logging

viurModules = {}

for viurModule in os.listdir(os.path.dirname(__file__)):

	if viurModule == "__init__.py" or not viurModule.endswith(".py"):
		continue

	viurModule = viurModule[:-3]

	try:
		_mod = __import__(viurModule, globals(), locals(), [viurModule])
		viurModules[viurModule] = getattr(_mod, viurModule)

	except (ImportError, AttributeError):
		try:
			_mod = __import__(viurModule, globals(), locals(), [viurModule[0].upper() + viurModule[1:]])
			viurModules[viurModule] = getattr(_mod, viurModule[0].upper() + viurModule[1:])

		except (ImportError, AttributeError):
			logging.error("Unable to import module %s" % viurModule)

		except:
			raise

	except:
		raise

globals().update(viurModules)
del viurModule, viurModules
