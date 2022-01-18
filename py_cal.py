print("Option 1 is Addition ")
print("Option 2 is Substraction")
print("Option 3 is Multiplication")
print("Option 4 is Division")

Option = (input('Enter your choice option: '))

num1 = float(input('Enter a number: '))
num2 = float(input('Enter a second number: '))

if Option == '1':
    print(num1, '+', num2 ,' = ', (num1+num2))
elif Option == '2':
    print(num1, '-', num2, ' = ', (num1-num2))
elif Option == '3':
    print(num1, ' * ', num2, ' = ', (num1*num2))
elif Option == '4':
    print(num1, ' / ', num2, ' = ', (num1/num2))
else:
    print('Invalid option')