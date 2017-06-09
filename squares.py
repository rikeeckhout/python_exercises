squares = []
for value in range(1,11):
    squares.append(value ** 2)

print(squares)
print("min : " + str(min(squares)))
print("max : " + str(max(squares)))
print("sum : " + str(sum(squares)))

squares = [value ** 2 for value in range(1,11)]
print(squares)
print(squares[:4])