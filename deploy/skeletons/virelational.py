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


class virelationalSkel(Skeleton):
	name = stringBone(
		descr=u"Name",
		required=True
	)

	relational = relationalBone(
		descr=u"Relational",
		kind="virelational"
	)

	relational_multi = relationalBone(
		descr=u"Relational multi",
		kind="virelational",
		multiple=True
	)

	relational_lang = relationalBone(
		descr=u"Relational lang",
		kind="virelational",
		languages=["de", "en"]
	)

	relational_multilang = relationalBone(
		descr=u"Relational multilang",
		kind="virelational",
		languages=["de", "en"],
		multiple=True
	)

	relationalusing = relationalBone(
		descr=u"Relationalusing",
		kind="virelational",
		format="$(dest.name) - $(rel.test)",
		using=testSkel
	)

	relationalusing_multi = relationalBone(
		descr=u"Relationalusing multi",
		kind="virelational",
		multiple=True,
		using=testSkel
	)

	relationalusing_lang = relationalBone(
		descr=u"Relationalusing lang",
		kind="virelational",
		languages=["de", "en"],
		using=testSkel
	)

	relationalusing_multilang = relationalBone(
		descr=u"Relationalusing multilang",
		kind="virelational",
		languages=["de", "en"],
		multiple=True,
		using=testSkel
	)
