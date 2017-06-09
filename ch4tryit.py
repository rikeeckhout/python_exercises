for value in range(1,21):
    print(value)

numbers = list(range(1,1000001))
#for number in numbers:
#    print (number)

print("min : "+str(min(numbers)))
print("max : "+str(max(numbers)))
print("sum : "+str(sum(numbers)))

numbers = list(range(1,20,2))
print(numbers)

numbers = list(range(3,31,3))
for number in numbers:
    print (number)

cubes = [value ** 3 for value in range(1,11)]
print(cubes)
print(cubes[-5:])
for cube in cubes[:5]:
    print (cube)