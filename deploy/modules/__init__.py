# This is the ViUR default module importer;
# If any other importing logic is wanted, please switch to manual import calls in this file, and remove
# the dynamic code provided below.

import logging
import os
import viur

####################################
# Automatic imports are done here! #
####################################

# start of script
_viur_modules = {}

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
            if getattr(_symbol, "__module__", None) != f"modules.{_module}" or isinstance(_symbol, viur.core.Module):
                continue

            _viur_modules[_name.lower()] = _symbol
            logging.debug("Importing %s as %s" % (_symbol, _name.lower()))

    except Exception as e:
        logging.error("Unable to import '%s'" % _module)
        raise e

globals().update(_viur_modules)
del _viur_modules, _module, _import, _name, _symbol, logging, os, viur  # remove private variables

#########################################
# Manual imports can also be done here! #
#########################################

# noinspection PyUnresolvedReferences
from viur.core.modules.site import Site as s
