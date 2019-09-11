*** Settings ***
Resource	../global.resource
Suit setup		User setup

*** Keywords ***
User setup
	Run Keyword If 	${parent setup} == ${EMPTY}    Set parent init

Set parent init
	Set global variable     ${parent setup} 	 Init function

