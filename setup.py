#!/usr/bin/env python3
import argparse, datetime, getpass, io, os, subprocess, sys, time, zipfile
from urllib.request import urlopen

try:
	whoami = getpass.getuser()
except:
	whoami = "viur"

ap = argparse.ArgumentParser(
	description="Setting up a clean ViUR project base.",
	epilog="The script runs interactively if not command-line arguments are passed."
)

ap.add_argument(
	"-A", "--app_id",
	type=str,
	help="The application-id that should be replaced in the arbitrary places."
)
ap.add_argument(
	"-a", "--author",
	type=str,
	default=whoami,
	help="The author's name that is placed in arbitrary places."
)

args = ap.parse_args()

app_id = args.app_id
whoami = args.author
update = False  # this might be changed by command-line flag later on

if args.app_id is None:
	prompt = f"Enter Author Name (leave empty to default to {whoami}): "
	name = input(prompt)

	if name:
		whoami = name

	app_id = os.path.split(os.getcwd())[-1]

	prompt = f"Enter application-id (leave empty to default to {app_id}): "
	name = input(prompt)

	if name:
		app_id = name

time = time.time()
timestamp = datetime.datetime.fromtimestamp(time).strftime("%Y-%m-%d %H:%M:%S")

workdir = os.getcwd() + "/deploy"
file_list = ["viur-project.md", "local_run.sh"]
replacements = {"{{app_id}}": app_id, "{{whoami}}": whoami, "{{timestamp}}": timestamp}

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
	with open(file_obj, "w") as outfile:
		for line in lines:
			outfile.write(line)

# Update submodules

if os.path.exists(".git"):
	print("Initializing and updating submodules")
	subprocess.check_output("git submodule update --init --recursive", shell=True)
	print("---")

	if update:
		print("Updating viur to latest master")
		subprocess.check_output(
			"cd deploy/viur && git checkout master && git pull && git submodule update --recursive",
			shell=True
		)
		print("---")

	print("Removing .git tether")
	try:
		subprocess.check_output("git remote rm origin", shell=True)
		print("---")
	except:
		pass


# Install prebuilt Vi
sys.stdout.write("Downloading latest build of viur-vi...")
zip = urlopen("https://github.com/viur-framework/viur-vi/releases/download/v3.0.3/viur-vi.zip").read()
zip = zipfile.ZipFile(io.BytesIO(zip))
zip.extractall('deploy/vi')
zip.close()
print("Done")

# commented out, we are using pyodide from cdn
# Update pyodide
# sys.stdout.write("Installing self-hosted Pyodide...")
# sys.stdout.flush()

# subprocess.check_output("./get-pyodide.py", shell=True)
# print("Done")

# Generate files

sys.stdout.write("Generating project documentation...")
sys.stdout.flush()

# Create a README.md
os.remove("README.md")  # this is needed because on windows os.rename will fail caused by existing dest!!!
os.rename("viur-project.md", "README.md")

# Remove yourself!
os.remove(sys.argv[0])

print("Done")

print("##############################################################")
print("# Well done! Project repository has been set-up now.         #")
print("# Please run ./viur-gcloud-setup.sh now as next step.        #")
print("##############################################################")
