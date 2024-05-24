# Fencing price 
# Auther: Hano De Bruin 
# Date 
# Version 1

def number_check(questions):
    eror = "put in a number bigger than zero/n"
    while True: 
        try:
            number=float(input(questions))
            if number>0:
                return number 
            else:
                print(eror)
        except ValueError:
            print (eror)
keepgoing="Y"
while keepgoing =="Y":  
    price= number_check("price per meter ")
    width = number_check ("width")
    hight= number_check ("hight")
    perimeter= (width+hight)*2
    cost=(perimeter)*price 
    print(f"Fencing cost per meter: = {cost} ")
    keepgoing = input ("Continue? Y/N ")
    if keepgoing!=("N"):
        keepgoing="Y"
print("Thanks for using this program")

            