"""
Error_handling

Interpting normal exceution of code is called error or exception
we will handle by using error handling

syntax:

try:
    risky code
except:
    print("error")
else:
    print("no error")
finally:
    print("Always")     

"""


a = 10
b =  5

try:
    print(b)
except:
    print("Error")
else:
    print("No error")
finally: 
    print("always")  

# try :
#     print('a'+33) 
# except Exception as a: 
#     print("type error",a)
# except ValueError:
#     print("value error")                     
