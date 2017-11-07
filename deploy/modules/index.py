# -*- coding: utf-8 -*-
from server import tasks, exposed
from server.render.html import default
import logging

class index(default):

	@exposed
	def index(self, *args, **kwargs):
		template = self.getEnv().get_template("index.html")
		return template.render(start=True)

	#@tasks.PeriodicTask(24*60)
	def backup(self, *args, **kwargs):
		"""
		Backup job kick-off for Google App Engine datastore admin.

		Enable it on production systems when necessary enabling and pre-configuration is done.
		You need to enable GAE datastore admin, initialize a GCS bucket for your app and install
		another queue specified in queue.yaml to get this run. This is done using

		``` gcloud app deploy -q --project=YOUR-PROJECT queue.yaml

		Then, uncomment above decorator.
		"""
		from google.appengine.ext.db.metadata import Kind
		from google.appengine.api.app_identity import get_application_id
		from google.appengine.api import taskqueue

		appname = get_application_id()
		kinds = []

		q = Kind.all()
		for kind in q.fetch(100):
			kindName = kind.kind_name

			if kindName in ["SharedConfData"] or kindName.startswith("_"):
				continue

			kinds.append(kindName)
			logging.debug("Adding kind '%s' to backup" % kindName)

		taskqueue.add(
			url="/_ah/datastore_admin/backup.create",
			method="GET",
			queue_name="data-backup",
			params={
				"name": "daily_backup", #No ending "_" accepted here, this causes error 400????
				"filesystem": "gs",
				"gs_bucket_name": "%s.appspot.com/backup" % appname,
				"kind": kinds
			}
		)

		logging.info("Daily backup queued for %s" % ", ".join(kinds))

index.html = True
