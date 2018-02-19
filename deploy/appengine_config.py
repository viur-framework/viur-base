# appengine_config.py
from google.appengine.ext import vendor
import logging

# Add any libraries install in the "lib" folder.
try:
	vendor.add("lib")
except Exception as err:
	logging.exception(err)

