import math
my_foods = ['pizza','falafel','frites']
friend_foods = my_foods[:]

my_foods.append('spaghetti')
friend_foods.append('ice cream')

print("my favorite foods are:")
print(my_foods)
print("\nmy friend's favorite foods are:")
print(friend_foods)

number = input('Enter a number?\n\t')
print("number = " + number)

print("Sqrt of {0} = {1}".format(number,math.sqrt(int(number))))

