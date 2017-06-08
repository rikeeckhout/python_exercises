motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('honda')
print(motorcycles)
motorcycles.insert(0,'bmw')
print(motorcycles)
motorcycles.insert(1,'test')
print(motorcycles)
del motorcycles[1]
print(motorcycles)
#popped_moto = motorcycles.pop()
#print(motorcycles)
#print(popped_moto)
#first_owned = motorcycles.pop(0)
#print(motorcycles)
#print(first_owned)
too_expensive = 'ducati'
print(too_expensive)
motorcycles.remove(too_expensive)
print(motorcycles)
print(motorcycles[-1])
for motorcycle in motorcycles:
    print(motorcycle.title() + ", nice motorcycle!")

print("End of List")