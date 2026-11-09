x = int(input("Introduceți un număr x: "))
z = int(input("Introduceți un număr z: "))
y = 0

while True:
    y = y*10+x%10
    x = x//100
    if x == 0:
        break

while y*z > 0 and y % 10 == z%10:
    y = y//10
    z = z//10


if y+z == 0:
    print('1')

else:
    print('0')