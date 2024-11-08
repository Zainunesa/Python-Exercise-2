# Question 1: Arithmetic and Assignment Operators

# TODO: Add 3 to x using the += operator
x = 3
x += 3
x  = x +3
# TODO: Multiply y by 2 using the *= operator
y = 2
y *=2
y= y*2
# TODO: Divide x by y and store the result in a variable called 'result'
result = x/y
# TODO: Print the value of 'result'
print(result)
#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators

# TODO: Create a condition that checks if a is greater than b
a > b


# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
b % 2 == 0

# TODO: Create a condition that checks if c is less than or equal to a
c <= a

# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a
final_condition = ( a > b or (b % 2 and c <= a))
# TODO: Print the value of 'final_condition'
print(final_condition)
#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
Score = int(input("Enter your test score: "))
# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F
if Score >= 90 and Score <= 100:
    print("You got an A")
elif Score >= 80 and Score <= 89:
    print("You got a B")
elif Score >= 70 and Score <= 79:
    print("You got a C")
elif Score >= 60 and Score <= 69:
    print("You got a D")
else: 
    Score <= 60
    print("You got an F")

# TODO: Print the grade for the given score
#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
numb1 = int(input("Enter a number: "))
numb2 = int(input("Enter a number: "))
# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation = input("Enter an operation, either (+, -, *, /): ")
# TODO: Use conditional statements to perform the chosen operation on num1 and num2
#answer = 0 (revision extra answer)**********
if operation == '+':
    answer = numb1 + numb2
    print(answer)
    #answer = numb1 + numb2 (revision extra answer)**********
elif operation == '-':
    answer = numb1 - numb2
    print(answer)
elif operation == '*':
    answer = numb1 / numb2
    print(answer)
elif operation == '/':
    answer = numb1 / numb2
    print(answer)


# TODO: Handle the case of division by zero
numb1 = int(input("Enter a number: "))
numb2 = int(input("Enter a number: "))

operation = input("Enter an operation, either (+, -, *, /): ")

if operation == '+':
    answer = numb1 + numb2
    print(answer)
elif operation == '-':
    answer = numb1 - numb2
    print(answer)
elif operation == '*':
    answer = numb1 * numb2
    print(answer)
elif operation == '/':
    if numb2 == 0:
         print("Error")
    else: 
        answer = numb1 / numb2
        print(answer)
# TODO: Print the result of the operation
print(answer)