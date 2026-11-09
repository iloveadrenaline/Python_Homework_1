x = int(input("Introduceți un număr x: "))
z = int(input("Introduceți un număr z: "))

while x > 0:
    y = int(input("Introduceți un număr y: "))

    if z < y-x:
        print(x%10)
    else:
        print(y%10)
    
    x = y