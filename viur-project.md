# {{app_id}}

Created by {{whoami}}.

https://{{app_id}}.appspot.com

## Description

This is {{app_id}}. It is an absolutely nice project written in the powerful ViUR 3 framework.

## Project setup

The following steps are necessary to setup this project appropriately.

1. Create a new Google Cloud project named `{{app_id}}` at https://console.cloud.google.com/projectcreate
2. Run `./viur-gcloud-setup.sh {{app_id}}`


After that, you can locally fire-up your new ViUR project with `./local_run.sh`, or deploy your app to Google App Engine.

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
