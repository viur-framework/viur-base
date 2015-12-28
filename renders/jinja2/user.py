# -*- coding: utf-8 -*-
import time
import json
from string import Template

import default
from server.skeleton import Skeleton
from server import errors


class Render(default.Render):  # Render user-data to xml
	loginTemplate = "user_login"
	editTemplate = "user_edit"
	editSuccessTemplate = "user_edit_success"
	logoutSuccessTemplate = "user_logout_success"
	loginSuccessTemplate = "user_login_success"
	verifySuccessTemplate = "user_verify_success"
	verifyFailedTemplate = "user_verify_failed"
	passwdRecoverInfoTemplate = "user_passwdrecover_info"

	def login(self, skel, tpl=None, **kwargs):
		return ( self.edit(skel, tpl=(tpl or self.loginTemplate), **kwargs) )

	def loginSucceeded(self, tpl=None, **kwargs):
		raise errors.Redirect("/index")

	def logoutSuccess(self, tpl=None, **kwargs):
		if "logoutSuccessTemplate" in dir(self.parent):
			tpl = tpl or self.parent.logoutSuccessTemplate
		else:
			tpl = tpl or self.logoutSuccessTemplate
		template = self.getEnv().get_template(self.getTemplateFileName(tpl))
		return ( template.render(**kwargs) )

	def verifySuccess(self, skel, tpl=None, **kwargs):
		if "verifySuccessTemplate" in dir(self.parent):
			tpl = tpl or self.parent.verifySuccessTemplate
		else:
			tpl = tpl or self.verifySuccessTemplate
		template = self.getEnv().get_template(self.getTemplateFileName(tpl))
		return ( template.render(**kwargs) )

	def verifyFailed(self, tpl=None, **kwargs):
		if "verifyFailedTemplate" in dir(self.parent):
			tpl = tpl or self.parent.verifyFailedTemplate
		else:
			tpl = tpl or self.verifyFailedTemplate
		template = self.getEnv().get_template(self.getTemplateFileName(tpl))
		return ( template.render(**kwargs) )

	def passwdRecoverInfo(self, msg, skel=None, tpl=None, **kwargs):
		if "passwdRecoverInfoTemplate" in dir(self.parent):
			tpl = tpl or self.parent.passwdRecoverInfoTemplate
		else:
			tpl = tpl or self.passwdRecoverInfoTemplate
		template = self.getEnv().get_template(self.getTemplateFileName(tpl))
		if skel:
			skel = self.collectSkelData(skel)
		return ( template.render(skel=skel, msg=msg, **kwargs) )

	def passwdRecover(self, *args, **kwargs):
		return ( self.edit(*args, **kwargs) )
