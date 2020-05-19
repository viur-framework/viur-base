#-*- coding: utf-8 -*-
from viur.core.skeleton import Skeleton, RelSkel
from viur.core.bones import *


class testSkel(RelSkel):
	article = stringBone(
		descr="Article"
	)

	price = numericBone(
		descr="Price",
		precision=2,
		params={
			"style": "amount.€"
		}
	)


class virecordSkel(Skeleton):
	name = stringBone(
		descr=u"Name",
		required=True
	)

	'''
	record = recordBone(
		descr="record",
		using=testSkel
	)
	'''

	record_multi= recordBone(
		descr="record multi",
		format="$(article) - $(price)",
		using=testSkel,
		multiple=True
	)

	'''
	record_lang= recordBone(
		descr="record lang",
		format="$(article) - $(price)",
		using=testSkel,
		languages=["de", "en"]
	)
	'''

	record_multilang= recordBone(
		descr="record multi lang",
		format="$(article) - $(price)",
		using=testSkel,
		multiple=True,
		languages=["de", "en"]
	)
