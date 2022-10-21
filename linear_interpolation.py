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


def main(arg):
    intercept, slope = interpolate(0.0, 61.0, 30)
    print('{0:.8f}'.format(slope))

if __name__ == "__main__":
    main(sys.argv[1:])