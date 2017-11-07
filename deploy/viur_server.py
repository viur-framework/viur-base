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
# Started:	    {{timestamp}}
# Copyright:    mausbrand GmbH, Dortmund
# Author:       {{whoami}}
#

from server import conf

# ------------------------------------------------------------------------------
# General configuration
#

#conf["viur.forceSSL"] = True
#conf["viur.disableCache"] = True

# ------------------------------------------------------------------------------
# Language-specific configuration
#

#conf["viur.languageMethod"] = "url"
#conf["viur.availableLanguages"] = ["en", "de"]

#conf["viur.defaultlangsvalues"] = {
# 	"en": u"English",
# 	"de": u"Deutsch",
# 	"es": u"Español",
# 	"fr": u"Français",
# 	"sv": u"Swedish",
# 	"it": u"Italiano",
# 	"cs": u"Čeština (Czech)",
# 	"ru": u"Русский (Russian)",
# 	"pt": u"Português",
# 	"sk": u"Slovenčina",
# 	"da": u"Dansk",
# 	"fi": u"Suomi (Finnish)",
# 	"pl": u"Polski",
# 	"nl": u"Nederlands",
# 	"no": u"Norsk" }

#server.setDefaultLanguage("en") #set default language!

# ------------------------------------------------------------------------------
# ViUR admin tool specific configurations
#

conf["admin.vi.name"] = "{{app_id}}"
#conf["admin.vi.logo"] = "/static/meta/logo.svg"

# ------------------------------------------------------------------------------
# Content Security Policy
#

conf["viur.security.contentSecurityPolicy"] = {}

# ------------------------------------------------------------------------------
# Bugsnag: Tell us what is wrong!
#

#conf["bugsnag.apiKey" ] = "INSERT YOUR BUGSNAG API KEY HERE"

# ------------------------------------------------------------------------------
# Server startup
#

import server, modules

application = server.setup(modules, server.render)

def main():
	server.run()

if __name__ == '__main__':
	main()
