#-*- coding: utf-8 -*-
from viur.core.skeleton import Skeleton, RelSkel
from viur.core.bones import *


class vidateSkel(Skeleton):
	name = stringBone(
		descr="Name",
		required=True
	)

	date = dateBone(
		descr="date",
		time=False
	)

	time = dateBone(
		descr="time",
		date=False
	)

	datetime = dateBone(
		descr="datetime"
	)
