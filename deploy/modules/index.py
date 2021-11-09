import datetime, logging

from viur.core import utils, tasks, conf, errors, exposed
from viur.core.prototypes import BasicApplication
from viur.core.utils import currentRequest

from google.cloud.datastore_admin_v1.services.datastore_admin.client import DatastoreAdminClient


class Index(BasicApplication):

	@exposed
	def index(self, *args, **kwargs):
		"""
		The first two lines of code here ensure that requesting a non-existent module or template will throw a 404
		instead of referring to index. Remove them if you wish to alter this behaviour.
		"""
		if len(args) > 1 or kwargs:
			raise errors.NotFound()

		template = self.render.getEnv().get_template("index.html")
		return template.render(start=True)

	@exposed
	def sitemap_xml(self, *args, **kwargs):
		currentRequest.get().response.headers["Content-Type"] = "text/xml"
		return self.render.view({}, tpl="sitemap")

	# @tasks.PeriodicTask(24 * 60)
	def backup(self, *args, **kwargs):
		"""
		Backup job kick-off for Google Cloud Storage.
		Use the maintenance script setup/enable-backup.sh to configure your project for backups.
		"""
		if utils.isLocalDevelopmentServer:
			logging.info("Backup tool is disabled on local development server")
			return

		bucket = "backup-dot-%s" % utils.projectID
		admin_client = DatastoreAdminClient()
		timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

		output_url_prefix = "gs://%s/%s" % (bucket, timestamp)

		admin_client.export_entities(
			project_id=utils.projectID,
			output_url_prefix=output_url_prefix
		)

		logging.info("Backup queued to be exported to %r", output_url_prefix)
