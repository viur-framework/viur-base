import json, logging, urllib

from skeletons.allbones import StringRelSkel
from viur.core.bones import *
from viur.core.prototypes import List
from viur.core.skeleton import RelSkel

flags = [
	{
		"required": False,
		"readOnly": False,
		"visible": False,
		"multiple": False,
	},
	{
		"required": True,
		"readOnly": False,
		"visible": False,
		"multiple": False,
	},
	{
		"required": False,
		"readOnly": True,
		"visible": False,
		"multiple": False,
	},
	{
		"required": False,
		"readOnly": False,
		"visible": True,
		"multiple": False,
	},
	{
		"required": True,
		"readOnly": True,
		"visible": False,
		"multiple": False,
	},
	{
		"required": True,
		"readOnly": False,
		"visible": True,
		"multiple": False,
	},
	{
		"required": False,
		"readOnly": True,
		"visible": True,
		"multiple": False,
	},
	{
		"required": True,
		"readOnly": True,
		"visible": True,
		"multiple": False,
	},
	{
		"required": False,
		"readOnly": False,
		"visible": False,
		"multiple": True,
	},
	{
		"required": True,
		"readOnly": False,
		"visible": False,
		"multiple": True,
	},
	{
		"required": False,
		"readOnly": True,
		"visible": False,
		"multiple": True,
	},
	{
		"required": False,
		"readOnly": False,
		"visible": True,
		"multiple": True,
	},
	{
		"required": True,
		"readOnly": True,
		"visible": False,
		"multiple": True,
	},
	{
		"required": True,
		"readOnly": False,
		"visible": True,
		"multiple": True,
	},
	{
		"required": False,
		"readOnly": True,
		"visible": True,
		"multiple": True,
	},
	{
		"required": True,
		"readOnly": True,
		"visible": True,
		"multiple": True,
	},
]

bonesToTest = [
	# (baseBone, [], {}),
	(booleanBone, [], {}),
	# (captchaBone, [], {"privateKey": "foo", "publicKey": "bar"}),
	# (colorBone, [], {}),
	# (credentialBone, [], {}),
	# (dateBone, [], {}),
	# (emailBone, [], {}),
	# (fileBone, [], {}),
	# (keyBone, [], {}),
	(numericBone, [], {}),
	# (passwordBone, [], {}),
	# (randomSliceBone, [], {}),
	# (recordBone, [], {"using": CoordRelSkel, "format": "$(lat) - $(lng)"}),
	# (relationalBone, [], {"module": "feedentry", "kind": "feedentry"}),
	# (selectBone, [], {"values": {"true": "Option A", "false": "Option B"}}),
	# (selectCountryBone, [], {}),
	# (spatialBone, [(50, 57), (7, 0), (10, 10)], {}),
	(stringBone, [], {}),
	# (treeLeafBone,  [], {"module": "file", "kind": "file"}),
	# (treeNodeBone,  [], {"module": "file", "kind": "file"}),
	# (userBone, [], {}),
]


class AllBones(List):
	pass

# 	def addSkel(self, *args, **kwargs):
# 		skel = super().addSkel()
# 		count = 0
# 		for testBone, extraArgs, extraKwargs in bonesToTest:
# 			for flagCombination in flags:
# 				mergedArgs = flagCombination.copy()
# 				mergedArgs["extra"] = "_".join(map(str, extraKwargs.values()))
# 				mergedArgs["params"] = {"tooltip": json.dumps(mergedArgs, indent=4)}
# 				boneName = urllib.parse.quote_plus("{}_{}_{}_{}_{}_{}".format(testBone.__name__, *mergedArgs.values()))
# 				logging.debug("boneName: %r, %r, %r, %r, %r", count, testBone, boneName, flagCombination, extraKwargs)
# 				try:
# 					skel.__setattr__(
# 						boneName,
# 						testBone(*extraArgs, descr=boneName, **flagCombination, **extraKwargs)
# 					)
# 					count += 1
# 				except Exception as err:
# 					logging.exception(err)
# 		return skel
#
# 	viewSkel = addSkel
# 	editSkel = addSkel
#
