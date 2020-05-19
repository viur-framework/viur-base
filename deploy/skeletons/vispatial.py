#-*- coding: utf-8 -*-
from viur.core.skeleton import Skeleton, RelSkel
from viur.core.bones import *

class vispatialSkel(Skeleton):
	name = baseBone(
		descr=u"Name",
		required=True
	)

	spatial = spatialBone(
		descr=u"spatial",
		boundsLat=(30.0, 70.0),
		boundsLng=(-20.0, 50.0),
		gridDimensions=(1000.0, 1000.0)
	)

	'''
	spatial_multi = spatialBone(
		descr=u"spatial multi"
		#required=True,
		multiple=True,
		boundsLat=(30.0, 70.0),
		boundsLng=(-20.0, 50.0),
		gridDimensions=(1000.0, 1000.0)
	)

	spatial_lang = spatialBone(
		descr=u"spatial lang",
		#required=True,
		languages=["de", "en"],
		boundsLat=(30.0, 70.0),
		boundsLng=(-20.0, 50.0),
		gridDimensions=(1000.0, 1000.0)
	)

	spatial_multilang = spatialBone(
		descr=u"spatial multilang",
		#required=True,
		multiple=True,
		languages=["de", "en"],
		boundsLat=(30.0, 70.0),
		boundsLng=(-20.0, 50.0),
		gridDimensions=(1000.0, 1000.0)
	)
	'''
