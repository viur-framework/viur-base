# This is the ViUR default skeleton importer;
# If any other importing logic is wanted, please switch to manual import calls in this file, and remove
# the dynamic code provided below.

import os

for skelModule in os.listdir(os.path.dirname(__file__)):
    if skelModule == "__init__.py" or not skelModule.endswith(".py"):
        continue

    __import__(skelModule[:-3], globals(), locals(), level=1)

del skelModule
