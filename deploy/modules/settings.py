from viur.core.prototypes.singleton import Singleton


class Settings(Singleton):
	adminInfo = {
		"name": "Settings",
		"moduleGroup": "settings",
		"handler": "singleton.settings",
		"icon": "icon-settings"
	}

	# Everyone can access the settings, even without being logged in,
	# because the settings contain information like the site title
	def canView(self):
		return True


Settings.json = True
Settings.html = True
