"""
This is the ViUR default module importer.

If any other importing logic is wanted, please switch to manual import calls in this file, and remove
the dynamic code provided below.
"""

####################################
# Automatic imports are done here! #
####################################

import os
import importlib
import inspect
from pathlib import Path
from viur.core import Module as __viur_Module

# Get the current directory (where this __init__.py is located)
__current_dir = Path(__file__).parent

# Define a blacklist of filenames (without path)
BLACKLIST = {"exclude_this.py", "ignore_me.py"}


# Recursive function to find all .py files in subdirectories
def __find_py_files(directory):
    py_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py") and file != "__init__.py" and file not in BLACKLIST:
                py_files.append(Path(root) / file)

    return py_files


# Iterate over all Python files in the module hierarchy
for __py_file in __find_py_files(__current_dir):
    # Convert file path to module name
    __relative_path = __py_file.relative_to(__current_dir)
    __module_name = ".".join(__relative_path.with_suffix("").parts)

    # Import the module
    __module = importlib.import_module(f".{__module_name}", package=__name__)

    # Inspect module for classes of type Module
    for name, obj in inspect.getmembers(__module, inspect.isclass):
        if issubclass(obj, __viur_Module) and obj.__module__ == __module.__name__:
            # Import the class into the current namespace
            print(name.lower(), obj)
            globals()[name.lower()] = obj


#########################################
# Manual imports can also be done here! #
#########################################

# noinspection PyUnresolvedReferences
# from viur.core.modules.site import Site as s  # noqa: E402, E401
