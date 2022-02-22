# Question 1
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += 'Oke'
print(cheese)
#Doesn't work because appends each letter separately as a list item - but why?
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese.append('Oke')
print(cheese)
#Using the append method works to add a single item
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += ['Vignotte', 'Delice de Bourgogne']
print(cheese)
#Using the overloaded operator nb square brackets to add more than one item
cheese.insert(2, 'Jarlsberg')
print(cheese)
#Item inserted at given position
cheese[2] = 'Gruyere'
print(cheese)
#replaces item in given position in list
cheese[:0] = ['Dolcelatte', 'Mrs Bell\'s Blue']
print(cheese)
#using slicing to prepend list items
cheese.pop(3)
print(cheese)
#removed fourth item in the list
print(sorted(cheese))
#returns a new copy of the list but does not alter the list
print(cheese)
cheese.sort()
print(cheese)
#The list has been permanently altered
