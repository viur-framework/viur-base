#-*- coding: utf-8 -*-
from viur.core.skeleton import Skeleton, RelSkel
from viur.core.bones import *

class vitextSkel(Skeleton):
	name = baseBone(
		descr=u"Name",
		required=True
	)

	text = textBone(
		descr="text"
	)

	text_multi = textBone(
		descr="text multi",
		multiple=True
	)

	text_lang = textBone(
		descr="text lang",
		languages=["de", "en"]
	)

	text_multilang = textBone(
		descr="text multilang",
		multiple=True,
		languages=["de", "en"]
	)
