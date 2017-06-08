import sys
print("hello, I'm Python!\n")
fruits = ['Banana', 'Apple', 'Lime']
loud_fruits = [fruit.upper() for fruit in fruits]
print(loud_fruits)
list(enumerate(fruits))

numbers = [2,4,6,8]
product = 1
for number in numbers:
    product = product * number

print('the product is : ',product)

name = input('What is your name?\n\t')
print("Hi, %s." %name)

def fib(n):
    a, b = 0, 1
    print("var a={0}\nvar b={1}\n".format(str(a),str(b)))
    while a < n:
        print(a,end=';')
        print()
        a, b = b, a+b
fib(1000)

