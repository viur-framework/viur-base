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


def _import_modules(_dir: Path, _prefix: str = "") -> None:
    for _path in _dir.iterdir():
        if _path.is_dir():
            _import_modules(_path, f"{_prefix}{_path.stem}.")
            continue

        elif _path.stem.startswith("_") or _path.suffix != ".py":
            continue

        _module = _prefix + _path.stem

        try:
            _import = __import__(_module, globals(), locals(), [_module], level=1)

            for _name in dir(_import):
                if _name.startswith("_"):
                    continue

                _symbol = getattr(_import, _name)
                if (getattr(_symbol, "__module__", None) != f"modules.{_module}"
                        or isinstance(_symbol, viur.core.Module) or isinstance(_symbol, types.FunctionType)):
                    continue

                if (alias := f"{_prefix}{_name.lower()}") not in BLACKLIST:
                    logging.debug(f"Importing {_symbol} as {alias}")
                    _viur_modules[alias] = _symbol

        except Exception:
            logging.exception(f"Unable to import '{_module}'")
            raise


_import_modules(Path(__file__).resolve().parent)

globals().update(_viur_modules)

del _viur_modules, Path, logging, viur, _import_modules, BLACKLIST

#########################################
# Manual imports can also be done here! #
#########################################

# noinspection PyUnresolvedReferences
from viur.core.modules.site import Site as s  # noqa: E402
