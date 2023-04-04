#     DEFINING GLOBAL VARIABLES 
uk_average=35423
usa_avergae=56516
canada_average=64000
cambodian_average=5649856

#     TAKING INPUTS 
salary=int(input("enter your salary in Germany : "))
migrate=input("enter the country you want to migrate to :")
if (migrate=="Canada" or migrate=="US" or migrate=="UK" or migrate=="Cambodia"):
    def convertSalary():
        inr=56*salary
        usd=1.18*salary
        pound=0.91*salary
        cambodian=4847.38*salary
                
        
