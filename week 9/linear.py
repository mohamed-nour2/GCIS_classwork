from array import Array
from random import randint

randint.seed(1)


array = Array(10)

#intialize array with random values

for i in range(len(array)):
    array[i] = randint(1,100)
    

print(array)
import time
start = time.time()

value = 9
flag = False


def linear_search(array):
    for index in range (len(array)):
        if array[index] == value:
            flag = True
            return index
        
    return 

index = linear_search(array)
print
        
       


