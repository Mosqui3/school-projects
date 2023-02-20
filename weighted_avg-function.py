#@author: Oscar Martinez Vega
#
#Final Exam - Question 6
#Programming Languages
#Dr. John Coleman

import statistics

def weighted_average(floats: list[float],weigths: list[float]=None ) -> float:
    if weigths == None:
        return statistics.mean(floats)
    else:
        if len(floats) != len(weigths): raise ValueError('floats and weigths must be of the same size')
        multi = []
        for i in floats:
            multi.append(i*weigths[floats.index(i)])
        return statistics.mean(multi)
        
        
print(weighted_average([100.0,95.0],[0.5,0.5]))
print(weighted_average([100.0,95.0]))
