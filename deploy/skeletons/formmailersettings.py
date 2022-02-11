from viur.core.bones import *
from viur.core.skeleton import Skeleton


class FormmailersettingsSkel(Skeleton):

	# Formmailer
	formmailer_recipients = emailBone(
		descr="Recipient for contactmailer",
		params={"category": "Formmailer"},
		required=True,
		multiple=True
	)
