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

def check_symmetry(param):
	size = len(param)
	#check lenth is odd or even

	if size%2:
		mid=size//2 +1
	else:
		mid=size//2

	start1=0
	start2=mid
	flag=0

	while(start1<mid and start2<size):
		if(param[start1]==param[start2]):
			start1 =start1+1
			start2 = start2+1
		else:
			flag=1
			break;
	if flag==0:
		return f"String is symmetric"
	else:
		return f"String is asymmetric"

	

print(check_palindrom(str_input))
print(check_symmetry(str_input))