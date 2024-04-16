#FIRST attempt. Funny output. It's giving me location in memory

# print('Welcome to my calculator!')
# print()
# first_num = int(input('Enter the first number: '))
# second_num = int(input('Enter the second number: '))

# def add(first_num, second_num):
#     return(first_num + second_num)

# def subtract(first_num, second_num):
#     return(first_num - second_num)

# def multiply(first_num, second_num):
#     return(first_num * second_num)

# def divide(first_num, second_num):
#     return(first_num / second_num)

# while True:
#     op_choice = input("Chose an operation OR enter 'q' to quit ( + , - , * , / ) ")
#     if op_choice == '+':
#         print('The answer is', add)
#     elif op_choice == '-':
#         print('The answer is', subtract)
#     elif op_choice == '*':
#         print('The answer is', multiply)
#     elif op_choice == '/':
#         print('The answer is', divide)
#     else:
#         print('Thanks for using this calculator!')
  
#SECOND attempt. Names of the functions were wrong, corrected them. Works fine. 

print('Welcome to my calculator!')
print() #cosmetic

def add(first_num, second_num):
    return(first_num + second_num)

def subtract(first_num, second_num):
    return(first_num - second_num)

def multiply(first_num, second_num):
    return(first_num * second_num)

def divide(first_num, second_num):
    if second_num != 0: #allows all numbers EXCEPT '0' to return the quotient
        return(first_num / second_num)
    else:
        return 'You can not divide by 0'

while True:
    first_num = int(input('Enter the first number: '))  #moved both of these down in order to get new entries after every calculation
    second_num = int(input('Enter the second number: '))    #moved both of these down in order to get new entries after every calculation
    op_choice = input("Chose an operation OR enter 'q' to quit ( + , - , * , / ) ")
    
    if op_choice == '+':
        print('The answer is', add(first_num, second_num))
    elif op_choice == '-':
        print('The answer is', subtract(first_num, second_num))
    elif op_choice == '*':
        print('The answer is', multiply(first_num, second_num))
    elif op_choice == '/':
        if divide(first_num, second_num) == 'You can not divide by 0':  #wordy but makes for cleaner output imo
            print('You can not divide by 0!')
        else:
            print('The answer is', divide(first_num, second_num))
    elif op_choice == 'q':
        print('Thanks for using the calculator!')
        break
    else:
        print('Invalid entry')