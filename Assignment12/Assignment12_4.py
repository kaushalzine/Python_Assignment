import os
import time
import psutil
from urllib.request import urlopen 
import schedule
from sys import *;
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart



def is_connected():
	try:
		urlopen('http://216.58.192.142',timeout=1)
		print("Connect ")

		return True
	except Exception:
		return False



def mailsender(filename,user,u_pass):
	
	
	
	

	try:
		
		
		sent_from=user
		to=['kaushalzine600@gmail.com']
		msg=MIMEMultipart()
		msg['From']=sent_from
		msg['To']=to
		body=""" Hello King Sysytem """	
		subject=""" The mail send..."""
		msg['Subject']=subject
		
		msg.attach(MIMEText(body,'plain'))
		attachment=open(filename,"rb")

		p=MIMEBase('application','octet-strem')
		p.set_payload((attachment).read())
		encoders.encode_base64(p)
		p.add_header('Content-Disposition',"attachment;filename=%s"% filename)
		msg.attach(p)

		server=smtplib.SMTP('smtp.gmail.com',587)
		server.starttls()
		server.login(user,u_pass)

		text=msg.as_string()
		server.sendmail(sent_from,to,text)
		server.close()
		print("mail send sussessfull")

	except Exception as E:
		print("Unamvble to send mail",E)


def processdisplay(path):

	if not os.path.exists(path):
		os.mkdir(path)
	filename=os.path.join(path,'ProcessDisplay%s.txt'%time.time())


	print("Inside method")
	processlist=[]
	file=open(filename,'w')
	print("Data File print process")
	for proc in psutil.process_iter():

		try:
			
			file.write(str(proc));

		except(Exception):

			pass
	return processlist	

def main():
	print("mail send System")

	path=argv[1]
	processlist=processdisplay(path)
	try:
		user='kaushalzine1@gmail.com'
		u_pass='8149214033'
		connected=is_connected()
		print(connected)

		if connected:
			mailsender(processlist,user,u_pass)

		else :
			print("No Connection ")
	
	except Exception:
		print("main Exception",E)			

if __name__=="__main__":
	main()





