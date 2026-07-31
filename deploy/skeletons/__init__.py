# This is the ViUR default skeleton importer;
# If any other importing logic is wanted, please switch to manual import calls in this file, and remove
# the dynamic code provided below.

import os

for skel_module in os.listdir(os.path.dirname(__file__)):
    if skel_module == "__init__.py" or not skel_module.endswith(".py"):
        continue

    __import__(skel_module[:-3], globals(), locals(), level=1)

del skel_module
