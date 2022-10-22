#! /usr/bin/env python3

import sys

"""
Module to perform linear interpolation on parsed CPU temperature data

"""

from pre_process import process_data


def interpolate(temp1: float, temp2: float, lower_time: float):
    """
    Function to interpolate on two temps, returning a tuple of C0 and C1 represnting the
    line between the two points. Currently uses fixed x_difference of 30 since it is 
    consistent over all data

    Args: 
        temp1 (float): the first temp value to interpolate on
        temp2 (float): the second temp value to interpolate on
        upper_time (float): upper bound for time value (always a multiple of 30)

    Returns:
        A tuple with C0 value in first position, C1 value in second position
    """
    x_difference = 30.0
    upper_time = lower_time + x_difference
    slope = (temp2 - temp1) / x_difference
    intercept = temp2 - (slope * upper_time)

    return (intercept, slope)

def generate_one_line(temp1: float, temp2: float, lower_time: float, iter: int) -> str:
    """
    Generate a single line of interpolation output, given args necessary to compute

    Args:
        temp1 (float): the first temp value to interpolate on
        temp2 (float): the second temp value to interpolate on
        upper_time (float): upper bound for time value (always a multiple of 30)
        iter (int): current iteration of loop
    """
    x_difference = 30.0
    upper_time = lower_time + x_difference
    intercept, slope = interpolate(temp1, temp2, lower_time)
    return f"{int(lower_time):>6d} <= x < {int(upper_time):>6d}; y_{int(iter):<7d}= {intercept:>13.4f} + {slope:>10.4f}x; interpolation"

def write_core_interpolation(times: list[int], temps: list[int], core_num: int):
    """
    Write the interpolations of a single core to an output file

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

def write_all_core_interpolations(times: list[int], cores_data: list[list]):
    """
    Write the interpolations of every core in an input file

    Args:
        times (list): List of time increments for each reading
        cores_data (list): List of lists containing temp readings for each core
    """
    for core_num, core_data in enumerate(cores_data):
        write_core_interpolation(times, core_data, core_num)
    

def main(arg):
    try:
        times, cores_data = process_data(arg[0])
    except:
        print("Please provide a valid input input file")
        sys.exit(1)
    
    write_all_core_interpolations(times, cores_data)

if __name__ == "__main__":
    main(sys.argv[1:])