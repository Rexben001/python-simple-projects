
def gg():
 x = int(input(": "))
 y = int(input(": "))
 if x < y:
    temp = x
    x = y
    y = temp
 remain = x%y
 print("1", remain)
 while remain != 0:
    x = y
    print("x", x)
    y = remain
    print("y", y)
    remain = x%y
    print("2",remain)
 gcd = y
 print (gcd)

gg()   

