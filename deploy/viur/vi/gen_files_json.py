import os, json

roots = ["vi", "vi_plugins"]

files = []

for r in roots:
	walkObj = os.walk(r)
	for root, dirnames, filenames in walkObj:
		for file in filenames:
			if file.endswith(".py") and not "(" in file:
				files.append(os.path.join(root, file))
				print("'%s',"%os.path.join(root,file))

with open("files.json", "w") as f:
	json.dump(files, f, indent=2)
