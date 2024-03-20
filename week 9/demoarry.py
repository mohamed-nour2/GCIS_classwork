from arrays import Array

array2 = Array(5,0)

array2  [3] = -1
array2  [1] = 2
array2  [4] = array2[1] + array2[3]
print(array2)

#first method

for i in range(len(array2)):
    print(array2[i])


