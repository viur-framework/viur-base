"""
This is the ViUR default module importer.

If any other importing logic is wanted, please switch to manual import calls in this file, and remove
the dynamic code provided below.
"""

import logging
import importlib
import os
import viur

####################################
# Automatic imports are done here! #
####################################

# start of script
_prefix = True  # set prefix if modules are in subfolder. Default: True, set to False if u don't want prefixing

_viur_modules = {}
_current_path = os.path.dirname(os.path.realpath(__file__))

for _root, _dirs, _files in os.walk(_current_path):
    for _module in os.listdir(_root):
        if _module == "__init__.py" or not _module.endswith(".py"):
            continue

        _module = _module[:-3]

        try:

            if _root == _current_path:
                _import = __import__(_module, globals(), locals(), level=1)
                _control = f"modules.{_module}"
            else:
                _folder_name = _root.split("/")

                if _prefix:
                    _import = importlib.import_module(f".{_folder_name[-1]}.{_module}", package="modules")
                    obj_key = f"{_folder_name[-1]}_{_module}"
                    globals()[obj_key] = _import
                    logging.debug(f"Module: {_module} will be imported as {obj_key}")
                else:
                    _import = importlib.import_module(f".{_folder_name[-1]}.{_module}", package="modules")

                _control = f"modules.{_folder_name[-1]}.{_module}"

            for _name in dir(_import):
                if _name.startswith("_"):
                    continue

                _symbol = getattr(_import, _name)
                if getattr(_symbol, "__module__", None) != _control or isinstance(_symbol, viur.core.Module):
                    continue

                _viur_modules[_name.lower()] = _symbol
                logging.debug("Importing %s as %s" % (_symbol, _name.lower()))

        except Exception as e:
            logging.error("Unable to import '%s'" % _module)
            raise e

globals().update(_viur_modules)

# remove private variables
del _viur_modules, _module, _import, _name, _symbol, logging, os, viur, _control, _folder_name, _current_path

#########################################
# Manual imports can also be done here! #
#########################################

# import XYZ as ZYX
