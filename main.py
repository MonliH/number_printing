
def print_digits(integer):
    num=str(integer) # turn the integer into a string
    if num=='': # base case: there is no number in the certain string
        print()
        print()
        return
    else:
        print(num[-1], end="") # print the last number first
        print_digits(num[:-1])
        return

def even_or_odd(number): # don't use recursion
    if number % 2 == 1:
        return False
    elif number % 2 == 0:
        return True

def odd_or_even(number): # use recursion
    if number==0:
        return True
    elif number==1:
        return False
    else:
        if number>0:
            return odd_or_even(number-2)
        else:
            return odd_or_even(number+2)

def print_asterisks(n):
    if n==1: #base case: only one asterisk in the first line
        return '*'
    else:
        return print_asterisks(n-1)+'\n'+'*'*n #remember to change the line every time finishing printing one line of asterisks

def raise_power(num,exponent): #num**power=num*num**(power-1)
    if exponent==0: #base case: when power equals to 0
        return 1
    else:
        return num*raise_power(num,exponent-1)

def menu():
    #print the menu
    print('(1)Print a digit reversed.')
    print('(2)Judge if a number is even(non-recursion)')
    print('(3)Judge if a number is even(recursion)')
    print('(4)Print asterisks at the same number of the line.')
    print('(5)Raise a number to a certain power.')
    print('(6)Exit')
    #Let the user give option
    function = str(input('\nWhat function do you want to run?(Hint: Enter 1 or 2 or 3 or 4 or 5 or 6)'))
    if function=='1':
        integer=input('What integer do you want to reverse?')
        newInteger=print_digits(integer)
        menu() #run the function again
    elif function=='2':
        number=int(input('What is the number you want to judge?'))
        result=even_or_odd(number)
        print(result)
        menu()
    elif function=='3':
        number=int(input('What is the number you want to judge?'))
        result=even_or_odd(number)
        print(result)
        menu()
    elif function=='4':
        n=int(input('How many lines of asterisks do you want to print?'))
        asterisks=print_asterisks(n)
        print(asterisks)
        menu()
    elif function=='5':
        num=int(input('What is the number to be raised?'))
        exponent=int(input('What is the exponent?'))
        result_number=raise_power(num,exponent)
        print('The result is',result_number)
        menu()
    elif function=='6':
        print('Done.') #finish the function
    else:
        print("Enter a number between 1 and 6")
        menu()
menu()
