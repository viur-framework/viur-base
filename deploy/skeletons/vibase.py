#-*- coding: utf-8 -*-
from viur.core.skeleton import Skeleton, RelSkel
from viur.core.bones import *


class vibaseSkel(Skeleton):
	name = baseBone(
		descr=u"Base",
		required=True
	)

	name_multi = baseBone(
		descr=u"Base multi",
		#required=True,
		multiple=True
	)

	name_lang = baseBone(
		descr=u"Base lang",
		#required=True,
		languages=["de", "en"]
	)

	name_multilang = baseBone(
		descr=u"Base multilang",
		#required=True,
		multiple=True,
		languages=["de", "en"]
	)
