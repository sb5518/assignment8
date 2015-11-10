__author__ = 'sb5518'
import unittest
from unittest import TestCase
import simulation
import os

class test_histograms_and_files(TestCase):

    def test_plot(self):
        try:
            os.remove('./histogram_0001_pos.pdf')
            os.remove('./histogram_0010_pos.pdf')
            os.remove('./histogram_0100_pos.pdf')
            os.remove('./histogram_1000_pos.pdf')
        except OSError:
            pass

        positions_list = (1, 10, 100, 1000)
        number_trials = 10000
        simulation.simulation_1.histogram_mean_std(positions_list, number_trials)

        self.assertTrue(os.path.isfile('./histogram_0001_pos.pdf'))
        self.assertTrue(os.path.isfile('./histogram_0001_pos.pdf'))
        self.assertTrue(os.path.isfile('./histogram_0001_pos.pdf'))
        self.assertTrue(os.path.isfile('./histogram_0001_pos.pdf'))

    def test_plot(self):
        try:
            os.remove('./results.txt')
        except OSError:
            pass

        positions_list = (1, 5, 10)
        number_trials = 100
        simulation.simulation_1.histogram_mean_std(positions_list, number_trials)
        self.assertTrue(os.path.isfile('./results.txt'))