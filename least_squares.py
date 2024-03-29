#! /usr/bin/env python3

import sys

"""
Module to perform least squares approximation on parsed CPU temperature data
Uses C0 and C1 formula derived in class to bypass need for a matrix solver
"""

from pre_process import process_data

def compute_sums(times: list[int], temps: list[int]) -> tuple:

    """
    Compute the sums needed to plug in for C0 and C1 equations

    Args:
        times (list): List of all time (x) values    
        temps (list): List of all corresponding temp (f(x)) values

    Returns:
        A tuple containing all 4 sums required for least squares computation
    """
    x_sum = 0.0
    x_sq_sum = 0.0
    f_sum = 0.0
    xf_sum = 0.0

    for time in times:
        x_sum += time
    for time in times:
        x_sq_sum += time ** 2
    for temp in temps:
        f_sum += temp
    for time, temp in zip(times, temps):
        xf_sum += time * temp
    
    return (x_sum, x_sq_sum, f_sum, xf_sum)

def compute_approximation(times: list[int], temps: list[int]) -> tuple:
    """
    Compute the least squares approximation using the equations for C0 and C1 derived during lecture

    Args:
        times (list): List of all time (x) values    
        temps (list): List of all corresponding temp (f(x)) values

    Returns:
        Tuple containing C0 and C1 values
    """
    x_sum, x_sq_sum, f_sum, xf_sum = compute_sums(times, temps)
    n = len(times)
    denom = (n * x_sq_sum) - x_sum ** 2

    c0 = ((x_sq_sum * f_sum) - (x_sum * xf_sum)) / denom
    c1 = ((n * xf_sum) - (x_sum * f_sum)) / denom

    return (c0, c1)

def generate_approximation_line(times: list[int], temps: list[int]):
    """
    Generates a line of least squares approximation for one core

    Args:
        times (list): List of all time (x) values    
        temps (list): List of all corresponding temp (f(x)) values

    Returns:
        Properly formatted line of data representing the equation of the line calculated through least squares approximation
    """
    lower_time = times[0]
    upper_time = times[-1]

    c0, c1 = compute_approximation(times, temps)

    return f"{lower_time:>6d} <= x < {upper_time:>6d}; y_{0:<7d}= {c0:>13.4f} + {c1:>10.4f}x; least squares approximation"


def main(argv):
    try:
        times, cores_data = process_data(argv[0])
    except:
        print("Please provide a valid input input file")
        sys.exit(1)
    for core in cores_data:
        print(generate_approximation_line(times, core))

if __name__ == "__main__":
    main(sys.argv[1:])