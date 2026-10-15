# how python will know ki ye lsit hai  ya tuple ya set
# list -> [] --> .append(), .remove()
# tuple-> ()
# set -> {} --> .add(), .remove()

''' python list is basically analogous to c++ vector '''
'''
languages = ["C++", "Python", "JavaScript"]

print(languages)
print(languages[0])
print(languages[1])

languages[0] = 'poland'
print(languages[0])

#add
languages.append('GO')
print(languages)
languages.remove('GO')
print(languages)

#languages.remove("po") --> error
print(len(languages))

#indexing
numbers = [10, 20, 30, 40, 50]


'''
# 10
# 50
# [20, 30, 40]
'''
print(numbers[0]) 
print(numbers[-1])
print(numbers[1:4])


#tuple
#same as list but immutable

point = (10, 20)

#set
# A set stores unique values.

numbers = {1, 2, 3, 3, 3}
print(numbers)

skills = {"C++", "Python", "Git"}

skills.add("Docker") #this will add docker in the set at any random position unlike .append() in list
skills.add("Python") #python won't be added because it's already there

print(skills)
skills.remove('Docker')
print(skills)'''


#Dictionary 
# This is one of the most important Python structures for automation and AI.

#unordered_map ke jaise

person = {
    "name": "Bhaskar",
    "age": 26,
    "role": "Software Engineer"
}

print(person)

#for adding new entries
person["experience"] = 4
print(person)
#person.popitem('experience')
#print(person)
for p in person:
    print(p)

for keys in person.keys():
    print(person[keys])
    
for key,val in person.items():
    print(f"key is {key}, val is  {val}")