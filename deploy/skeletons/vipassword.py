#-*- coding: utf-8 -*-
from viur.core.skeleton import Skeleton, RelSkel
from viur.core.bones import *


class vipasswordSkel(Skeleton):
	pw = passwordBone(
		descr=u"password"
	)

	pw_lang = passwordBone(
		descr=u"password lang",
		#required=True,
		languages=["de", "en"]
	)
