import os
from PIL import Image, ImageGrab
import getpass
import time

directory = "C:/Users/" + getpass.getuser() + "/AppData/Local/" + "CatchThelsSoftware/"

def getScreenshot():
	img = ImageGrab.grab()
	img.save(directory + "screenshot.jpg")

def createLoggingDirectory():
	if os.path.exists(directory):
		pass
	else:
		os.mkdir(directory)