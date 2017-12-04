# {{app_id}}

Created by {{whoami}}.

https://{{app_id}}.appspot.com

## Description

This is {{app_id}}.

## Prerequisites

To install prerequisites, do

	pip2 install -t appengine/lib -r requirements.txt --upgrade

## Run local development version

To locally run, do

	./local_run.sh

or manually, do

	cd deploy
	dev_appserver.py -A {{app_id}} --log_level=debug .

## Deploy to GAE

Deployment is performed using the gcloud SDK:

	cd deploy

	# Deploy to dev
	gcloud app deploy --no-promote -q --project={{app_id}} --version=$USER-dev

	# Deploy to live (beware!)
	gcloud app deploy -q --project={{app_id}} --version=`date +"%Y-%m-%d"-$USER`

## Contact

- @{{whoami}}
