#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is an example scripts using LFPy with a passive cell model adapted from
Mainen and Sejnowski, Nature 1996, for the original files, see
http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=2488

Here, excitatory and inhibitory neurons are distributed on different parts of
the morphology, with stochastic spike times produced by the
NEURON's NetStim objects associated with each individual synapse.

Otherwise the same as "example6.py", without the active conductances

Copyright (C) 2017 Computational Neuroscience Group, NMBU.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""

# importing some modules, setting some matplotlib values for pl.plot.
import LFPy
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size' : 12,
                     'figure.facecolor' : '1',
                     'figure.subplot.wspace' : 0.5,
                     'figure.subplot.hspace' : 0.5})

#seed for random generation
np.random.seed(1234)

################################################################################
# A couple of function declarations
################################################################################

def insert_synapses(synparams, section, n, netstimParameters):
    '''find n compartments to insert synapses onto'''
    idx = cell.get_rand_idx_area_norm(section=section, nidx=n)

    #Insert synapses in an iterative fashion
    for i in idx:
        synparams.update({'idx' : int(i)})

        # Create synapse(s) and setting times using the Synapse class in LFPy
        s = LFPy.Synapse(cell, **synparams)
        s.set_spike_times_w_netstim(**netstimParameters)

################################################################################
# Define parameters, using dictionaries
# It is possible to set a few more parameters for each class or functions, but
# we chose to show only the most important ones here.
################################################################################

#define cell parameters used as input to cell-class
cellParameters = {
    'morphology' : 'morphologies/L5_Mainen96_wAxon_LFPy.hoc',
    'cm' : 1.0,                 # membrane capacitance
    'Ra' : 150,                 # axial resistance
    'v_init' : -65,             # initial crossmembrane potential
    'passive' : True,           # switch on passive mechs
    'passive_parameters' : {'g_pas' : 1./30000, 'e_pas' : -65}, # passive params    
    'nsegs_method' : 'lambda_f',# method for setting number of segments,
    'lambda_f' : 100,           # segments are isopotential at this frequency
    'dt' : 2**-4,               # dt of LFP and NEURON simulation.
    'tstart' : -100,          #start time, recorders start at t=0
    'tstop' : 200,            #stop time of simulation
    #'custom_code'  : ['active_declarations_example3.hoc'], # will run this file
}

# Synaptic parameters taken from Hendrickson et al 2011
# Excitatory synapse parameters:
synapseParameters_AMPA = {
    'e' : 0,                    #reversal potential
    'syntype' : 'Exp2Syn',      #conductance based exponential synapse
    'tau1' : 1.,                #Time constant, rise
    'tau2' : 3.,                #Time constant, decay
    'weight' : 0.005,           #Synaptic weight
    'record_current' : True,    #record synaptic currents
}
# Excitatory synapse parameters
synapseParameters_NMDA = {         
    'e' : 0,
    'syntype' : 'Exp2Syn',
    'tau1' : 10.,
    'tau2' : 30.,
    'weight' : 0.005,
    'record_current' : True,
}
# Inhibitory synapse parameters
synapseParameters_GABA_A = {         
    'e' : -80,
    'syntype' : 'Exp2Syn',
    'tau1' : 1.,
    'tau2' : 12.,
    'weight' : 0.005,
    'record_current' : True
}
# where to insert, how many, and which input statistics
insert_synapses_AMPA_args = {
    'section' : 'apic',
    'n' : 100,
    'netstimParameters': {
        'number' : 1000,
        'start' : 0,
        'noise' : 1,
        'interval' : 20,
    }
}
insert_synapses_NMDA_args = {
    'section' : ['dend', 'apic'],
    'n' : 15,
    'netstimParameters': {
        'number' : 1000,
        'start' : 0,
        'noise' : 1,
        'interval' : 90,
    }
}
insert_synapses_GABA_A_args = {
    'section' : 'dend',
    'n' : 100,
    'netstimParameters': {
        'number' : 1000,
        'start' : 0,
        'noise' : 1,
        'interval' : 20,
    }
}

# Define electrode geometry corresponding to a laminar electrode, where contact
# points have a radius r, surface normal vectors N, and LFP calculated as the
# average LFP in n random points on each contact:
N = np.empty((16, 3))
for i in range(N.shape[0]): N[i,] = [1, 0, 0] #normal unit vec. to contacts
# put parameters in dictionary
electrodeParameters = {
    'sigma' : 0.3,              # Extracellular potential
    'x' : np.zeros(16) + 25,      # x,y,z-coordinates of electrode contacts
    'y' : np.zeros(16),
    'z' : np.linspace(-500, 1000, 16),
    'n' : 20,
    'r' : 10,
    'N' : N,
}

# Parameters for the cell.simulate() call, recording membrane- and syn.-currents
simulationParameters = {
    'rec_imem' : True,  # Record Membrane currents during simulation
}

################################################################################
# Main simulation procedure
################################################################################

#Initialize cell instance, using the LFPy.Cell class
cell = LFPy.Cell(**cellParameters)

#Insert synapses using the function defined earlier
insert_synapses(synapseParameters_AMPA, **insert_synapses_AMPA_args)
insert_synapses(synapseParameters_NMDA, **insert_synapses_NMDA_args)
insert_synapses(synapseParameters_GABA_A, **insert_synapses_GABA_A_args)

#perform NEURON simulation, results saved as attributes in the cell instance
cell.simulate(**simulationParameters)

# Initialize electrode geometry, then calculate the LFP, using the
# LFPy.RecExtElectrode class. Note that now cell is given as input to electrode
# and created after the NEURON simulations are finished
electrode = LFPy.RecExtElectrode(cell, **electrodeParameters)
print('simulating LFPs....')
electrode.calc_lfp()
print('done')

#plotting some variables and geometry, saving output to .pdf.
from example_suppl import plot_ex3
fig = plot_ex3(cell, electrode)
fig.savefig('example8.pdf', dpi=300)
plt.show()