'''
====ADVANCED FUNCTIONS====
* Lambda
* Filter
* map
* Generator
* reduce

'''
 
'''
---------------------LAMBDA------------------
=> A lambda function is a small anonymous function.(It is called unknow)
=> A lambda function can take any number of arguments,
   but can only have one experssion

'''

# x = lambda a,b,c : a+b-c
# print(x(5,7,9))
# print("\n")



# l1 = [12,34,24,35]
# l2 = []
# for i in l1:
#     t = lambda a:a+1
#     l2.append(t(i))
# print(l2)    
# print("\n")

'''
-------------------FILTER----------------
The filter() method filters the given sequence with the help
of a function that the tests each element in the sequence
to be true or not

-----------------Syntax:
filter(function,sequence)
parameters:

function: function that tests if each element of a sequence true or not.
sequence: sequence which needs to be filtered, it can be sets, lists, tuple,
          or containers of any iterators.
returns: returns an iterator that is already filtered.

'''

# ages = [3,7,9,14,18,24,30]
# def myfun(x):
#     if x>= 18:
#         return True
#     else:
#         return False
# vote = filter(myfun, ages)
# print(list(vote))   


'''
------------------Generator-function---------------------
Generator-function: A generator-function is defined like a normal function,
                    is defined like a normal function,
                    but whenever it needs to generate a value, it does so with
                    the yield keyword rather than return.
                =>  If the body of a def contains yield, the function automatically
                    becomes a generator function. 

A Python program to demonstrate use of 
generator object with next()

+ A generator function:

'''

# def simpleGeneratorFun():
#     yield 11
#     yield 12
#     yield 13

# # x is a generator object
# x = simpleGeneratorFun()

# # Iteration over the generator object using next
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())


'''
---------------------------------------YIELD---------------------------------------
The yeild statement is responsible for controlling the flow of the generator function.
It pause the function execution by saving all states and yielded to the caller.
Later it resumes execution when a successive function is called. We can use the multiple
yield statement in the generator function.

The return statement return a value and terminates the whole function and only one return 
statement can be used in the function.

'''

# def n():
#     return 1+5
#     return 2+1
# print(n())


'''

--------------------------------------MAP()----------------------------
The python map() function is used to return a list of results
after applying a given function to each item of an iterable(list, tuple etc.,)

map(function, iteration)
'''

# def calculate(n):
#     return n+n
# number = (1,2,3,4)
# result = map(calculate, number)
# print(list(result))


'''
------------------------REDUCE-------------------------
The reduce() function, as the name describes,
applies a given function to the iterables and returns a single value.


'''

# => Not running <=
#    def sum(*a):
#        return a+a
#    sum(1,3,5,6,7,9,12,13)

# from functools import reduce
# r=reduce(lambda a,b:a+b,[12,13,25,39,45])
# print(r)


a = "Nare"
l= lambda d:a+"sh"
print(l(a))