#-*- coding: utf-8 -*-
from viur.core.skeleton import Skeleton, RelSkel
from viur.core.bones import *


class viemailSkel(Skeleton):
	email = emailBone(
		descr=u"email",
		required=True
	)

	email_multi = emailBone(
		descr=u"email multi",
		#required=True,
		multiple=True
	)

	email_lang = emailBone(
		descr=u"email lang",
		#required=True,
		languages=["de", "en"]
	)

	email_multilang = emailBone(
		descr=u"email multilang",
		#required=True,
		multiple=True,
		languages=["de", "en"]
	)
