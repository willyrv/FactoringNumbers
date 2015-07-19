#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 11:18:18 2015

@author: willy
"""

import numpy as np

def naive_ffmethod(n):
    """
    Naive Fermat's Factorization method.
    Takes an integer n and return two factor in a tuple (c, d).
    If n is prime, then return (n, 1)
    """
    # The method is valid only if n is odd
    # Check if n is odd
    if n%2==0:
        return ((n/2, 2) if n>2 else (2, 1))
        
    factors = (n, 1)
    start = int(np.trunc(np.sqrt(n)) + 1)
    end = int(np.true_divide(n+1, 2) + 1)
    a = start
    while a < end:
        b_square = a**2 - n
        b = np.sqrt(b_square)
        if np.trunc(b) == b: # If b is a perfect square
            return (int(a+b), int(a-b))
        a+=1
    return factors
    
if __name__ == "__main__":
    f_in = open('./input.txt', 'r')
    f_out = open('./output.txt', 'w')
    #lines = f_in.readlines()
    n = f_in.readline()
    while n != '':
        factors = naive_ffmethod(int(n))
        f_out.write("{}; {}\n".format(factors[0], factors[1]))
        n = f_in.readline()
    f_in.close()
    f_out.close()
