#@author: Oscar Martinez Vega
#
#Homework - mod42 Decorator
#Programming Languages
#Dr. John Coleman
#
#Description:
#mod42 decorator – mod42 is a decorator that takes
#the input of the wrapped function and replaces it
#by the input and the output mod 42.
#
#Extra Cedrit
#mod(n) decorator - mod is a decorator that takes
#the input of the wrapped function and replaces it
#by the input and the output mod n.

from functools import wraps

#Normal mod42 decorator
def mod42(f):
    @wraps(f)
    def wrapper(*args,**kwargs):
        args = tuple(arg%42 for arg in args)
        kwargs = {k:v%42 for k,v in kwargs.items()}
        result = f(*args,**kwargs)
        return result%42
    return wrapper

#EXTRA CREDIT
def mod(n):
    def inner(f):
        @wraps(f)
        def wrapper(*args,**kwargs):
            args = tuple(arg%n for arg in args)
            kwargs = {k:v%n for k,v in kwargs.items()}
            result = f(*args,**kwargs)
            return result%n
        return wrapper
    return inner

@mod42
def exp(a,b):
    return a**b

@mod(42)
def exp2(a,b):
    return a**b
