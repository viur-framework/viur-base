"""
This is the ViUR default module importer.

If any other importing logic is wanted, please switch to manual import calls in this file, and remove
the dynamic code provided below.
"""

####################################
# Automatic imports are done here! #
####################################

import logging
import types
import viur
from pathlib import Path

_viur_modules = {}

BLACKLIST = []  # filenames that should be blacklisted for the import


def _import_modules(_path, _prefix=""):
    for _module in Path(_path).iterdir():
        _module_name = _module.name

        if _module.is_dir():
            _import_modules(_module, f"{_prefix}{_module_name}.")
            continue

        elif _module_name.startswith("_") or not _module_name.endswith(".py"):
            continue

        _module_name = _prefix + _module_name[:-3]

        try:
            _import = __import__(_module_name, globals(), locals(), [_module_name], level=1)

            for _name in dir(_import):
                if _name.startswith("_"):
                    continue

                # logging.info(getattr(_import, _name))
                _symbol = getattr(_import, _name)
                if (getattr(_symbol, "__module__", None) != f"modules.{_module_name}"
                        or isinstance(_symbol, viur.core.Module) or isinstance(_symbol, types.FunctionType)):
                    continue

                if _name.lower() not in BLACKLIST:
                    logging.debug(f"Importing {_symbol} as {_prefix}{_name.lower()}")
                    _viur_modules[f"{_prefix}{_name.lower()}"] = _symbol

        except Exception:
            logging.exception(f"Unable to import '{_module_name}'")
            raise


_import_modules(Path(__file__).resolve().parent)

globals().update(_viur_modules)

del _viur_modules, Path, logging, viur, _import_modules, BLACKLIST


#########################################
# Manual imports can also be done here! #
#########################################

# import MODULE
# import MODULE as NAME
# from MODULE import CLASS/FUNCTION as NAME
