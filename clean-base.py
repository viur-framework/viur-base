#!/bin/sh
# using the following stackoverflow answer to determine where /usr/bin/python points to
# https://stackoverflow.com/questions/18993438/shebang-env-preferred-python-version
''''which python2 >/dev/null 2>&1 && exec python2 "$0" "$@" # '''
''''which python  >/dev/null 2>&1 && exec python  "$0" "$@" # '''
''''exec echo "Error: I can't find python anywhere"         # '''
import sys, os, subprocess, time, datetime, getpass, argparse, urllib, zipfile

try:
	whoami = getpass.getuser()
except:
	whoami = "viur"

ap = argparse.ArgumentParser(
		description="Setting up a clean ViUR project base.",
		epilog="The script runs interactively if not command-line arguments are passed.")

ap.add_argument("-A", "--app_id", type=str, help="The application-id that should be replaced in the arbitrary places.")
ap.add_argument("-a", "--author", type=str, default=whoami, help="The author's name that is placed in arbitrary places.")

args = ap.parse_args()

app_id = args.app_id
whoami = args.author

if args.app_id is None:
	prompt = "Enter Author Name (leave empty to default to %s): " % whoami
	try:
		name = raw_input(prompt)
	except NameError:
		name = input(prompt)

	if name:
		whoami = name

	app_id = os.path.split(os.getcwd())[-1]

	if not app_id.endswith("-viur"):
		app_id += "-viur"

	prompt = "Enter application-id (leave empty to default to %s): " % app_id

	try:
		name = raw_input(prompt)
	except NameError:
		name = input(prompt)

	if name:
		app_id = name

time = time.time()
timestamp = datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')

workdir = os.getcwd()+"/deploy"
file_list = ["viur-project.md", "local_run.sh"]
replacements = {"{{app_id}}":app_id, "{{whoami}}":whoami, "{{timestamp}}":timestamp}

# Build file list in which to search for placeholders to replace

for subdir, dirs, files in os.walk("."):
	for file in files:
		filepath = subdir + os.sep + file

		if any([filepath.endswith(ext) for ext in [".py", ".yaml", ".html", ".md", ".sh", ".json", ".js", ".less"]]):
			file_list.append(filepath)

# Replace placeholders with values entered by user or defaults

for file_obj in file_list:
	lines = []
	with open(file_obj) as infile:
		for line in infile:
			for src, target in replacements.items():
				line = line.replace(src, target)
			lines.append(line)
	with open(file_obj, 'w') as outfile:
		for line in lines:
			outfile.write(line)

# Update submodules

if os.path.exists(".git"):
	print("Downloading submodules")
	subprocess.check_output('git submodule init', shell=True)
	subprocess.check_output('git submodule update', shell=True)
	subprocess.check_output('cd vi && git submodule init && git submodule update', shell=True)
	print("Removing .git tether")
	try:
		subprocess.check_output('git remote rm origin', shell=True)
		print(".git remote tether removed")
	except:
		pass
else:
	print(".git tether already removed")

# Install latest built of vi

zipname = "vi.zip"

sys.stdout.write("Downloading latest build of vi...")
urllib.urlretrieve("https://www.viur.dev/package/download/vi/latest", zipname)
print("Done downloading latest build of vi")

sys.stdout.write("Extracting latest build of vi...")

zip = zipfile.ZipFile(zipname, "r")
zip.extractall('deploy/')
zip.close()

os.remove(zipname)

print("Done extracting vi")

# Rename viur project
orig = os.path.join(workdir, "viur-project.py")
newname = os.path.join(workdir, app_id+".py")
os.rename(orig, newname)

# Add newly renamed viur-project.py to local git
subprocess.check_output('git add '+ newname, shell=True)

# Create a README.md
os.remove("README.md")  # this is needed because on windows os.rename will fail caused by existing dest!!!
os.rename("viur-project.md", "README.md")

# Remove yourself!
os.remove(sys.argv[0])
