weight=float(input("Enter your weight:"))
unit=input("Enter 'kilogram' or 'pounds'?(k or L): ")
if(unit=="k"):
    weight=round(weight*2.20462,2)
    unit="Lbs"
    print(f"Your weight is {weight} {unit}")
elif(unit=="L"):
    weight=round(weight/2.20462,2)
    unit="Kgs"
    print(f"Your weight is {weight} {unit}")
else:
    print(f"{unit} is not valid")



