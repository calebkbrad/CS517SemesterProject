#! /usr/bin/env python3

import sys

"""
Module to perform linear interpolation on parsed CPU temperature data

"""

from pre_process import process_data


def interpolate(temp1: float, temp2: float, upper_time: float):
    """
    Function to interpolate on two temps, returning a tuple of C0 and C1 represnting the
    line between the two points. Currently uses fixed x_difference of 30 since it is 
    consistent over all data

    Args: 
        temp1 (float): the first temp value to interpolate on
        temp2 (float): the second temp value to interpolat on

    Returns:
        A tuple with C0 value in first position, C1 value in second position
    """
    x_difference = 30.0

    slope = (temp2 - temp1) / x_difference
    intercept = temp2 - (slope * upper_time)

    return (intercept, slope)

def generate_one_line(temp1: float, temp2: float, upper_time: float, iter: int) -> str:
    x_difference = 30.0
    lower_time = upper_time - x_difference
    intercept, slope = interpolate(temp1, temp2, upper_time)
    return f"{int(lower_time):>6d} <= x < {int(upper_time):>6d}; y_{int(iter):<7d}= {intercept:>13.4f} + {slope:>10.4f}x; interpolation"

def main(arg):
    intercept, slope = interpolate(0.0, 61.0, 30)
    print(generate_one_line(0.0, 61.0, 30, 0))

if __name__ == "__main__":
    main(sys.argv[1:])