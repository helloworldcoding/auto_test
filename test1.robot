
*** Variables ***
${var1}		value1
${tup1}		${1,3}
@{list1}	12   23   34
&{dict1}	key1=val1	name=zhangsan	age=12


*** Test Cases ***

First Case
	Log	Hello world!	warn

Second Case
	${res}	Evaluate	1+2+3
	Should Be Equal		${res}		${6}

Third Case
	${res}	Evaluate	'i'*3
	Length Should Be	${res}	3

Case4
	#string
	${str}	set variable	test1_string
	#tuple
	${tuple}	set variable	${1,"tuple1"}
	@{list2} 	Create List	1	3	"adfa"
	&{D1}	Create Dictionary	name=zhangsan	age=12	

	Log to console	${str}	
	Log to console	${tuple}	warn
	Log to console	${list2}
	Log to console	${D1}
	
