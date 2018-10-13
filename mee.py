number = int(input("Enter a number: "))
def collatz(number):
        if number %2 == 0:
            number =(number/2)
            print(number)
            return number
        elif number %2 == 1:
            number = (3*number)+1
            print(number)
            return number
        else:
            print()
        return number
result = collatz(number)
while result != 1:
    collatz(number)
    
            
