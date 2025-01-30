from viur.core.bones import *
from viur.core.skeleton import Skeleton


class EmptySkel(Skeleton):
    name = StringBone(
        descr="Name",
        required=True,
    )
