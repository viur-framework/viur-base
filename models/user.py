# -*- coding: utf-8 -*-

from server.modules.{user_module} import userSkel
from server.bones import *
from server import conf


class userSkel(userSkel):
	customer_id = stringBone(descr=u"customer id (import)", required=False, indexed=True, searchable=True)
	dealer_group = stringBone(descr=u"dealer group (import)", required=False, indexed=True, searchable=True)

	salutation = selectOneBone(descr=u"Anrede", required=True,
	                           values={{"Mr.": u"Herr", "Ms.": u"Frau", "none": u"Keine Angabe"}},
	                           defaultValue="none")
	companyname = stringBone(descr=u"Firmenname", required=False, indexed=True, searchable=True)
	title = stringBone(descr=u"Titel", required=False, indexed=True, searchable=True)
	firstname = stringBone(descr=u"Vorname", required=True, indexed=True, searchable=True)
	lastname = stringBone(descr=u"Nachname", required=True, indexed=True, searchable=True)
	street = stringBone(descr=u"Straße und Hausnummer", required=False, indexed=True, searchable=True)
	zipcode = stringBone(descr=u"PLZ", required=False, indexed=True, searchable=True)
	city = stringBone(descr=u"Stadt", required=False, indexed=True, searchable=True)
	country = selectCountryBone(descr=u"Land", required=False, defaultValue="de", indexed=True)
	phone = stringBone(descr=u"Telefon", required=False, indexed=True, searchable=True)
	cell_phone = stringBone(descr=u"Mobiltelefon", required=False, indexed=True, searchable=True)
	fax = stringBone(descr=u"Fax", required=False, indexed=True, searchable=True)
	lang = selectOneBone(descr=u"Sprache", values=conf["language_names"], defaultValue="de", visible=True)
