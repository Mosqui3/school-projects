#@author: Oscar Martinez Vega
#
#Project 3 - Multiset Class
#Programming Languages
#Dr. John Coleman
#
#Description:
#Multiset class – a Multiset is an unordered container
#object in which objects can appear more than once. 

class Multiset:
    #initiates the class by loading the elements into a dictionaries having the elements as the key and their count as the value
    def __init__(self, items):
        self.multiset = {}
        if type(items) == dict or type(items) == int or type(items) == float or type(items) == complex or type(items) == bool:
            raise TypeError(f"items must be an iterable of type string, list, tuple, or set. {type(items).__name__} is not allowed")
        for e in items:
            if type(e) == list or type(e) == set or type(e) == tuple or type(e) == dict or type(e) == bool:
                raise TypeError(f"Multiset cannot contain lists, sets, tuples, dictionaries, or booleans as elements. {e} is a {type(e).__name__}")
            else:
                if e in self.multiset:
                    x = self.multiset[e]
                    x += 1
                    self.multiset[e] = x
                else:
                    self.multiset[e] = 1

    def __repr__(self):
        return f'Multiset({self.multiset})'

    def __str__(self):
        return f'{self.multiset}'

    #len() => lengt method: returns the sum of the counts
    def __len__(self):
        x = 0
        for i in self.multiset.values():
            x = x + i
        return x

    def __iter__(self):
        for k,c in self.multiset.items():
            for _ in range(c):
                yield k

    #in => contains method: True or False depending is the item is or is not in the multiset
    def __contains__(self, item):
        if item in self.multiset.keys():
            return True
        else:
            return False

    #returns the underlying set. Just the items not the counts
    def support(self):
        x = []
        for e in self.multiset.keys():
            x.append(e)
        setM = set(x)
        return setM

    #returns the count of an specific item
    def count(self, item):
        if item not in self.multiset:
            return 0
        else:
            return self.multiset[item]

    #adds a new item to the multiset and updates the count
    def add(self, item):
        if type(item) == list or type(item) == set or type(item) == tuple or type(item) == dict or type(item) == bool:
            raise TypeError(f"Multiset cannot contain lists, sets, tuples, dictionaries, or booleans as elements. {item} is a {type(item).__name__}")
        else:
            if item in self.multiset:
                x = self.multiset[item]
                x += 1
                self.multiset[item] = x
            else:
                self.multiset[item] = 1

    #remove an item by updating its count or removing it completely
    def remove(self, item):
        if item not in self.multiset:
            raise ValueError(f'{item} not found in Multiset')
        elif self.multiset[item] == 1:
            self.multiset.pop(item)
        else:
            x = self.multiset[item]
            x -= 1
            self.multiset[item] = x

    #adds an iterable of items to the multiset with the method union
    def update(self, items):
        if type(items) == dict or type(items) == int or type(items) == float or type(items) == complex or type(items) == bool:
            raise TypeError(f"items must be an iterable of type string, list, tuple, or set. {type(items).__name__} is not allowed")
        itemsM = Multiset(items)
        self.__ior__(itemsM)
        return self

    #adds an iterable of items to the multiset with the method add
    def update_add(self, items):
        if type(items) == dict or type(items) == int or type(items) == float or type(items) == complex or type(items) == bool:
            raise TypeError(f"items must be an iterable of type string, list, tuple, or set. {type(items).__name__} is not allowed")
        for e in items:
            self.add(e)
        return self

    #== --> equality method: returns True or False if two Multisets are equal or not
    def __eq__(self, otherMultiset):
        if type(otherMultiset) != Multiset:
            raise TypeError(f"unsupported operand type(s) for =: 'Multiset' and '{type(otherMultiset).__name__}'. Second operand must be a Multiset")
        if self.multiset == otherMultiset.multiset:
            return True
        else:
            return False

    #<= --> less-equal method: returns True or False if two Multisets are less or equal, or not
    def __le__(self, otherMultiset):
        if type(otherMultiset) != Multiset:
            raise TypeError(f"unsupported operand type(s) for <=: 'Multiset' and '{type(otherMultiset).__name__}'. Second operand must be a Multiset")
        for e in self.multiset.keys():
            if e in otherMultiset.multiset.keys():
                if self.multiset[e] <= otherMultiset.multiset[e]:
                    pass
                else:
                    return False
            else:
                return False
        return True

    #< --> less method: returns True or False if two Multisets are less than each other or not        
    def __lt__(self, otherMultiset):
        if type(otherMultiset) != Multiset:
            raise TypeError(f"unsupported operand type(s) for <: 'Multiset' and '{type(otherMultiset).__name__}'. Second operand must be a Multiset")
        if self.__le__(otherMultiset) == False:
            return False
        else:
            for e in self.multiset.keys():
                if self.multiset[e] < otherMultiset.multiset[e]:
                    return True
                else:
                    return False
                
    #| --> union method: returns the union of two Multisets            
    def __or__(self, otherMultiset):
        if type(otherMultiset) != Multiset:
            raise TypeError(f"unsupported operand type(s) for |: 'Multiset' and '{type(otherMultiset).__name__}'. Second operand must be a Multiset")
        union = {}
        for e in otherMultiset.multiset.keys():
            if e in self.multiset.keys():
                if self.multiset[e] >= otherMultiset.multiset[e]:
                    union[e] = self.multiset[e]
                else:
                    union[e] = otherMultiset.multiset[e]
            else:
                union[e] = otherMultiset.multiset[e]
        for e in self.multiset.keys():
            if e not in otherMultiset.multiset.keys():
                union[e] = self.multiset[e]
        return union

    #|= --> union-equal method: assigns the union of two Multisets to the the first multiset
    def __ior__(self, otherMultiset):
        if type(otherMultiset) != Multiset:
            raise TypeError(f"unsupported operand type(s) for |=: 'Multiset' and '{type(otherMultiset).__name__}'. Second operand must be a Multiset")
        self.multiset = self.__or__(otherMultiset)
        return self

    #& --> intersection method: returns the intersection of two Multisets
    def __and__(self, otherMultiset):
        if type(otherMultiset) != Multiset:
            raise TypeError(f"unsupported operand type(s) for &: 'Multiset' and '{type(otherMultiset).__name__}'. Second operand must be a Multiset")
        inter = {}
        for e in self.multiset.keys():
            if e in otherMultiset.multiset.keys():
                if self.multiset[e] <= otherMultiset.multiset[e]:
                    inter[e] = self.multiset[e]
                else:
                    inter[e] = otherMultiset.multiset[e]
        return inter

    #&= --> intersection-equal method: assigns the intersection of two Multisets to the the first multiset
    def __iand__(self, otherMultiset):
        if type(otherMultiset) != Multiset:
            raise TypeError(f"unsupported operand type(s) for &=: 'Multiset' and '{type(otherMultiset).__name__}'. Second operand must be a Multiset")
        self.multiset = self.__and__(otherMultiset)
        return self

    #-  -->  subtraction method: returns the subtraction of two Multisets
    def __sub__(self, otherMultiset):
        if type(otherMultiset) != Multiset:
            raise TypeError(f"unsupported operand type(s) for -: 'Multiset' and '{type(otherMultiset).__name__}'. Second operand must be a Multiset")
        dif = self.multiset.copy()
        for e in otherMultiset.multiset.keys():
            if e in dif.keys():
                dif[e] = dif[e] - otherMultiset.multiset[e]
        empty = []
        for e in dif.keys():
            if dif[e] <= 0:
                empty.append(e)
        if len(empty) == len(dif):
            dif.clear()
        else:
            for n in empty:
                dif.pop(n)
        return dif

    #-= --> subtraction-equal method: assigns the subtraction of two Multisets to the the first multiset
    def __isub__(self, otherMultiset):
        if type(otherMultiset) != Multiset:
            raise TypeError(f"unsupported operand type(s) for -=: 'Multiset' and '{type(otherMultiset).__name__}'. Second operand must be a Multiset")
        self.multiset = self.__sub__(otherMultiset)
        return self

    #^  -->  xor method: returns the xor of two Multisets
    def __xor__(self, otherMultiset):
        if type(otherMultiset) != Multiset:
            raise TypeError(f"unsupported operand type(s) for ^: 'Multiset' and '{type(otherMultiset).__name__}'. Second operand must be a Multiset")
        union = self.__or__(otherMultiset)
        inter = self.__and__(otherMultiset)
        for e in inter.keys():
            if e in union.keys():
                union[e] = union[e] - inter[e]
        empty = []
        for e in union.keys():
            if union[e] <= 0:
                empty.append(e)
        if len(empty) == len(union):
            union.clear()
        else:
            for n in empty:
                union.pop(n)
        return union

    #^= --> xor-equal method: assigns the xor of two Multisets to the the first multiset
    def __ixor__(self, otherMultiset):
        if type(otherMultiset) != Multiset:
            raise TypeError(f"unsupported operand type(s) for ^=: 'Multiset' and '{type(otherMultiset).__name__}'. Second operand must be a Multiset")
        self.multiset = self.__xor__(otherMultiset)
        return self


