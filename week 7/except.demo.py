def generate_value():
    number = int(input("enter an integer: "))

    if number < 0 or number > 10:
        raise ValueError("this value is not correct")
    return number

try:
    generate_value()

except ValueError :
    print("test")