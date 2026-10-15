
#exceercise1
'''employees profile'''
'''
emp ={
    'name':'Bhaskar',
    'experience':4,
    'primary_language':['c','c++'],
    'skills':'to be verified',
    'is_learning_ai':'yes'
}

#simply printing values
for k,v in emp.items():
    print(f'{k}:{v}')
if(emp['experience']>=3):
    print('experienced eng')

#excercise2

numbers = [10, 25, 30, 45, 50, 75, 100]

for val in numbers:
    if(val>40):
        print(val)'''


#excercise3

errors = [
    "Connection timeout",
    "Authentication failed",
    "Connection timeout",
    "Invalid response",
    "Authentication failed",
    "Connection timeout",
]

#expected o/p 
'''Connection timeout: 3
Authentication failed: 2
Invalid response: 1'''
    
def count_errors(errors):
    error_items = {}
    for item in errors:
        if(item in error_items):
            error_items[item] = error_items[item]+1
        else:
            error_items[item] = 1
    return error_items
    for k,v in error_items.items():
        print(f"{k}:{v}")  

ce = count_errors(errors)
for k,v in ce.items():
    print(f"{k}:{v}")  

'''maxc = 0
errorz = ''
for item in error_items:
    if(maxc<error_items[item]):
        maxc = error_items[item]
        errorz = item
print(f"most frequent error :{errorz}")
print(f"count: {maxc}")'''