#!/bin/sh
cd deploy
dev_appserver.py -A {{app_id}} --log_level=debug .
