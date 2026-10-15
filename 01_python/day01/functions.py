'''again in cpp
int add(int a, int b) {
    return a + b;
}'''

#in py
'''def add (a,b):
    return a+b

print(add(8,9))'''

#positional arguments
'''def describe_person(name, age):
    print(f"{age} is {name} years old")

describe_person(90, "Bhaskar")

#describe_person('bhaskar', 90)'''


#keyword arguments
#You can specify the parameter names explicitly:

#describe_person(age=26, name="Bhaskar")

# Default arguments
# Sometimes an argument should be optional.

'''def greet(name, message="Welcome"):
    print(f"{message}, {name}!")

greet("Bhaskar")
greet("Bhaskar", "Good morning")'''


#return vs print inside a function
#simple rule
# if u want to re-use the values use return else simply return

'''
name = 'bhaskar'

def change(name):
    name = 'python'
    return name

k = change(name)
print(name)
print(k)'''

'''above code will print bhaskar python'''
#One practical rule: prefer passing values into functions and returning results instead of relying on global variables. This makes code easier to test and debug.

'''Type	Mutable?
int	No
float	No
bool	No
str	No
tuple	No, although it may contain mutable objects
list	Yes
dict	Yes
set	Yes'''

#like as jaise upar vale code me string ko update karne ka try kara function ke andar to nahi hua

#but let's try same code with lists

def change_lis(my_list):
    my_list.clear()

li=[0,9,8,7]

change_lis(li)
print(li) #--> empty list

''' yaha pe ek concept hai
agar mai function ke andar my_list = [] --> this makes the local param refer to a diff list
but
my_list.clear(), my_list.append() --> this modifies the list object'''