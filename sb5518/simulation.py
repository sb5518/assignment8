__author__ = 'sb5518'

import numpy as np
import matplotlib.pyplot as plt

""" This class is used to store the functions to run simulation of the homework. It has three static functions.

The first one, one_day, just receives the position number and creates a list with all the positions and it's values.
Afterwards it simulates the results of one day trial based on a biased coin and stores the results in a list as well

The second one, multi_day_simulation, takes a position and a number of trials. It uses the number of trials to iterate the one_day function over and over with the position value.
Afterwards it calculates the ROI and store it in the daily_ret dictionary

THe third one, histogram_mean_std takes a list of positions numbers and a number of iterations. It uses the multi_day_simulation and run it for each
of the values of the positions list with a certain number of iterations. Afterwards, it calculates the STD and Mean for each of the positions number and store
them all together in a txt. file. Finally, it plots the histograms of the distributions of the simulations for each of the number of positions and store them separately in a different
pdf file.

It is important to clarify that this class theoretically accepts negative and float positions, which in reality we know it is not true. The assigment8 program will make
use of this class but only accepting integer and positive numbers to make it more realistic.

It is also important to clarify that if class receives a negative number for the number of trials, calculations will be made based on the
absolut number.

"""


class simulation_1:
    @staticmethod
    def one_day(position): #This first method, just receives input, calculate the position value and create a list of all the "stocks". Afterwards it simulates the outcomes for each of this stocks based on a biased coin

        try:
            total_money = 1000
            position_value = total_money/position
            list_of_investments = list()

            while total_money > 0:
                list_of_investments.append(position_value)
                total_money = total_money - position_value
            outcomes = list()

            for i in list_of_investments:
                biased_coin_simulation = np.random.randint(1, high=101)
                if biased_coin_simulation >49:
                    outcomes.append(i * 2)
                if biased_coin_simulation <50:
                    outcomes.append(0)
            cumu_ret = 0

            for i in outcomes:
                cumu_ret = cumu_ret + i

            return cumu_ret

        except TypeError:
            raise TypeError("Incorrect Data Type")
        except ArithmeticError as e:
            print "Error" + e

    @staticmethod
    def multi_day_simulation(num_trials, position): #This second methods, receives a position and a number of trials. It uses the one_day method to calculate the outcome of one particular trial, replicate this for n trials, and finally calculate the ROI and store it in a list

        try:
            daily_ret = dict()
            cumu_ret = dict()
            num_trials = abs(num_trials)
            for trial in range(num_trials):
                cumu_ret[trial] = float(simulation_1.one_day(position))
                daily_ret[trial] = (cumu_ret[trial]/1000) - 1
            return daily_ret

        except TypeError:
            raise TypeError("Incorrect Data Type")
        except ArithmeticError as e:
            print "Error" + e
        except LookupError:
            print "Lookup error"

    @staticmethod
    def histogram_mean_std(positions_list, trials_number): #This last method executes the multi_day_simulation for each number of positions that the user inputs and a number of simulations. Then calculates the STD and Mean of each of the simulations and store them all togheter on a txt. It also plots a histogram of the distribution of each simulation and saves each of them in a separate pdf. file

        try:
            results_file = open ('results.txt', 'w')

            for position in positions_list:
                trial_results = simulation_1.multi_day_simulation(trials_number, position).values()
                plt.hist(trial_results, 100, range=[-1, 1])
                plt.savefig("histogram_" + str(position).zfill(4) + "_pos.pdf")
                plt.close()
                trial_results_array = np.array(trial_results)
                results_file.write("Position: " + str(position))
                results_file.write('\n')
                results_file.write("Mean: " + str(trial_results_array.mean()))
                results_file.write('\n')
                results_file.write("Standard Deviation: " + str(trial_results_array.std()))
                results_file.write('\n')

            results_file.close()

        except TypeError:
            raise TypeError("Incorrect Data Type")
        except IOError:
            print "Error with files creation. Please check your file system"
        except ArithmeticError as e:
            print "Error" + e


