import zipfile
from modules import otherlogging
import os
import getpass
import shutil

def createZipFile(name):
	zipFile = zipfile.ZipFile("C:/Users/" + getpass.getuser() + "/AppData/Local/" + name, 'w', zipfile.ZIP_DEFLATED)
	for files in os.listdir(otherlogging.directory):
		zipFile.write(otherlogging.directory + files)
	zipFile.close()

def removeFile(path):
	os.remove(path)

def copyFile(path, end_path):
	shutil.copyfile(path, end_path, follow_symlinks=True)