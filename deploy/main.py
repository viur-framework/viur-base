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

from viur.core import conf, db, email, securityheaders, secret, current, errors, setup
from viur.core.config import ConfigType


# ------------------------------------------------------------------------------
# Project-specific configuration
#

MY_VERSION = "0.0.1" + ("-dev" if "dev" in conf.instance.project_id else "")


class ProjectConfig(ConfigType):
    """
    This class represents the project configuration.

    It should contain any parametrization used throughout the project, and can always be accessed by
    by `conf.project` after importing `conf` from `viur.core`.
    """

    version = MY_VERSION
    """Version number"""

    maintenance_mode = False
    """Maintenance mode"""

    appnames = {
        "{{app_id}}": "My Project",
    }

    main_url = None if conf.instance.is_dev_server else "https://www.example.com"

    # see https://core.docs.viur.dev/en/stable/viur/core/bones/file/index.html#core.bones.file.FileBone derive-parameter
    # standard_derives = {
    #     "thumbnail": [
    #         {"width": 1920},
    #         {"width": 1280},
    #         {"width": 900},
    #         {"width": 500}
    #     ]
    # }


conf.project = ProjectConfig()

# ------------------------------------------------------------------------------
# General configuration
#

conf.valid_application_ids = list(conf.project.appnames.keys())


# ------------------------------------------------------------------------------
# Debugging & Performance
#

# conf.debug.disable_cache = True
# conf.debug.trace = True
# conf.debug.trace_external_call_routing = True
# conf.debug.trace_exceptions = True
# db.config["traceQueries"] = True

# ViUR >= 3.4 compatibility feature disabling
conf.compatibility.remove("json.bone.structure.keytuples")  # render new dict-style bone-structure
conf.compatibility.remove("json.bone.structure.camelcasenames")  # render new keys in bone structure only

# ViUR >= 3.5 compatibility feature disabling
conf.compatibility.remove("json.bone.structure.inlists")  # disable structure rendering on list

# ViUR >= 3.6 compatibility feature disabling
# render old-style tuple-list in SelectBone's values structure
conf.compatibility.remove("bone.select.structure.values.keytuple")

# ------------------------------------------------------------------------------
# User module
#

# Client-ID for OAuth with Google Account
# conf.user.google_client_id = ""
# conf.user.google_gsuite_domains = ["example.com"]

# User roles
#
# conf.user.roles = {
#     "custom": "Custom setting",
#     "admin": "Administrator",
#     "backoffice": "Back office worker",
#     "salesforce": "Sales force worker",
# }

# ------------------------------------------------------------------------------
# File module
#

# Enable thumbnailer if ViUR should downscale images
# from viur.core.modules.file import thumbnailer
#
# conf.file_derivations = {
#     "thumbnail": thumbnailer
# }

# ------------------------------------------------------------------------------
# Language-specific configuration
#

# conf.i18n.language_method = "url"
# conf.i18n.available_languages = ["en", "de"]

# ------------------------------------------------------------------------------
# Admin specific configurations
#

conf.admin.name = \
    conf.project.appnames.get(conf.instance.project_id, conf.instance.project_id) \
    + " v" + conf.project.version

# conf.admin.logo = "/static/images/logo.svg"
# conf.admin.login_logo = "/static/images/logo.svg"
# conf.admin.login_background = "login-backgound-2.jpg"
# conf.admin.color_primary = "#2e7291"
# conf.admin.color_secondary = "#15a995"
# conf.admin.module_groups = {
#     "system": {
#         "name": "System",
#         "icon": "gear",
#     },
# }

# ------------------------------------------------------------------------------
# Email configuration
#

# conf.email.mailjet_api_key = secret.get("mailjet-api-key")
# conf.email.mailjet_api_secret = secret.get("mailjet-api-secret")
# conf.email.transport_class = email.EmailTransportMailjet
# conf.email.send_from_local_development_server = True  # enable sending emails from local development server
# conf.email.sender_override = "mail@viur.dev"
# conf.email.recipient_override = ["mail@viur.dev"]  # send all emails to this recipient

# ------------------------------------------------------------------------------
# Content Security Policy (CSP)
#

# GitHub Buttons
securityheaders.addCspRule("style-src", "unsafe-inline", "enforce")  # yes, GitHub buttons need this...
securityheaders.addCspRule("script-src", "buttons.github.io", "enforce")
securityheaders.addCspRule("connect-src", "api.github.com", "enforce")

# Enable this if you want to use the captcha, but not unsafe-inline:
# securityheaders.addCspRule("script-src", "sha256-TLq3i7CjxmHUoz+BrQ6w5D2+hv35BEkew240zhZ0uvA=", "enforce")

# ------------------------------------------------------------------------------
# Enforce use of a config-specific domain using request preprocessor
#

# if conf.project.main_url:
#     def handle_request(path):
#         """
#         This simple request preprocessor can be used to canalize all requests coming
#         from several domains and 301 redirects them to a main URL.
#         """
#         request = current.request.get()
#         if request.is_deferred:
#             return path
#
#         # This is the enforced main-URL
#         main_url = conf.project.main_url
#         url = request.request.url.lower()
#
#         # The enforcement is only performed when the URL is...
#         if not url.startswith(main_url):
#             for proto in ["http://", "https://"]:
#                 if url.startswith(proto):
#                     # ... inside of this list.
#                     for other in (main_url.removeprefix("https://"), ):
#                         if url[len(proto):].startswith(other):
#                             raise errors.Redirect(main_url + url[len(proto) + len(other):], status=301)  # permanent
#
#         # otherwise, the URL remains untouched
#         return path
#
#     conf.request_preprocessor = handle_request

# ------------------------------------------------------------------------------
# Provide a maintenance mode using the request preprocessor
#

# if conf.project.maintenance_mode:
#     def maintenance_mode(path):
#         """
#         Request preprocessor for maintenance mode;
#         Only root-users can work normally.
#         """
#         cuser = current.user.get()
#         if not (cuser and "root" in cuser["access"]):
#             return "/s/maintenance"
#
#         return path
#
#     conf.request_preprocessor = maintenance_mode

# ------------------------------------------------------------------------------
# CORS configuration for VueJS development
#

# import re
#
# conf.security.cors_max_age = datetime.timedelta(seconds=30)
# conf.security.cors_allow_credentials = True
# conf.security.cors_origins = "*"
# conf.security.cors_origins = [
#     # "*",
#     # "http://localhost:8080",
#     # "http://localhost:9090",
#     # Allows any localhost port:
#     re.compile(r"^(http://localhost:(\d{4,5}))/?$", flags=re.IGNORECASE),
# ]
# # conf.security.cors_origins_use_wildcard = True
#
# # Allows the header "X-Requested-With" and "X-ViUR-*"
# conf.security.cors_allow_headers = [
#     "X-Requested-With",
#     re.compile(r"^X-ViUR-.*$", flags=re.IGNORECASE),
# ]

# ------------------------------------------------------------------------------
# Server startup
#

import modules  # noqa
import render  # noqa

# core.setDefaultLanguage("de")
app = setup(modules, render)
