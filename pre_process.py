#! /usr/bin/env python3

"""
Module to pre-process the data from an input file for CPU Temperatures project in
a form that can be used for later piecewise linear interpolation and 
least squares approximation
"""

from parse_temps import parse_raw_temps

 

def process_data(valid_input_file: str) -> tuple:

    """
    Processes temperature data in an input file into a tuple where
    the first element is the list of times and the second element
    is a list containing a list for each core

    Args:
        valid_input_file (str): a valid file path to an input file with CPU temps for
        four cores

    Returns:
        A tuple with a list of times as the first element, and a list of lists containing
        data for each core
    """
    with open(valid_input_file, 'r') as temps_file:
            times = []
            core_data = [[] for _ in range(0, 4)]

            for time, raw_core_data in parse_raw_temps(temps_file):
                times.append(time)
                for core_idx, reading in enumerate(raw_core_data):
                    core_data[core_idx].append(reading)

    return (times, core_data)

