#   MARKING GLOBAL VARIABLES 
RED="red"
BLUE="blue"
YELLOW="yellow"

color1=input("enter the  primary color in lowercase letter :").lower()
color2=input("enter the secondary color in lowercase letter :").lower()

#    CHECKING THE COLORS 
if color1!=RED and color1!=BLUE and color1!=YELLOW :
    print("Error : Invalid Color1")

elif color2!=RED and color2!=BLUE and color2!=YELLOW:
    print("Error : Invalid Color2")
    
elif color1 == color2:
    print("Error : The two colors you entered are same ")
    
else:
    #   MIXING THE COLORS 
    if color1==RED:
        if color2==BLUE:
            print("PURPLE")
        elif color2==YELLOW:
                print("ORANGE")
    
    if color1==BLUE:
        if color2==RED:
            print("PURPLE")
        elif color2==YELLOW:
            print('GREEN')
            
    if color1==YELLOW:
        if color2==RED:
            print("ORANGE")
        elif color2==BLUE:
            print("GREEN")
    

    