#-*- coding: utf-8 -*-
from viur.core.skeleton import Skeleton, RelSkel
from viur.core.bones import *


class vicolorSkel(Skeleton):
	name = stringBone(
		descr="Name",
		required=True
	)

	color = colorBone(
		descr="color"
	)

	color_lang = colorBone(
		descr="color lang",
		languages=["de", "en"]
	)
