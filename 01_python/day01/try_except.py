#Basic exception handling
'''
Real automation code fails. 
Files disappear, APIs time out, JSON is malformed, 
and dictionaries may not contain the key we expect.
Python provides try and except to handle expected failures.'''

response = {"status": "passed"}

try:
    print(response["error"])
except KeyError:
    print("The response does not contain an error field")