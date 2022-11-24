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

def compute_approximation(times: list[int], temps: list[int]) -> str:
    """
    Compute the least squares approximation using the equations for C0 and C1 derived during lecture

    Args:
        times (list): List of all time (x) values    
        temps (list): List of all corresponding temp (f(x)) values


    """
    x_sum, x_sq_sum, f_sum, xf_sum = compute_sums(times, temps)
    n = len(times)
    denom = (n * x_sq_sum) - x_sum ** 2

    c0 = ((x_sq_sum * f_sum) - (x_sum * xf_sum)) / denom
    c1 = ((n * xf_sum) - (x_sum * f_sum))

    return (c0, c1)

def main(argv):
    times, cores_data = process_data(argv[0])
    # x_sum, x_sq_sum, f_sum, xf_sum = compute_sums(times, cores_data[0])
    # print(x_sum)
    # print(x_sq_sum)
    # print(f_sum)
    # print(xf_sum)
    c0, c1 = compute_approximation(times, cores_data[0])
    print(c0)
    print(c1)

if __name__ == "__main__":
    main(sys.argv[1:])