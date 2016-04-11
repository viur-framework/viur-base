# -*- coding: utf-8 -*-
from server.modules.user import User
from skeletons.user import userSkel

class user(User):
	baseSkel = userSkel
	viewSkel = userSkel

	adminInfo = {
		"name": u"User",
	    "handler": "list",
	    "icon": "icons/modules/users.svg"
	}
