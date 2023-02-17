from viur.core import conf
from viur.core.bones import *
from viur.core.skeleton import Skeleton


class ExampleSkel(Skeleton):
    # Defaults
    name = StringBone(
        descr="Name",
        required=True
    )

    sortindex = NumericBone(
        descr="Sort index",
        indexed=True,
        required=True
    )

    image = FileBone(
        descr="Image",
        derive=conf["derives"]
    )

    # SEO
    seo_title = StringBone(
        descr="SEO Title",
        params={
            "category": "SEO"
        }
    )

    seo_description = StringBone(
        descr="SEO Description",
        params={
            "category": "SEO"
        }
    )

    seo_keywords = StringBone(
        descr="SEO Keywords",
        params={
            "category": "SEO"
        }
    )

    seo_image = FileBone(
        descr="SEO Preview Image",
        params={
            "category": "SEO"
        }
    )
