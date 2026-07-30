'''student_age = 21                    # Integer
student_percentage = 78.5           # Float
student_name = "Anjani"             # String
is_graduated = True                 # Boolean
student_skills = ["Python", "SQL", "HTML"]  # List

print("TASK 1")
print("Age:", student_age)
print("Percentage:", student_percentage)
print("Name:", student_name)
print("Graduated:", is_graduated)
print("Skills:", student_skills)




def swap_values(a, b):
    a, b = b, a
    return a, b


print("\nTASK 2")

x = 10
y = 20

print("Before swapping:")
print("x =", x)
print("y =", y)

x, y = swap_values(x, y)

print("After swapping:")
print("x =", x)
print("y =", y)



print("\nTASK 3 - SIMPLE CALCULATOR")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero"

else:
    result = "Invalid operator"

print("Result:", result)





print("\nTASK 4 - VARIABLE SCOPE")

def outer_function():
    message = "Hello"

    def inner_function():
        nonlocal message
        message = "Hello Anjani"
        print("Inside inner function:", message)

    print("Before inner function:", message)

    inner_function()

    print("After inner function:", message)


outer_function()'''



print("\nTASK 5 - FORMATTED STRING")

name = input("Enter your name: ")
age = input("Enter your age: ")
location = input("Enter your location: ")

formatted_message = f"My name is {name}. I am {age} years old and I live in {location}."

print(formatted_message)