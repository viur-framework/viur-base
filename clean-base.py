#!/usr/bin/env python3
import argparse
import datetime
import getpass
import os
import subprocess
import sys


try:
    whoami = getpass.getuser()
except Exception:
    whoami = "viur"

ap = argparse.ArgumentParser(
    description="Setting up a clean ViUR project base.",
    epilog="The script runs interactively if not command-line arguments are passed."
)
ap.add_argument(
    "-A",
    "--app_id",
    type=str,
    help="The application-id that should be replaced in the arbitrary places."
)
ap.add_argument(
    "-a",
    "--author",
    type=str,
    default=whoami,
    help="The author's name that is placed in arbitrary places."
)
ap.add_argument(
    "-c",
    "--clean-history",
    action="store_true",
    default=True,
    help="Clean the git history."
)
args = ap.parse_args()
app_id = args.app_id
whoami = args.author
clean_history = args.clean_history
update = False  # this might be changed by command-line flag later on

if args.app_id is None:
    prompt = input(f"Enter author name (leave empty to default to {whoami}): ")

    if prompt:
        whoami = prompt

    app_id = os.path.split(os.getcwd())[-1]

    prompt = input(f"Enter application-id (leave empty to default to {app_id}): ")

    if prompt:
        app_id = prompt

    while (prompt := input("Do you want to clean the git history? [Y/n] ").lower().strip()) not in {"", "y", "n"}:
        print(f'Invalid option "{prompt}". "y", "n" or empty input expected.')

    clean_history = prompt != "n"

timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

workdir = os.getcwd() + "/deploy"
file_list = ["viur-project.md"]
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

if clean_history and os.path.exists(".git"):
    print("Cleaning git history")
    subprocess.check_output("git checkout --orphan main_tmp", shell=True)
    print(subprocess.check_output("git branch -D main", shell=True).decode().rstrip("\n"))
    subprocess.check_output("git branch -m main", shell=True)
    print(
        "Current branch is:",
        subprocess.check_output("git branch --show-current", shell=True)
        .decode().rstrip("\n")
    )
    print("---")

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
print("#                                                            #")
print("# Next run                                                   #")
print("#                                                            #")
print("#     pipenv install --dev                                   #")
print("#     pipenv run viur build release                          #")
print("#                                                            #")
print("# Afterwards, run                                            #")
print("#                                                            #")
print("#     ./viur-gcloud-setup.sh                                 #")
print("#                                                            #")
print("##############################################################")
