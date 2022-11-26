#! /usr/bin/env python3

import sys

"""
Module to compute all calculations for the project.
Current implementations include piecewise linear interpolation and least squares approximation
"""

from pre_process import process_data
from linear_interpolation import generate_one_line
from least_squares import generate_approximation_line

def write_core_computations(times: list[int], temps: list[int], core_num: int):
    """
    Writes all computations of a single core to an output file

    Args:
        times (list): List of time increments of for each reading
        temps (list): List of the temperature readings for a single core
        core_num (int): A number associated with the core for unique file names for multiple cores
    """
    filename = f'output_core_{core_num}.txt'

    with open(filename, 'w') as core_output:
        for iter, time in enumerate(times):
            if iter == len(times) - 1:
                break
            line = generate_one_line(temps[iter], temps[iter+1], time, iter)
            core_output.write(line + '\n')
        approx_line = generate_approximation_line(times, temps)
        core_output.write(approx_line + '\n')

def write_all_core_computations(times: list[int], cores_data: list[list[int]]):
    """
    Writes the computations of all cores to separate output files

    Args:
        times (list): List of time increments for each reading
        cores_data (list): List of lists containing temp readings for each core
    """
    for core_num, core_data in enumerate(cores_data):
        write_core_computations(times, core_data, core_num)

def main(argv):
    try:
        times, cores_data = process_data(argv[0])
    except:
        print("Please provide a valid input input file")
        sys.exit(1)
    
    write_all_core_computations(times, cores_data)
    print('All calculations completed successfully')

if __name__ == "__main__":
    main(sys.argv[1:])