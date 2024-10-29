# {{app_id}}

Created by {{whoami}}.

https://{{app_id}}.appspot.com


## Description

This is {{app_id}}. It is an absolutely nice project doing something, and is written using the ViUR framework.


## First time project setup

The following steps are necessary to setup this project appropriately.

1. Create a new Google Cloud project named `{{app_id}}` at https://console.cloud.google.com/projectcreate
2. Run `./viur-gcloud-setup.sh {{app_id}}`
3. Once, run `pipenv install --dev` to install a local development environment


After that, you always can locally fire-up your new ViUR project with `pipenv run viur run`.

To deploy your project, use `pipenv run viur deploy app`, with additional options.

## Setting up Google Login

1. https://console.cloud.google.com/apis/credentials/consent?project={{app_id}}
2. Internal -> Create
3. App name: "{{app_id}}" or your project's name
4. User-support email (your Gcloud account mail)
5. Authorized domain 1: {{app_id}}.appspot.com
6. Developer contact: (you contact mail)
7. Save & continue
8. https://console.cloud.google.com/apis/credentials/oauthclient?project={{app_id}}
9. "Web Application" - "Web client 1"
10. Configure authorized JavaScript origins
  - https://{{app_id}}.appspot.com
  - http://localhost:8080
  - http://localhost:8081 (for VueJS development)
  - http://localhost:8082 (for VueJS development)
  - http://localhost
11. Configure authorized redirect URIs
  - https://{{app_id}}.appspot.com
  - http://localhost:8080
  - http://localhost:8081 (for VueJS development)
  - http://localhost:8082 (for VueJS development)
  - http://localhost
12. Create
13. Copy the client id and assign it to `conf.user.google_client_id` in `main.py` or,
    when you have multiple projects with the same code-base, you can also store this client id as a secret value and use the same
    identifier. To do this, follow these steps:
    - https://console.cloud.google.com/security/secret-manager/create?project={{app_id}}
    - Name: google-clientid
    - Paste copyied client id and set `conf.user.google_client_id = secret.get("google-clientid")` in your `main.py`
14. Optionally set `conf.user.google_gsuite_domains` to authorized Gsuite domains that allow for User registration in your project

## Contact

Contact @{{whoami}} for help and support.
