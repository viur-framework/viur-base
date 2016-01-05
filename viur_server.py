#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#                 iii
#                iii
#               iii
#
#           vvv iii uu      uu rrrrrrrr
#          vvvv iii uu      uu rr     rr
#   v     vvvv  iii uu      uu rr     rr
#  vvv   vvvv   iii uu      uu rr rrrrr
# vvvvv vvvv    iii uu      uu rr rrr
#  vvvvvvvv     iii uu      uu rr  rrr
#   vvvvvv      iii  uu    uu  rr   rrr
#    vvvv       iii   uuuuuu   rr    rrr
#
#   I N F O R M A T I O N    S Y S T E M
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Project:      {{app_id}}
# Copyright:    ???
# Authors:      ???
#

import os, sys

# include project specific templates.base_template.libs into sys.path
for lib in os.listdir("libs"):
	if not lib.lower().endswith(".zip"):  # Skip invalid file
		continue
	sys.path.insert(0, os.path.join("libs", lib))

from server.config import conf

# --- KONFIG ---

conf["viur.languageMethod"] = "url"
conf["admin.vi.name"] = "{{app_name}}"
conf["viur.defaultlangsvalues"] = {
	"en": u"English",
	"de": u"Deutsch",
	"es": u"Español",
	"fr": u"Français",
    "sv": u"Swedish",
    "it": u"Italiano",
    "cs": u"Čeština (Czech)",
    "ru": u"Русский (Russian)",
    "pt": u"Português",
    "sk": u"Slovenčina",
    "da": u"Dansk",
    "fi": u"Suomi (Finnish)",
    "pl": u"Polski",
    "nl": u"Nederlands",
    "no": u"Norsk" }

conf["supported_languages"] = ["de", "en"]

conf["country_names"] = {
	"gb": u"Great Britain",
	"de": u"Germany",
	"fr": u"France",
	"it": u"Italia",
	"ru": u"Russia",
	"no": u"Norway",
	"se": u"Sweden",
	"dk": u"Denmark",
	"nl": u"Netherlands",
	"es": u"Spain",
	"pt": u"Portugal",
	"be": u"Belgium",
	"lu": u"Luxemburg",
	"ch": u"Switzerland",
	"at": u"Austrial",
	"cz": u"Czech Republic",
	"hu": u"Hungrary",
	"si": u"Slowenia",
	"hr": u"Croatia",
	"fi": u"Finland",
	"lt": u"Latvia",
	"gr": u"Greek",
	"tr": u"Turkey",
	"ie": u"Ireland"
}

import renders
import modules
import server

server.setDefaultLanguage("en")
application = server.setup(modules, renders)

def main():
	server.run()

if __name__ == '__main__':
	main()
