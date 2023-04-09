def Merge(dict1, dict2): 
    res = {**dict1, **dict2} 
    return res 
      
# 两个字典
dict1 = {"name": "Joy", "age": 25}
dict2 = {"name": "Joy", "city": "New York"}
dict3 = Merge(dict1, dict2) 
print(dict3)
def list_to_dictionary(keys, values):
  return dict(zip(keys, values))

list1 = [1, 2, 3]
list2 = ['one', 'two', 'three']

print(list_to_dictionary(list1, list2))
a, b = 1,0

try:
    print(a/b)
except ZeroDivisionError:
    print("Can not divide by zero")
finally:
    print("Executing finally block")
import sys

var1 = 15
list1 = [1,2,3,4,5]

print(sys.getsizeof(var1))
print(sys.getsizeof(list1))
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

a, b = 5, 10

print((add if b > a else subtract)(a,b))
