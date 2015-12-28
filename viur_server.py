#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

# include project specific templates.base_template.libs into sys.path
for lib in os.listdir("libs"):
	if not lib.lower().endswith(".zip"):  # Skip invalid file
		continue
	sys.path.insert(0, os.path.join("libs", lib))

from server.config import conf
# --- KONFIG ---

conf["viur.languageMethod"] = "url"
conf["admin.vi.name"] = "{app_name}"
conf["language_names"] = {{
	"en": u"English", "de": u"Deutsch", "es": u"Español", "fr": u"Français",
	"sv": u"Swedish", "it": u"Italiano", "cs": u"Czechoslovakia", "ru": u"Russian",
	"pt": u"Portugal", "sk": u"Slovak Republic", "da": u"Denmark", "fi": u"Finland",
	"pl": u"Poland", "nl": u"Netherlands", "no": u"Norway"}}

conf["supported_languages"] = ["de", "en"]

conf["country_names"] = {{
	"gb": "Großbritannien", "de": "Deutschland", "fr": u"Frankreich",
	"it": u"Italien", "ru": "Russland", "no": "Norwegen", "se": "Schweden",
	"dk": u"Dänemark", "nl": u"Niederlande", "es": u"Spanien",
	"pt": u"Portugal", "be": u"Belgien", "lu": u"Luxemburg",
	"ch": u"Schweiz", "at": u"Österreich", "cz": u"Tschechien",
	"hu": u"Ungarn", "si": u"Slowenien", "hr": u"Kroatien",
	"fi": u"Finnland", "lt": u"Litauen", "gr": u"Griechenland",
	"tr": u"Türkei", "ie": u"Irland"
}}

import renders
import modules
import server


server.setDefaultLanguage("de")
application = server.setup(modules, renders)


def main():
	server.run()


if __name__ == '__main__':
	main()
