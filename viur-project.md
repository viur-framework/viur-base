# {{app_id}}

Created by {{whoami}}.

https://{{app_id}}.appspot.com

## Description

This is {{app_id}}. It is an absolutely nice project written in the powerful ViUR 3 framework.

## Project setup

The following steps are necessary to setup this project appropriately.

1. Create a new Google Cloud project named `{{app_id}}` at https://console.cloud.google.com/projectcreate
2. Create a new service account at https://console.cloud.google.com/iam-admin/serviceaccounts/create?project={{app_id}} and store the credentials JSON-file into `deploy/store_credentials.json`. The service account is named `{{app_id}}@{{app_id}}.iam.gserviceaccount.com` by default, which is fine.
3. Set up Google Cloud Datastore database at https://console.cloud.google.com/datastore/setup?project={{app_id}}
4. Enable Cloud Tasks API at https://console.developers.google.com/apis/api/cloudtasks.googleapis.com/overview?project={{app_id}}
5. Deploy task queue settings using `gcloud app deploy -q --project={{app_id}} --version=`date +"%Y-%m-%d"-jm` queue.yaml`


Now you can locally fire-up your new ViUR project with `./local_run.sh`, or deploy your app to Google App Engine.

## Deploy to GAE

Deployment is performed using the gcloud SDK:

```bash
$ cd deploy

# Deploy to dev
$ gcloud app deploy --no-promote -q --project={{app_id}} --version=$USER-dev

# Deploy to live (beware!)
$ gcloud app deploy -q --project={{app_id}} --version=`date +"%Y-%m-%d"-$USER`
```

## Contact

Contact @{{whoami}} for help and support.
