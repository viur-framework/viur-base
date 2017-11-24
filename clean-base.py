#!/usr/bin/env python
import sys, os, subprocess, time, datetime, getpass, argparse
from sys import argv

try:
	whoami = getpass.getuser()
except:
	whoami = "Bernd"

ap = argparse.ArgumentParser(
		description="Setting up a clean ViUR project base.",
		epilog="The script runs interactively if not command-line arguments are passed.")

ap.add_argument("-A", "--app_id", type=str, help="The application-id that should be replaced in the arbitrary places.")
ap.add_argument("-a", "--author", type=str, default=whoami, help="The author's name that is placed in arbitrary places.")

args = ap.parse_args()

appid = args.app_id
whoami = args.author

if args.app_id is None:
	try:
		prompt = "Enter Author Name (leave empty to default to %s): " % getpass.getuser()
		whoami = raw_input(prompt)
		if whoami == "":
			whoami = getpass.getuser()
	except:
		whoami = raw_input("Enter Author Name: ")
	while True:
		appid = raw_input("Enter desired app_id: ")
		if appid != "":
			break

time = time.time()
timestamp = datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')

workdir = os.getcwd()+"/deploy"
file_list = []
replacements = {"{{app_id}}":appid, "{{whoami}}":whoami, "{{timestamp}}":timestamp}
if os.path.exists(".git"):
	print("Downloading submodules")
	subprocess.check_output('git submodule init', shell=True)
	subprocess.check_output('git submodule update', shell=True)
	subprocess.check_output('cd vi && git submodule init && git submodule update', shell=True)
	print("Removing .git tether")
	try:
		subprocess.check_output('git remote rm origin', shell=True)
	except:
		pass
else:
	print(".git tether already removed")

for subdir, dirs, files in os.walk(workdir):
	for file in files:
		filepath = subdir + os.sep + file

		if filepath.endswith(".py") or filepath.endswith(".yaml") or filepath.endswith(".html"):
			file_list.append(filepath)
#print (file_list)

for file_obj in file_list:
	lines = []
	with open(file_obj) as infile:
		for line in infile:
			for src, target in replacements.iteritems():
				line = line.replace(src, target)
			lines.append(line)
	with open(file_obj, 'w') as outfile:
		for line in lines:
			outfile.write(line)

orig = os.path.join(workdir, "viur_server.py")
newname = os.path.join(workdir, appid+".py")
os.rename(orig, newname)
os.remove(argv[0])
