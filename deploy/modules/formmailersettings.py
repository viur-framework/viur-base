from viur.core.prototypes.singleton import Singleton


class Formmailersettings(Singleton):
	adminInfo = {
		"name": "Formmailersettings",
		"moduleGroup": "settings",
		"handler": "singleton.formmailersettings",
		"icon": "icon-inbox"
	}
