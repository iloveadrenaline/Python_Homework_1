n = int(input("Introduceți un număr n: "))
s = -1

while n > 0:
    if n%10 > s:
        s = n%10
    else:
        s = 11

    n = n//10

print(s)