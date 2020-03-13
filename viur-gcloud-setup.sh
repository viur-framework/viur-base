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
done

gcloud iam service-accounts keys create deploy/store_credentials.json --iam-account=$project@appspot.gserviceaccount.com

gcloud services enable --project=$project cloudtasks.googleapis.com

# Google Cloud Storage

gsutil uniformbucketlevelaccess set on gs://$project.appspot.com/ 

cat <<ENDL >cors$$.json
[
    {
      "origin": [
	  	"https://$project.appspot.com",
		"http://localhost:8080",
		"http://127.0.0.1:8080"
		],
      "method": ["GET", "HEAD", "DELETE", "POST", "OPTIONS"],
	  "responseHeader": [
        "Content-Type",
        "Access-Control-Allow-Origin",
        "x-goog-resumable"],
      "maxAgeSeconds": 3600
    }
]
ENDL

gsutil cors set cors$$.json gs://$project.appspot.com
rm cors$$.json

# Deploy

pushd deploy
for yaml in cron.yaml queue.yaml index.yaml
do
	gcloud app deploy -q --project=$project $yaml
done

echo
echo "--- Project Setup Done ---"
echo
