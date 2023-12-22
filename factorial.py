def factorial(n):
    if(n == 0 | n == 1):
        return n
    else:
        return n * factorial(n - 1)

class example:
    def __init__(self):
        num = int(input("Introduce un numero:"))
        print(factorial(num))
        
example()


        