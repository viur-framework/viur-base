#-*- coding: utf-8 -*-
from viur.core.skeleton import Skeleton, RelSkel
from viur.core.bones import *

class vidirSkel(Skeleton):
	name = baseBone(
		descr=u"Name",
		required=True
	)

	treedir = treeDirBone(
		descr=u"dir",
		kind="file",
		module="file"
	)
	'''
	treedir_multi = treedirBone(
		descr=u"dir multi",
		#required=True,
		multiple=True,
		kind="file"
	)

	treedir_lang = treedirBone(
		descr=u"dir lang",
		#required=True,
		languages=["de", "en"],
		kind="file"
	)

	treedir_lang = treedirBone(
		descr=u"dir multilang",
		#required=True,
		multiple=True,
		languages=["de", "en"],
		kind="file"
	)
	'''
