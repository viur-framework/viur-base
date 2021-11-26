#!/bin/bash
# fixme: This shell script becomes part of viur-cli soon.

# Steps for setting up:
# 1. Create a bucket named "backup-dot-YOUR-APPID" in Google Cloud Storage
# 2. Set the following permissions on Google Cloud Console IAM
# 	(https://console.cloud.google.com/iam-admin/iam) for the user YOUR-APPID@appspot.gserviceaccount.com:
#
# 	- Datastore > Cloud Datastore Import Export Admin
# 	- Storage > Storage Admin
#
#    (see screenshot here: https://docs.viur.is/images/backup-settings.png)
#
# Note: This will only work on App Engine projects that are associated with a billing account.

project=$1

if [ -z "$project" ]
then
  echo "Usage: $0 PROJECT_ID"
  exit 1
fi

# Create a bucket
gsutil mb -l EUROPE-WEST3 -p $project gs://backup-dot-$project
if [ $? -ne 0 ]
then
  exit 1
fi

set -ex

# Configure service account and IAM policies
for role in roles/storage.admin roles/datastore.importExportAdmin
do
  gcloud projects add-iam-policy-binding $project --member serviceAccount:$project@appspot.gserviceaccount.com --role $role
done

set +ex

echo "Done!"
