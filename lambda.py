x = lambda a, b : a * b
print(x(5, 6))

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
 
final_list = list(filter(lambda x: (x%2 != 0) , li))
print(final_list)

# Using lambda() Function with map()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
 
final_list = list(map(lambda x: x*2, li))
print(final_list)

animals = ['dog', 'cat', 'parrot', 'rabbit']
uppered_animals = list(map(lambda animal: str.upper(animal), animals))
 
print(uppered_animals)

from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print (sum)