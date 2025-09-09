"""
ENCAPSULATION

-> wrapping of variable & methsods into single unit.

->Access specifer:
+ public
+ private      (__) double undrescore
+ protected     (_) single underscore

"""
# class demo():
#     __a = 10
#     _b = 20
#     print(__a)
#     print(_b)

class demo():
    def __init__(self,a,b):
        self.__a=a
        self._b=b
class demo2(demo):
     def output(self):
        #   print(self._b)
        print(self.__a)
d=demo2(3,4)
d.output()           
    