#!/bin/sh
set -ex
project=$1

if [ -z "$project" ]
then
	echo "Usage: $0 PROJECT_ID"
	exit 1
fi

gcloud app create --project=$project --region=europe-west3

for role in roles/editor roles/iam.serviceAccountTokenCreator roles/storage.objectAdmin
do
	gcloud projects add-iam-policy-binding $project --member serviceAccount:$project@appspot.gserviceaccount.com --role $role

	if [ $? -ne 0 ]
	then
		exit $?
	fi
done

gcloud iam service-accounts keys create deploy/store_credentials.json --iam-account=$project@appspot.gserviceaccount.com

gcloud services enable --project=$project cloudtasks.googleapis.com

pushd deploy
for yaml in cron.yaml queue.yaml index.yaml
do
	gcloud app deploy -q --project=$project queue.yaml
done

echo
echo "--- Project Setup Done ---"
echo
