# -*- coding: utf-8 -*-

from server.modules.{{user_module}} import {{user_module_class}}
from models.user import userSkel

class user({{user_module_class}}):
	baseSkel = userSkel
	viewSkel = userSkel

	adminInfo = {
		"name": u"User",
	    "handler": "list",
	    "icon": "icons/modules/users.svg"
	}
