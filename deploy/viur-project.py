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
# ------------------------------------------------------------------------------
#
# Project:      {{app_id}}
# Initiated:    {{timestamp}}
# Copyright:    {{whoami}} @ Mausbrand Informationssysteme GmbH
# Author:       {{whoami}}
#
# ------------------------------------------------------------------------------

from server import conf, securityheaders

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

# ------------------------------------------------------------------------------
# ViUR admin tool specific configurations
#

conf["admin.vi.name"] = "{{app_id}}"

# ------------------------------------------------------------------------------
# Content Security Policy
#

#GitHub Buttons
securityheaders.addCspRule("script-src", "buttons.github.io", "enforce")
securityheaders.addCspRule("connect-src", "api.github.com", "enforce")

# ------------------------------------------------------------------------------
# Server startup
#

import server, modules, render

#server.setDefaultLanguage("en") #set default language!
application = server.setup(modules, render)

if __name__ == '__main__':
	server.run()
