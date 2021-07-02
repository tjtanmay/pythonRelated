str_input=input("String to Check:\n")

def check_palindrom(param):
	mid=(len(param)-1)//2
	start=0
	last=len(param)-1
	flag=0
	while(start<mid):
		if(param[start]==param[last]):
			start +=1
			last -=1
		else:
			flag=1
			break;

	if flag==1:
		return f"string is not a palindrom"
	else:
		return f"string is palindrom"

print(check_palindrom(str_input))