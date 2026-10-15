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
    
#Here, KeyError happens because "error" isn't a key in the dictionary.
'''
Common exceptions you'll encounter:
Exception	Typical cause
NameError	Referencing an undefined name
KeyError	Missing dictionary key
IndexError	Invalid list index
TypeError	Operation used with an incompatible type
ValueError	Correct type, but invalid value
FileNotFoundError	File doesn't exist at the specified path

A useful debugging habit: read the last line of a traceback first to understand the exception, then inspect the preceding lines to locate where it happened.
Don't catch every exception indiscriminately. Catch the errors you know how to handle, and let unexpected failures remain visible while developing.
'''