# -*- coding: utf-8 -*-
from server.modules.user import userSkel
from server.bones import *
from server import conf

class userSkel(userSkel):
	'''
	customer_id = stringBone(descr=u"Customer ID", indexed=True, searchable=True)

	salutation = selectOneBone(descr=u"Salutation", required=True,
	                            values={"Mr.": u"Mr.", "Ms.": u"Mrs.", "none": u"Not provided"},
	                            defaultValue="none")

	company = stringBone(descr=u"Company name", indexed=True, searchable=True)
	title = stringBone(descr=u"Title", indexed=True, searchable=True)
	firstname = stringBone(descr=u"First name", required=True, indexed=True, searchable=True)
	lastname = stringBone(descr=u"Last name", required=True, indexed=True, searchable=True)
	street = stringBone(descr=u"Address", indexed=True, searchable=True)
	zipcode = stringBone(descr=u"ZIP-Code", indexed=True, searchable=True)
	city = stringBone(descr=u"City", indexed=True, searchable=True)
	country = selectCountryBone(descr=u"Country", defaultValue="de", indexed=True)

	phone = stringBone(descr=u"Phone", indexed=True, searchable=True)
	cellphone = stringBone(descr=u"Mobile", indexed=True, searchable=True)
	fax = stringBone(descr=u"Fax", indexed=True, searchable=True)
	'''

	lang = selectOneBone(descr=u"Language",
	                        values=conf["viur.defaultlangsvalues"],
	                        defaultValue="de", visible=True)
