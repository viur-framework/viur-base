#!/bin/sh
PROJECT_ID="{{app_id}} "

which app_server >/dev/null 2>&1
if [ $? -ne 0 ]
then
	dev_appserver.py -A $PROJECT_ID $* deploy
else
	app_server -A $PROJECT_ID $* deploy
fi
