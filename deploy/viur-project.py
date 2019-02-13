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
#conf["admin.vi.logo"] = "/static/meta/logo.svg"

# ------------------------------------------------------------------------------
# Content Security Policy
#

# This is an example configuration to allow different content-security policies
# from several trusted domains.

# securityheaders.addCspRule("default-src", "*.gstatic.com", "enforce")

# securityheaders.addCspRule("script-src", "unsafe-inline", "enforce")
# securityheaders.addCspRule("script-src", "*.googleapis.com", "enforce")
# securityheaders.addCspRule("script-src", "*.google.com", "enforce")
# securityheaders.addCspRule("script-src", "*.gstatic.com", "enforce")
# securityheaders.addCspRule("script-src", "*.google-analytics.com", "enforce")
# securityheaders.addCspRule("script-src", "*.jquery.com", "enforce")

# securityheaders.addCspRule("img-src", "*.google-analytics.com", "enforce")

# securityheaders.addCspRule("img-src", "data:", "enforce")
# securityheaders.addCspRule("img-src", "unsafe-inline", "enforce")
# securityheaders.addCspRule("img-src", "unsafe-eval", "enforce")

# securityheaders.addCspRule("style-src", "fonts.googleapis.com", "enforce")

# securityheaders.addCspRule("frame-src", "*.youtube-nocookie.com", "enforce")
# securityheaders.addCspRule("frame-src", "*.youtube.com", "enforce")
# securityheaders.addCspRule("frame-src", "*.google.com", "enforce")

# ---------------------------------------------------------------------------------------------------------------------
# Request preprocessor
#

# The request preprocessor can be used to perform rewritings and other,
# request-related stuff before the normal ViUR function routing will be
# executed.

'''
def handleRequest(path):
	if "X-AppEngine-TaskName" in server.request.current.get().request.headers:
		return path

	url = server.request.current.get().request.url

	if url.startswith("https://your-domain.com"):
		raise server.errors.Redirect(url.replace("https://", "https://www.", 1))

	return path

conf["viur.requestPreprocessor"] = handleRequest
'''

# ------------------------------------------------------------------------------
# Server startup
#

import server, modules, render

#server.setDefaultLanguage("en") #set default language!
application = server.setup(modules, render)

if __name__ == '__main__':
	server.run()
