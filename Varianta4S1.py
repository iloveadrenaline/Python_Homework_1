a = int(input("Introduceți un număr a: "))
b = int(input("Introduceți un număr b: "))

if a < b:
    a, b = b, a 

for x in range(a, b - 1, -1):
    if x % 2!= 0:
        print(x)