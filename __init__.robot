*** Settings ***
Resource	global.resource
Suite setup 	Login admin
Suite teardown 	Logout admin

*** Keywords ***
Login admin
	Set global variable		${parent setup}		init function
	MyLog	login in admin


Logout admin
	MyLog	logout admin

