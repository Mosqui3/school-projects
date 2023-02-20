#@author: Oscar Martinez Vega
#
#Homework - Shoe Class
#Programming Languages
#Dr. John Coleman
#
#Description:
#   Function rand_map(n) returns a function which
#   is a random map on range(n) (0, 1, 2, ..., n-1).
#   If f(k) is computed once then the same value
#   should be returned in subsequent calls to f(k).


from functools import cache
import random


def rand_map(n):
    @cache
    def f(k):
        return int(n*random.random())
    return f
