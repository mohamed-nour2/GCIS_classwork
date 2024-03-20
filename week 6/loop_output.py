for number in range (1 ,11):
    v = number  **2
    print(v, end=" ")

m = "mohamed"
v1 = m * 3
print(v1)

line = "#" * 10 
for i in range (1,6):
    print(line)

for row in range (0,5):
    for coloum in range (0 ,10):
        print("#" , end = "")
    print()


for count in range (0,5):
    line = "#" * count
    print(line)



PART1 = "#"
PART2 ="++"
for count in range (1,7):
    line = PART1*count + PART2* count +PART1
    print(line)



sum = 0
count = 1 
while count <= 10 :
    sum = sum + count 
    count = count + 1
print(sum)

n = int(input("enter a value: "))
sum = 0 
number_copy = n
while n > 0:
    ld =n % 10
    sum = sum + ld **3 
    number = number // 10

if number_copy == sum :
    print(f"{number}is an armstrong number.")

else :
    print(f"{number}is NOT an armstrong number.")

def isarmstrong(number):
    sum = 0
    count = 1
    while count <= 10:
        sum = sum + count
        count = count + 1
    print(sum)

    n = number
    sum = 0
    number_copy = n
    while n > 0:
        ld = n % 10
        sum = sum + ld ** 3
        n = n // 10
    if number_copy == sum:
        return True
    else:
        return False

def main():
    number = int(input("Enter a number: "))
    if isarmstrong(number):
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")

if __name__ == "__main__":
    main()





        
num = 8
while num > 1:
    if num == 5:
        num += 1
        continue
    print(num)
    
while True:
    number = int(input("enter a value: "))
    if number > 0:
        sum = sum + number
        continue
print("end")