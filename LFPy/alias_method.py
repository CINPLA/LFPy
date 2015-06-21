#!/usr/bin/env python
from time import time
import numpy as np

def alias_method(idx, area, nsyn):
    '''
    Alias method for drawing random numbers from a discrete probability
    distribution. See http://www.keithschwarz.com/darts-dice-coins/
    
    Arguments
    ::
        
        idx : np.ndarray
            compartment indices as array of ints
        area : np.ndarray
            compartment areas as array of floats
        nsyn : int
            number of randomized compartment indices
            
    
    Returns
    ::
        
        out : np.ndarray
            integer array of randomly drawn compartment indices
            
    '''
    # Construct the table.
    J, q = alias_setup(area)
     
    #output array
    spc = np.zeros(nsyn, dtype=int)
    
    #prefetch random numbers, alias_draw needs nsyn x 2 numbers
    rands = np.random.rand(nsyn, 2)
    
    K = J.size 
    # Generate variates using alias draw method
    for nn in range(nsyn):
        kk = np.floor(rands[nn, 0]*K)
        if rands[nn, 1] < q[kk]:
            spc[nn] = idx[kk]
        else:
            spc[nn] = idx[J[kk]]
        
    return spc


def alias_setup(area):
    '''
    Set up function for alias method.
    See http://www.keithschwarz.com/darts-dice-coins/
    
    Arguments
    ::
        
        area : np.ndarray
            float array of compartment areas
    
    Returns
    ::
        
        J : np.ndarray
            array of ints
        q : np.ndarray
            array of floats
    '''        
    K = area.size
    q = area*K
    J = np.zeros(K, dtype=int)

    # Sort the data into the outcomes with probabilities
    # that are larger and smaller than 1/K.
    smaller = np.zeros(K, dtype=int)
    larger = np.zeros(K, dtype=int)
    s_i = 0
    l_i = 0
    for kk in range(K):
        if q[kk] < 1:
            smaller[s_i] = kk
            s_i += 1
        else:
            larger[l_i] = kk
            l_i += 1
            
    s_i -= 1
    l_i -= 1
    
    # Loop though and create little binary mixtures that
    # appropriately allocate the larger outcomes over the
    # overall uniform mixture.
    while s_i > 0 and l_i > 0:
        small = smaller[s_i]
        large = larger[l_i]
        
        J[small] = large
        q[large] = q[large] + q[small] - 1

        s_i -= 1
    
        if q[large] < 1:
            s_i += 1
            l_i -= 1
            smaller[s_i] = large
 
    return J, q
