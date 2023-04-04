#    TAKING THE INPUTS 
month=int(input("enter the month in numeric form :"))
day=int(input("enter the day in numeric form :"))
year=int(input("enter the year as two numerical digits :"))

if month in range(0,13):
    # print("Success: congratulations! you have entered the correct date ")
    pass
else:
    print("Error: Invalid month input")
    exit(1)
    
if day in range(0,31):
    # print("Success: congratulations! you have entered the correct date")
    pass
else:
    print("Error: Invalid day input")
    exit(1)
    
if year in range(0,100):
    # print("Success: congratulations! you have entered the correct date ")
    pass
else:
    print("Error: Invalid year input")
    exit(1)
    
print("Success: congratulations! you have entered the correct date ")
print("the date is : "+ str(month)+"/"+ str(day)+"/"+ str(year))




