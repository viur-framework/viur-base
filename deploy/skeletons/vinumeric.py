#-*- coding: utf-8 -*-
from viur.core.skeleton import Skeleton, RelSkel
from viur.core.bones import *


class vinumericSkel(Skeleton):
	name = stringBone(
		descr=u"Name",
		required=True
	)

	numeric = numericBone(
		descr="numeric"
	)

	numeric_prec = numericBone(
		descr="numeric prec=2",
		precision=2
	)

	numeric_euro = numericBone(
		descr="numeric euro",
		params={
			"style": "amount.€"
		}
	)

	numeric_euro_prec = numericBone(
		precision=2,
		descr="numeric euro prec=2",
		params={
			"style": "amount.€"
		}
	)

	numeric_dollar_prec = numericBone(
		descr="numeric multiple dollar prec=2",
		precision=2,
		params={
			"style": "amount.$ delimiter.dot"
		},
		multiple=True
	)

	numeric_bitcoin_prec4 = numericBone(
		descr="numeric bitcoin lang prec4",
		precision=4,
		params={
			"style": "amount.BTC"
		},
		languages=["de", "en"]
	)
