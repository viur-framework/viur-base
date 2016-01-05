# -*- coding: utf-8 -*-
import sys, os, datetime, binascii

cwd = os.getcwd()
dirs = []
files = {}

for dirname, dirnames, filenames in os.walk("."):
	if dirname == ".":
		for ignore in [".idea", ".git", "server"]:
			if ignore in dirnames:
				dirnames.remove(ignore)

		for ignore in ["README.md", "make_setup.py"]:
			if ignore in filenames:
				filenames.remove(ignore)

		dirname = ""
	elif dirname.startswith("./"):
		dirname = dirname[2:]

	for dir in dirnames:
		dirs.append(((dirname + "/") if dirname else "") + dir)

	for file in filenames:
		filename = ((dirname + "/") if dirname else "") + file
		f = open(filename, "rb")
		files[filename] = binascii.hexlify(f.read())
		f.close()

out = ""
out += "# -*- coding: utf-8 -*-\n"
out += "# THIS FILE WAS GENERATED WITH %s ON %s\n" % (__file__, str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
out += "# DO NOT MODIFY THIS FILE PERMANENTLY - IT WILL GO AWAY!\n\n"

out += "import os, sys\n\n"

out += "dirs = %s\n" % dirs
out += "files = %s\n\n" % files

out += """

cwd = os.getcwd()
prgc = sys.argv[0]

if prgc.startswith("/") or prgc[1]==":":
    path = os.path.dirname( prgc )
else:
    path = os.path.abspath( os.path.dirname( os.path.join( cwd, prgc ) ) )

path = os.path.abspath( os.path.join( path , ".." ) )
os.chdir( path )
appid = path[ path.rfind( os.path.sep )+1: ].strip()

print("This will initialize the application %s in %s.\\nContinue [y/n]?" % (appid, path) )
try:
	answ = raw_input()
except NameError:
	answ = input()

if not answ.lower() in ["y","yes"]:
    sys.exit(0)

for folder in dirs:
	folder = os.path.join(path, *folder.split("/"))
	if not os.path.exists(folder):
		print("Creating %s..." % folder)
		os.mkdir(folder)

for name, content in files.items():
	print("Writing %s..." % name)
	content = content.decode("hex")
	open(name, "w+").write(content)

"""

print(out)
