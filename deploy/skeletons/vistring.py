#-*- coding: utf-8 -*-
from viur.core.skeleton import Skeleton, RelSkel
from viur.core.bones import *


class vistringSkel(Skeleton):
	string = stringBone(
		descr=u"String",
		required=True
	)

	string_multi = stringBone(
		descr=u"String multi",
		#required=True,
		multiple=True
	)

	string_lang = stringBone(
		descr=u"String lang",
		#required=True,
		languages=["de", "en"]
	)

	string_multilang = stringBone(
		descr=u"String multilang",
		#required=True,
		multiple=True,
		languages=["de", "en"]
	)
