#@author: Oscar Martinez Vega
#
#Final Exam - Question 3
#Programming Languages
#Dr. John Coleman

import math

def f(n):
    factors = [i for i in range(1,n) if n%i == 0]
    oddFactors = [f for f in factors if f%2 != 0]
    limit2 = int(math.sqrt(n))
    generator = []
    for f in oddFactors:
        for p in range(1, limit2 + 1):
            if (2**p)*f == n:
                for i in range(p):
                    generator.append(2)
                generator.append(f)
    for t in generator:
        yield t
        
print('f(40)')
for value in f(40):
    print(value)
print()
print('f(16)')
for value in f(16):
    print(value)
print()
print('f(150)')
for value in f(150):
    print(value)
