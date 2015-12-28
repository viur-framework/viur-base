# -*- coding: utf-8 -*-
from server.applications.singleton import Singleton


class appconf(Singleton):
	adminInfo = {"name": u"global config",
	             "handler": "singleton",
	             "icon": "icons/modules/settings.svg",
	             "sortIndex": 1
	}


appconf.jinja2 = True
