#!/usr/bin/python
import os, sys, subprocess
from os.path import join

# Define folders which should be included
target_folders = [ "materials", "models", "particles", "scenes", "media", "scripts", "shadereditorui", "shaders", "sound", "resource"
# Define file types which should be included
file_types = [ "vmt", "vtf", "vbf", "mdl", "phy", "vtx", "vvd", "pcf", "vcd" , "txt", "res", "lst", "raw", "gam", "ttf", "dump", "vcs", "pcf", "bik", "wav", "mp3", "ico", "image", "ani" ]

# Path to vpk executable
if sys.platform.startswith('linux'):
	vpk_path = "/pathto/bin/vpk_linux32"
elif sys.platform.startswith('win'):
	vpk_path = "/pathto/bin/vpk.exe"
else:
	print( "Error: unknown platform!" )

# VPK name
pak_name = "your_pack"

response_path = join(os.getcwd(), "vpk_list.txt")

out = open(response_path, 'w')
len_cd = len(os.getcwd()) + 1

for user_folder in target_folders:
	for root, dirs, files in os.walk(join(os.getcwd(), user_folder)):
		for file in files:
			if len(file_types) and file.rsplit(".")[-1] in file_types:
				if sys.platform.startswith('win'):
					out.write(os.path.join(root[len_cd:], file).replace("/", "\\") + "\n")
				else:
					out.write(os.path.join(root[len_cd:], file) + "\n")

out.close()

if sys.platform.startswith('linux'):
	os.environ['LD_LIBRARY_PATH'] = '/pathto/bin/'

subprocess.call([vpk_path, "-M", "a", pak_name, "@" + response_path])
