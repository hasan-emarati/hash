def function1():
    # Code for function 1
    print('Function 1 is running')

def function2():
    # Code for function 2
    print('Function 2 is running')

while True:
    print('Please select a function:')
    print('1. Function 1')
    print('2. Function 2')
    choice = input('Enter your choice (1/2): ')
    if choice == '1':
        function1()
        break
    elif choice == '2':
        function2()
        break
    else:
        print('Invalid choice, please try again')