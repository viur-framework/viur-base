# {{app_id}}

Created by {{whoami}}.

https://{{app_id}}.appspot.com


## Description

This is {{app_id}}. It is an absolutely nice project written in the powerful ViUR 3 framework.


## First time project setup

The following steps are necessary to setup this project appropriately.

1. Create a new Google Cloud project named `{{app_id}}` at https://console.cloud.google.com/projectcreate
2. Run `./viur-gcloud-setup.sh {{app_id}}`
3. Once, run `pipenv install --dev` to install a local development environment


After that, you always can locally fire-up your new ViUR project with `pipenv run viur run`.

To deploy your project, use `pipenv run viur deploy app`, with additional options.


## Contact

Contact @{{whoami}} for help and support.
