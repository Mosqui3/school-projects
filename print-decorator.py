#@author: Oscar Martinez Vega
#
#Final Exam - Question 5
#Programming Languages
#Dr. John Coleman

from functools import wraps

def printer(f):
    @wraps(f)
    def wrapper(*args,**kwargs):
        args = tuple(arg for arg in args)
        kwargs = {k:v for k,v in kwargs.items()}
        print('inputs: args:',args,'kwargs:',kwargs)
        result = f(*args,**kwargs)
        print('output:',result)
        return result
    return wrapper

@printer
def f(a,c,b):
    return a+c+b

print(f(3,1,b=6))
