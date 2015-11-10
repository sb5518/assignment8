__author__ = 'sb5518'

""" Return of Investment simulation program.

The purpose of this program is to generate investment simulations based on user input.

The program will ask user to input the number of shares that he/she wants to buy. The number of shares must be a divisor
 of 1000,
which is the total amount to invest.

The program will ask for user input at once, and will run a simulation for each of those inputs. The user must enter at
least 1 positions input, but can enter more of them.
When the user does not want to enter more position values, he/she must enter "No", which is the only way to continue
with the program.

If input of user is negative, not an integer, or not a divisor of 1000, he/she will be asked for input again.

After the user decided all the different positions that he/she wants to simulate, the program will ask the user to input
 a number of simulations/days

Again, the input has to be integer, and positive.

Afterwards, the simulation will run, and histograms about distributions as well as Mean and STD will be written in a
file (as requested by homework)"""

import simulation

list_of_positions = list()
is_input_correct = False

while is_input_correct == False:    #Loop until we get a valid list of numbers of shares

    try:
        user_input = raw_input("Please enter a number of positions you want to have."
                               " The number must be a divisor of 1000 ")
        user_input = int(user_input)

        if (1000 % user_input) > 0:
                print "The number is not a divisor of 1000"
        elif user_input < 0:
                print "The number is not positive."
        elif user_input > 1000:
                print "The number must be smaller or equal to 1000"
        else:
            is_input_correct = True
            list_of_positions.append(user_input)

    except (KeyboardInterrupt, EOFError): #avoid interrupting the program
        continue
    except ValueError: #This catches when the user enters a string that is not an integer number, or a float.
        print('Please enter a number. It must be an integer')

user_input_2 = 'Hey'

while user_input_2 != 'No':

    try:
        user_input_2 = raw_input('Please enter another number of positions you want to have. The number must be a '
                                 'divisor of 1000. \nIf you do not want to simulate another number of positions, '
                                 'please write "No" ')

        if user_input_2 == 'No':
            continue
        else:
            user_input_2 = int(user_input_2)
            if (1000 % user_input_2) > 0:
                print "The number is not a divisor of 1000"
            elif user_input_2 < 0:
                print "The number is not positive."
            elif user_input_2 > 1000:
                print "The number must be smaller or equal to 1000"
            else:
                list_of_positions.append(user_input_2)

    except (KeyboardInterrupt, EOFError): #avoid interrupting the program
        continue
    except ValueError: #This catches when the user enters a string that is not an integer number, or a float.
        print('Please enter a number. It must be an integer')

is_input_correct = False
number_of_trials = 0

while is_input_correct == False:

    try:
        user_input_3 = raw_input("Please enter a number of Trials that you want to simulate. ")
        user_input_3 = int(user_input_3)

        if user_input_3 == 0:
            print "The number of trials has to be greater than 0"
        elif user_input_3 < 0:
            print "The number is not positive."
        else:
            is_input_correct = True
            number_of_trials = user_input_3

    except (KeyboardInterrupt, EOFError): #avoid interrupting the program
        continue
    except ValueError:
        print('Please enter a number. It must be an integer') #This catches when the user enters a string that is not an integer number, or a float.

# Now with the list of positions and number of trials I run the simulations and create the informative files.

simulation.simulation_1.histogram_mean_std(list_of_positions, number_of_trials)
