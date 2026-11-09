n = int(input("Introduceți un număr n: "))
nr = 0

for a in range(9, -1, -1):
    m = n

    while m != 0 and m%10 != a:
        m = m//10

    if m != 0:
        nr = nr * 10 + m%10

print(nr)