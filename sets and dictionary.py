favourite_fruits={'Apple','Pineapple','Watermelon','grapes','Orange'}
print(favourite_fruits)
favourite_fruits.add('Banana')
print(favourite_fruits)
favourite_fruits.remove('Pineapple')
print(favourite_fruits)
print('Banana' in favourite_fruits)

details={'name':'Anjani','Age':20,'Occupation':'Student'}
print(details)
details['Location']='Karimnagar'
print(details)
details.update({'Age':22})
print(details)
print(details['Occupation'])

def remove_duplicates(numbers):
 return set(numbers)
numbers=[1,2,2,1,4,4,5]
results=remove_duplicates(numbers)
print(results)

