*** Settings ***
Resource	../global.resource
Suit setup	 Run keywords	${parent setup} 	AND		Get User Info   12


*** Test Cases ***
Check User
	MyLog	check user
Add User
	MyLog	new user


*** Keywords ***
Get User Info
	[Documents]		get user infomation
	[Arguments]		${id}
	MyLog	user id is ${id}
