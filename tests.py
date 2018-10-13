#while the user keep entering another value instead of a WHOLE NUMBER
#keep on looping till the user enter the right value
import sys
while True:
 try:
    number = int(input("Enter your age: " ))
    print("thanks for entering the correct value")
    break
 except ValueError:
    print("Pls, enter a whole number i.e. numbers without decimals")


try:
    f = open('ben.txt')
    for line in f:
        print(line.rstrip())
    f.close()
except IOError as e:
    print(e)
