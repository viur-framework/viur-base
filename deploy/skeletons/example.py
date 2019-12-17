#-*- coding: utf-8 -*-
from viur.core.skeleton import Skeleton
from viur.core.bones import *

class exampleSkel(Skeleton):
	# Defaults
	name = stringBone(
		descr=u"Name",
		required=True
	)
	sortindex = numericBone(
		descr=u"Sort index",
		indexed=True,
		required=True
	)
	image = fileBone(
		descr=u"Image"
	)

	# SEO
	seo_title = stringBone(
		descr=u"SEO Title",
		params={"category": u"SEO"}
	)
	seo_description = stringBone(
		descr=u"SEO Description",
		params={"category": u"SEO"}
	)
	seo_keywords = stringBone(
		descr=u"SEO Keywords",
		params={"category": u"SEO"}
	)
	seo_image = fileBone(
		descr=u"SEO Preview Image",
		params={"category": u"SEO"}
	)
