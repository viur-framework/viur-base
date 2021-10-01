from viur.core.bones import *
from viur.core.skeleton import Skeleton
from viur.core import conf


class ExampleSkel(Skeleton):
	# Defaults
	name = stringBone(
		descr="Name",
		required=True
	)
	sortindex = numericBone(
		descr="Sort index",
		indexed=True,
		required=True
	)
	image = fileBone(
		descr="Image",
		derive=conf["derives"]
	)

	# SEO
	seo_title = stringBone(
		descr="SEO Title",
		params={"category": "SEO"}
	)
	seo_description = stringBone(
		descr="SEO Description",
		params={"category": "SEO"}
	)
	seo_keywords = stringBone(
		descr="SEO Keywords",
		params={"category": "SEO"}
	)
	seo_image = fileBone(
		descr="SEO Preview Image",
		params={"category": "SEO"}
	)
