#-*- coding: utf-8 -*-
from viur.core.skeleton import Skeleton, RelSkel
from viur.core.bones import *

class vifileSkel(Skeleton):
	name = baseBone(
		descr=u"Name",
		required=True
	)

	file = fileBone(
		descr=u"file"
	)

	file_multi = fileBone(
		descr=u"file multi",
		#required=True,
		multiple=True
	)

	file_lang = fileBone(
		descr=u"file lang",
		#required=True,
		languages=["de", "en"]
	)

	file_multilang = fileBone(
		descr=u"file multilang",
		#required=True,
		multiple=True,
		languages=["de", "en"]
	)
