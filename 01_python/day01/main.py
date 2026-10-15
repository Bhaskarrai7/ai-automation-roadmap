name = "Bhaskar" #string
age = 26         #int
experience = 4.0 #float
is_learning_ai = True #bool
have_learnt = None

print(name)
print(age)
print(experience)
print(is_learning_ai)

print(type(age))
print(type(have_learnt))

''' 
let's deep dive into strings
'''

name = 'Saurabh'

print(len(name))
print(len('Bhaskar'))
print('Bhaskar'.lower())
print(name.upper())

#You can index strings:

name = "Bhaskar"
print(name[0])
print(name[1])
print(name[-1])
#Bhaskar
#0123456
print(name[0:3]) #Bha
print(name[2:5]) #ask
print(name[:4])  #Bhas
print(name[3:])  #skar

#f-strings
#instead of 

name = "Bhaskar"
age = 26
print("My name is " + name + " and I am " + str(age)) #typecast

print(f"My name is {name } and I am {age}")


#mini exercise
results = [
    "passed",
    "failed",
    "passed",
    "skipped",
    "failed",
    "passed",
]

def summarize_test_results(results: list[str]) -> dict[str, int]:
    result_sum = {}
    for item in results:
        if item in result_sum:
            result_sum[item]+=1
        else:
            result_sum[item]=1
    return result_sum

ans = summarize_test_results(results)
for key,val in ans.items():
    print(f"{key}:{val}")