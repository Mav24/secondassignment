"""
Assignment 4 part 2

Begin by executing this script from the command line by typing
    '$ python assignment_4_part2_murray_duke.py'
"""


numer_of_trys = 0
while numer_of_trys < 3:
    try:
        user_pin = int(input('Please enter your PIN: '))
        
    except ValueError:
        print('Please enter a numeric value!')
        continue
    
    if user_pin == 1234:
        print('Your account balcance is: $100.00 Goodbye!')
        break
    else:
        print('\nInvalid pin!')
        numer_of_trys += 1
        continue
if numer_of_trys == 3:
    print('\nAccount locked. The police are on their way!')

    