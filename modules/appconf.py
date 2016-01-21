# -*- coding: utf-8 -*-
from server.prototypes.singleton import Singleton

class appconf(Singleton):

	adminInfo = {
		"name": u"Configuration",
		"handler": "singleton",
	    "icon": "icons/modules/settings.svg",
	    "sortIndex": 1
	}

appconf.jinja2 = True