def main():
    example1 = Multiset('OscarMartinezVega')
    print("This is my first example of Multiset:", "\n", example1)
    print("The length of example1:", len(example1))
    print("The support of example1:", example1.support())
    print("The count for the letter 'a' in example1:", example1.count('a'))
    example1.remove('a')
    example1.remove('s')
    print("Remove once 's' and 'a' from example1:", example1)
    print("Count of 's':", example1.count('s'))
    print("Count of 'a':", example1.count('a'))
    example1.add('a')
    print("Add 'a' once. Count of 'a':", example1.count('a'))
    print("Update example1 with 'OscarOscar':", example1.update('OscarOscar'))
    print("Update_add example1 with 'MartinezVega':", example1.update_add('MartinezVega'),"\n")

    example2 = Multiset([1,1,2,3,3,4,5,5,6,7,7,8,9,9])
    print("This is my second example of Multiset:", "\n", example2)
    example3 = Multiset([1,2])
    print("This is my third example of Multiset:", "\n", example3)
    print("Are example2 and example3 equal?", example2 == example3)
    print("Is example2 less or equal than example3?", example2 <= example3)
    print("Is example3 less than example2?", example3 < example2, '\n')

    example4 = Multiset([1,2,3,4,5,6])
    print("This is my fourth example of Multiset:", "\n", example4)
    example5 = Multiset([4,5,6,7,8,9])
    print("This is my fifth example of Multiset:", "\n", example5)
    print("Union of example4 and example5:", example4 | example5)
    print("Intersection of example4 and example5:", example4 & example5)
    print("Subtraction of example4 minus example5:", example4 - example5)
    print("Xor of example4 and example5:", example4 ^ example5)
    example4 ^= example5
    print("Assigning xor of example4 and example5 to example4:", example4)

if __name__ == "__main__":
    main()

