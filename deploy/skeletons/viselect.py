#-*- coding: utf-8 -*-
from viur.core.skeleton import Skeleton, RelSkel
from viur.core.bones import *

class viselectSkel(Skeleton):
	name = stringBone(
		descr=u"Name",
		required=True
	)

	select = selectBone(
		descr="select",
		values={"eins": "1", "zwei": "2", "drei": "3"}
	)

	select_lang = selectBone(
		descr="select lang",
		values=["eins", "zwei", "drei"],
		languages=["de", "en"]
	)

	select_multi = selectBone(
		descr="select multi",
		multiple=True,
		values={"eins": "1", "zwei": "2", "drei": "3"}
	)

	select_multi_lang = selectBone(
		descr="select multi lang",
		multiple=True,
		values=["eins", "zwei", "drei"],
		languages=["de", "en"]
	)
