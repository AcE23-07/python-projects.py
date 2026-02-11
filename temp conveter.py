#temprature converter from celsius to fahrenheit and vice-versa
Temprature=float(input("Enter temprature  "))
unit=input("in 'celsius'or 'fehrenheit':(C or F)")
if(unit=="C"):
    Temprature= round((Temprature*1.8)+32,2)
    unit=  "*F"
    print(f"Temprature is {Temprature}{unit}")
elif(unit=="F"):
    Temprature=round((Temprature-32)/1.8)
    unit= "*C"
    print(f"Temprature is {Temprature}{unit}")
else:
    print(f"{unit} is not valid")