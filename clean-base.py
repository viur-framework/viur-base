import sys, os, subprocess, time, datetime
from sys import argv

whoami = raw_input("Enter Author Name: ")
appid = raw_input("Enter desired app_id: ")
time = time.time()
timestamp = datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')

workdir = os.getcwd()+"/deploy"
file_list = []
replacements = {"{{app_id}}":appid, "{{whoami}}":whoami, "{{timestamp}}":timestamp}
if os.path.exists(".git"):
	print("Downloading submodules")
	subprocess.check_output('git submodule init', shell=True)
	subprocess.check_output('git submodule update', shell=True)
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
