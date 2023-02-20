#@author: Oscar Martinez Vega
#
#Final Exam - Question 4
#Programming Languages
#Dr. John Coleman

class Vector:
    def __init__(self, numbers):
        self.numbers = numbers

    def __add__(self, vector):
        if len(self.numbers) != len(vector.numbers): raise ValueError('Vectors must be of the same size')
        addition = []
        for i in self.numbers:
            addition.append(i+vector.numbers[self.numbers.index(i)])
        self.numbers = addition.copy()
        addition.clear()

    def __repr__(self):
        return f'Vector({self.numbers})'

    def __str__(self):
        return f'{self.numbers}'

a = Vector([1,2,3])
b = Vector([10,20,30])

print('Vectot a:', a)
print('Vectot b:', b)

a+b

print('a+b:', a)
