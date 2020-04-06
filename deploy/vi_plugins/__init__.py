# -*- coding: utf-8 -*-

# This is the major Vi plugin init file.
# Do custom plugin imports and customized settings here.

# Plugin imports
#import vi_plugins.bones

# Vi config
from vi.config import conf

# Change default batch size
#conf["batchSize"] = 64

# Show bone name identifiers instead of descriptions:
#conf["showBoneNames"] = False

# To globally disable the internal preview, uncomment this:
#conf["internalPreview"] = False

# Change language
# from i18n import setLanguage, getLanguage
#conf["currentlanguage"] = "de"
#setLanguage(conf["currentlanguage"])

print(conf)
print("!!! ALL PROJECT CUSTOMIZATIONS LOADED !!!")