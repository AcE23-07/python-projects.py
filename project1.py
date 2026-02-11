#simple calulcator using if-else(conditional -statement) and arthimatic operator.
operator=input("enter your operator(+,-,*,/,//,**,%)")
num1=float(input("enter your 1st number"))
num2=float(input("enter your 2nd number"))
if(operator=="+"):
    result=num1+num2
    print(round(result,3))
elif(operator=="-"):
    result=num1-num2 
    print(round(result,3))
elif(operator=="*"):
    result=num1*num2
    print(round(result,3))
elif(operator=="/"):
    result=num1/num2 
    print(round(result,3))
elif(operator=="%"):
    result=num1%num2
    print(round(result,3))
elif(operator=="//"):
    result=num1//num2 
    print(round(result,3))
elif(operator=="**"):
    result=num1**num2
    print(round(result,3))
else:
    print(f"{operator} is not valid operator")                                                