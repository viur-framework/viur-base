#-*- coding: utf-8 -*-
from server.skeleton import Skeleton
from server.bones import *

class personSkel(Skeleton):
	name = stringBone(descr="Name")
	age = numericBone(descr="Age")
