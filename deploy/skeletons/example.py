from viur.core import conf
from viur.core.bones import *
from viur.core.skeleton import Skeleton


class ExampleSkel(Skeleton):
    # Defaults
    name = StringBone(
        descr="Name",
        required=True,
    )

    # image = FileBone(
    #     descr="Image",
    #     derive=conf.project.standard_derives,
    # )
