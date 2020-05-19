#-*- coding: utf-8 -*-
from viur.core.skeleton import Skeleton, RelSkel
from viur.core.bones import *


class vibooleanSkel(Skeleton):
	name = stringBone(
		descr="Name",
		required=True
	)

	boolean = booleanBone(
		descr=u"Boolean"
	)

	boolean_lang = booleanBone(
		descr=u"Boolean lang",
		languages=["de", "en"]
	)
