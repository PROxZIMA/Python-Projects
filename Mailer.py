import smtplib

def send_mail():	
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	
	your_mailaddr = input("Mention you Email address : ", )
	your_app_password = input(f"What's the app password for the Email address {your_mailaddr} ?", )
	server.login(your_mailaddr, your_app_password)
	print("Mail logged in!")
	to_addr = input("Whome do you want to send it to? ", )
	msg=str(99*'error 404 ')
	n=int(input('Enter a number : '))
	for i in range (n,0,-1):
		server.sendmail(your_mailaddr, to_addr, msg)
		print("Mail has been sent")
	server.quit()
	print("Server quitting now!")

send_mail()