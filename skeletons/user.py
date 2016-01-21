# -*- coding: utf-8 -*-

from server.modules.{{user_module}} import userSkel
from server.bones import *
from server import conf

class userSkel(userSkel):
	customer_id = stringBone(descr=u"Customer ID", required=False, indexed=True, searchable=True)

	salutation = selectOneBone(descr=u"Salutation", required=True,
	                           values={"Mr.": u"Mr.", "Ms.": u"Mrs.", "none": u"Not provided"},
	                           defaultValue="none")

	company = stringBone(descr=u"Company name", required=False, indexed=True, searchable=True)
	title = stringBone(descr=u"Title", required=False, indexed=True, searchable=True)
	firstname = stringBone(descr=u"First name", required=True, indexed=True, searchable=True)
	lastname = stringBone(descr=u"Last name", required=True, indexed=True, searchable=True)
	street = stringBone(descr=u"Address", required=False, indexed=True, searchable=True)
	zipcode = stringBone(descr=u"ZIP-Code", required=False, indexed=True, searchable=True)
	city = stringBone(descr=u"City", required=False, indexed=True, searchable=True)
	country = selectCountryBone(descr=u"Country", required=False, defaultValue="de", indexed=True)

	phone = stringBone(descr=u"Phone", required=False, indexed=True, searchable=True)
	cellphone = stringBone(descr=u"Mobile", required=False, indexed=True, searchable=True)
	fax = stringBone(descr=u"Fax", required=False, indexed=True, searchable=True)

	lang = selectOneBone(descr=u"Language", values=conf["viur.defaultlangsvalues"],
	                        defaultValue="de", visible=True)
