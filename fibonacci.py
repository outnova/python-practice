def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

class example:
    def __init__(self):
        num = int(input("Ingrese un numero: "))
        fib(num)

example()

# Code in C / Java: 
#
# fibonacci(n) {
#   if(n == 0 || n == 1) {
#       return n;
#   } else {
#       return fibonacci(n - 1) 
#       + fibonacci (n - 2);
#   }
# }