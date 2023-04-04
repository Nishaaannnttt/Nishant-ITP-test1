#     DEFINING GLOBAL VARIABLES 
uk_average=35423
usa_average=56516
canada_average=64000
cambodian_average=5649856

#     TAKING INPUTS 
salary=int(input("enter your salary in Germany : "))
migrate=input("enter the country you want to migrate to :").lower()

def convertSalary():    
    
    cad=1.55*salary
    usd=1.18*salary
    pound=0.91*salary
    cambodian=4847.38*salary
    # return cad,usd,pound,cambodian
    
    if(migrate=="canada"): 
        # cad=cad
        if cad>canada_average:
            print("you will be rich in canada with salary of " +str(cad) +" CAD")
        else:
            print("you will be poor in canada with salary of "+str(cad)+" CAD")
            
    elif(migrate=="usa"):
        if usd>usa_average:
            print("you will be rich in usa with salary of " +str(usd) +" USD")
        else:
            print("you will be poor in usa with salary of "+str(usd)+" USD")
            
    elif(migrate=="uk"):
        if pound>uk_average:
            print("you will be rich in uk with salary of " +str(pound) +" UK")
        else:
            print("you will be poor in uk with salary of "+str(pound)+" UK")
            
    elif(migrate=="cambodia"):
        if cambodian>cambodian_average:
            print("you will be rich in cambodia with salary of " +str(cambodian) +" cambodian riel")
        else:
            print("you will be poor in cambodia with salary of "+str(cambodian)+" cambodian riel")
    
convertSalary()
            
        
            
        
        
    
                
        
