from viur.core.bones import *
from viur.core.skeleton import Skeleton


class SettingsSkel(Skeleton):

	# Site Settings
	site_title = stringBone(
		descr="Site-Title",
		defaultValue="{{app_id}}"
	)

	site_slogan = stringBone(
		descr="Site-Slogan",
		defaultValue="Website for {{app_id}}"
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
	seo_image = fileBone(
		descr="SEO Preview Image",
		params={"category": "SEO"}
	)
	'''
	Caution!
		This switches <meta name="robots" content="index, follow"> in viur_base.html on.
		We recommend you switching this via the VI.
	'''
	is_development = booleanBone(
		descr="This Website is in development mode (noindex nofollow is set). Disabling this sets index and follow",
		defaultValue=True
	)
