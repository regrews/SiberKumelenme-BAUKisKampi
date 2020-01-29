# -*- coding: utf-8 -*-
import requests
import hashlib

def getMd5sum(TEXT):
	return hashlib.md5(TEXT.encode('utf-8')).hexdigest()


def getPage(URL):
	req = requests.get(URL)
	istenilen=parseText(req.text)
	return istenilen, req.cookies

def parseText(FULL_TEXT):
	HINT_STR="<h1 align='center'>MD5 encrypt this string</h1><h3 align='center'>"
	TEXT=FULL_TEXT.split("\n")
	temp=""
	for satir in TEXT:
		if HINT_STR in satir:
			temp=satir
		token=temp.replace(HINT_STR,"")
		token=token.split("</h3>")
		final=token[0]
	return final
def postString(URL,STRING,COOKIES):
	ERR_STR="Too slow!"
	DATA={"hash":STRING}
	post_request=requests.post(URL,cookies=COOKIES,data=DATA)
	if ERR_STR not in post_request.text:
		print(post_request.text)

if __name__ == '__main__':
	while True:
		URL=""
		gerekli_string, verilenCookie=getPage(URL)
		postString(URL, getMd5sum(gerekli_string), verilenCookie)