# {{app_id}}

Created by {{whoami}}.

https://{{app_id}}.appspot.com

## Description

This is {{app_id}}.

## Build the Vi

To build the Vi, run

```bash
$ cd vi
$ make deploy
```

## Change Git origin URL

Please set another Git repository origin. The default viur-base origin has been automatically deleted by ``clean-base.py``, for security reasons.

```bash
$ git remote add git@github.com:{{whoami}}/{{app_id}}.git
```

## Project setup

1. Create new project `{{app_id}}` at https://console.cloud.google.com/projectcreate
2. Create a new service account at https://console.cloud.google.com/iam-admin/serviceaccounts/create?project={{app_id}} and store the credentials JSON-file into `deploy/store_credentials.json`. The service account is named `{{app_id}}@{{app_id}}.iam.gserviceaccount.com` by default, which is fine.
3. Set up Google Cloud Datastore database at https://console.cloud.google.com/datastore/setup?project={{app_id}}
4. Enable Cloud Tasks API at `https://console.developers.google.com/apis/api/cloudtasks.googleapis.com/overview?project={{app_id}}`
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
