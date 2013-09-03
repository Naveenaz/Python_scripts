#!/usr/bin/python

class SquareSumComputer:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def transform(self, x):
        print x * x

    def inputs(self):
        print range(self.a, self.b)

    def compute(self):
        print sum(self.transform(value) for value in self.inputs())

class CubeSumComputer(SquareSumComputer):
    def transform(self, x):
         print x * x * x

square=SquareSumComputer(5,5)
cube=CubeSumComputer(1,5)
cube.transform(5)

cube.inputs()    #inheritance



--------------------------------------
Output:

./python override.py 
125
[1, 2, 3, 4]
