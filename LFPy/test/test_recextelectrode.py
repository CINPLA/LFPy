#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyright (C) 2012 Computational Neuroscience Group, NMBU.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

"""

from __future__ import division
import os
import unittest
import numpy as np
from scipy.integrate import quad
from scipy import real, imag
import LFPy
import neuron

# for nosetests to run load the SinSyn sinusoid synapse currrent mechanism
neuron.load_mechanisms(os.path.join(LFPy.__path__[0], 'test'))

class testRecExtElectrode(unittest.TestCase):
    """
    test class LFPy.RecExtElectrode
    """

    def test_method_pointsource(self):
        #create LFPs using LFPy-model
        LFP_LFPy = stickSimulation(method='pointsource')
    
        #create LFPs using the analytical approach
        time = np.linspace(0, 100, 100*2**6+1)
        R = np.ones(11)*100
        Z = np.linspace(1000, 0, 11)
    
        LFP_analytic = np.empty((R.size, time.size))
        for i in range(R.size):
            LFP_analytic[i, ] = analytical_LFP(time, electrodeR=R[i],
                                                    electrodeZ=Z[i])
        np.testing.assert_allclose(LFP_analytic, LFP_LFPy, atol=1E-4)
    
    def test_method_linesource(self):
        #create LFPs using LFPy-model
        LFP_LFPy = stickSimulation(method='linesource')
    
        #create LFPs using the analytical approach
        time = np.linspace(0, 100, 100*2**6+1)
        R = np.ones(11)*100
        Z = np.linspace(1000, 0, 11)
    
        LFP_analytic = np.empty((R.size, time.size))
        for i in range(R.size):
            LFP_analytic[i, ] = analytical_LFP(time, electrodeR=R[i],
                                                    electrodeZ=Z[i])
        np.testing.assert_allclose(LFP_analytic, LFP_LFPy, atol=1E-4)

    
    def test_method_soma_as_point(self):
        #create LFPs using LFPy-model
        LFP_LFPy = stickSimulation(method='soma_as_point')
    
        #create LFPs using the analytical approach
        time = np.linspace(0, 100, 100*2**6+1)
        R = np.ones(11)*100
        Z = np.linspace(1000, 0, 11)
    
        LFP_analytic = np.empty((R.size, time.size))
        for i in range(R.size):
            LFP_analytic[i, ] = analytical_LFP(time, electrodeR=R[i],
                                                    electrodeZ=Z[i])
        np.testing.assert_allclose(LFP_analytic, LFP_LFPy, atol=1E-4)

    
    
    def test_method_pointsource_dotprodcoeffs(self):
        #create LFPs using LFPy-model
        LFP_LFPy = stickSimulationDotprodcoeffs(method='pointsource')
    
        #create LFPs using the analytical approach
        time = np.linspace(0, 100, 100*2**6+1)
        R = np.ones(11)*100
        Z = np.linspace(1000, 0, 11)
    
        LFP_analytic = np.empty((R.size, time.size))
        for i in range(R.size):
            LFP_analytic[i, ] = analytical_LFP(time, electrodeR=R[i],
                                                    electrodeZ=Z[i])
        np.testing.assert_allclose(LFP_analytic, LFP_LFPy, atol=1E-4)

    
    def test_method_linesource_dotprodcoeffs(self):
        #create LFPs using LFPy-model
        LFP_LFPy = stickSimulationDotprodcoeffs(method='linesource')
    
        #create LFPs using the analytical approach
        time = np.linspace(0, 100, 100*2**6+1)
        R = np.ones(11)*100
        Z = np.linspace(1000, 0, 11)
    
        LFP_analytic = np.empty((R.size, time.size))
        for i in range(R.size):
            LFP_analytic[i, ] = analytical_LFP(time, electrodeR=R[i],
                                                    electrodeZ=Z[i])
        np.testing.assert_allclose(LFP_analytic, LFP_LFPy, atol=1E-4)

    
    def test_method_soma_as_point_dotprodcoeffs(self):
        #create LFPs using LFPy-model
        LFP_LFPy = stickSimulationDotprodcoeffs(method='soma_as_point')
    
        #create LFPs using the analytical approach
        time = np.linspace(0, 100, 100*2**6+1)
        R = np.ones(11)*100
        Z = np.linspace(1000, 0, 11)
    
        LFP_analytic = np.empty((R.size, time.size))
        for i in range(R.size):
            LFP_analytic[i, ] = analytical_LFP(time, electrodeR=R[i],
                                                    electrodeZ=Z[i])
        np.testing.assert_allclose(LFP_analytic, LFP_LFPy, atol=1E-4)

    
    def test_method_pointsource_contact_average_r10n100(self):
        #create LFPs using LFPy-model
        LFP_LFPy = stickSimulationAveragingElectrode(
            contactRadius=10, contactNPoints=100, method='soma_as_point')
    
        #create LFPs using the analytical approach
        time = np.linspace(0, 100, 100*2**6+1)
        R = np.ones(11)*100
        Z = np.linspace(1000, 0, 11)
    
        LFP_analytic = np.empty((R.size, time.size))
        for i in range(R.size):
            LFP_analytic[i, ] = analytical_LFP(time, electrodeR=R[i],
                                                    electrodeZ=Z[i])
        np.testing.assert_allclose(LFP_analytic, LFP_LFPy, atol=1E-4)

    
    def test_method_linesource_contact_average_r10n100(self):
        #create LFPs using LFPy-model
        LFP_LFPy = stickSimulationAveragingElectrode(
            contactRadius=10, contactNPoints=100, method='linesource')
    
        #create LFPs using the analytical approach
        time = np.linspace(0, 100, 100*2**6+1)
        R = np.ones(11)*100
        Z = np.linspace(1000, 0, 11)
    
        LFP_analytic = np.empty((R.size, time.size))
        for i in range(R.size):
            LFP_analytic[i, ] = analytical_LFP(time, electrodeR=R[i],
                                                    electrodeZ=Z[i])
        np.testing.assert_allclose(LFP_analytic, LFP_LFPy, atol=1E-4)

    
    def test_method_soma_as_point_contact_average_r10n100(self):
        #create LFPs using LFPy-model
        LFP_LFPy = stickSimulationAveragingElectrode(
            contactRadius=10, contactNPoints=100, method='soma_as_point')
    
        #create LFPs using the analytical approach
        time = np.linspace(0, 100, 100*2**6+1)
        R = np.ones(11)*100
        Z = np.linspace(1000, 0, 11)
    
        LFP_analytic = np.empty((R.size, time.size))
        for i in range(R.size):
            LFP_analytic[i, ] = analytical_LFP(time, electrodeR=R[i],
                                                    electrodeZ=Z[i])
        np.testing.assert_allclose(LFP_analytic, LFP_LFPy, atol=1E-4)

    def test_sigma_inputs(self):

        stickParams = {
            'morphology' : os.path.join(LFPy.__path__[0], 'test', 'stick.hoc'),
            'passive_parameters' : {'g_pas' : 1./30000, 'e_pas' : -65},
            'passive': True,
            'tstart' : 0,
            'tstop' : 20,
            'dt' : 2**-4,
            'nsegs_method' : 'lambda_f',
            'lambda_f' : 1000,

        }
        stick = LFPy.Cell(**stickParams)

        electrodeParams = {
            'sigma' : [0.3, 0.3, 0.3, 0.3],
            'x' : np.ones(11) * 100.,
            'y' : np.zeros(11),
            'z' : np.linspace(1000, 0, 11),
        }

        np.testing.assert_raises(ValueError, LFPy.RecExtElectrode, **electrodeParams)

    def test_bad_cell_position_in_slice(self):

        electrodeParams = {
            'sigma_T' : 0.3,
            'sigma_S' : 1.5,
            'sigma_G' : 0.0,
            'h': 200,
            'x' : np.linspace(0, 1000, 11),
            'y' : np.zeros(11),
            'z' : np.zeros(11),
            'method': "pointsource",
        }

        stickParams = {
            'morphology' : os.path.join(LFPy.__path__[0], 'test', 'stick.hoc'),
            'passive_parameters' : {'g_pas' : 1./30000, 'e_pas' : -65},
            'passive': True,
            'tstart' : -10,
            'tstop' : 20,
            'dt' : 2**-4,
            'nsegs_method' : 'lambda_f',
            'lambda_f' : 1000,

        }
        stick = LFPy.Cell(**stickParams)
        stick.set_rotation(y=np.pi/2)
        stick.simulate(rec_imem=True)

        stick.set_pos(z=-100)
        MEA = LFPy.RecMEAElectrode(stick, **electrodeParams)
        np.testing.assert_raises(RuntimeError, MEA.calc_lfp)

        stick.set_pos(z=300)
        MEA = LFPy.RecMEAElectrode(stick, **electrodeParams)
        np.testing.assert_raises(RuntimeError, MEA.calc_lfp)

    def test_sqeeze_cell_and_bad_position(self):

        electrodeParams = {
            'sigma_T' : 0.3,
            'sigma_S' : 1.5,
            'sigma_G' : 0.0,
            'h': 200,
            'x' : np.linspace(0, 1000, 11),
            'y' : np.zeros(11),
            'z' : np.zeros(11),
            'method': "pointsource",
            'squeeze_cell_factor': None,
        }

        stickParams = {
            'morphology' : os.path.join(LFPy.__path__[0], 'test', 'ball_and_sticks.hoc'),
            'passive_parameters' : {'g_pas' : 1./30000, 'e_pas' : -65},
            'passive': True,
            'tstart' : -10,
            'tstop' : 20,
            'dt' : 2**-4,
            'nsegs_method' : 'lambda_f',
            'lambda_f' : 1000,

        }
        stick = LFPy.Cell(**stickParams)
        stick.set_rotation(y=np.pi/2)
        stick.simulate(rec_imem=True)

        stick.set_pos(z=1)
        MEA = LFPy.RecMEAElectrode(stick, **electrodeParams)
        np.testing.assert_raises(RuntimeError, MEA.test_cell_extent)

        stick.set_pos(z=199)
        MEA = LFPy.RecMEAElectrode(stick, **electrodeParams)
        np.testing.assert_raises(RuntimeError, MEA.test_cell_extent)

        electrodeParams = {
            'sigma_T' : 0.3,
            'sigma_S' : 1.5,
            'sigma_G' : 0.0,
            'h': 200,
            'x' : np.linspace(0, 1000, 11),
            'y' : np.zeros(11),
            'z' : np.zeros(11),
            'method': "pointsource",
            'squeeze_cell_factor': 0.1,
        }

        stick.set_pos(z=-1)
        MEA = LFPy.RecMEAElectrode(stick, **electrodeParams)
        np.testing.assert_raises(RuntimeError, MEA.test_cell_extent)

        stick.set_pos(z=201)
        MEA = LFPy.RecMEAElectrode(stick, **electrodeParams)
        np.testing.assert_raises(RuntimeError, MEA.test_cell_extent)



    def test_isotropic_version_of_anisotropic_methods(self):

        stickParams = {
            'morphology' : os.path.join(LFPy.__path__[0], 'test', 'stick.hoc'),
            'passive_parameters' : {'g_pas' : 1./30000, 'e_pas' : -65},
            'passive': True,
            'tstart' : 0,
            'tstop' : 20,
            'dt' : 2**-4,
            'nsegs_method' : 'lambda_f',
            'lambda_f' : 1000,

        }
        stimParams = {
            'pptype' : 'SinSyn',
            'delay' : -100.,
            'dur' : 1000.,
            'pkamp' : 1.,
            'freq' : 100.,
            'phase' : -np.pi/2,
            'bias' : 0.,
            'record_current' : True
        }

        isotropic_electrodeParams = {
            'sigma' : 0.3,
            'x' : np.ones(11) * 100.,
            'y' : np.zeros(11),
            'z' : np.linspace(1000, 0, 11),
        }
        anisotropic_electrodeParams = isotropic_electrodeParams.copy()
        anisotropic_electrodeParams["sigma"] = [isotropic_electrodeParams["sigma"]] * 3


        methods = ["pointsource", "linesource", "soma_as_point"]

        for method in methods:
            isotropic_electrodeParams["method"] = method
            anisotropic_electrodeParams["method"] = method

            isotropic_electrode = LFPy.RecExtElectrode(**isotropic_electrodeParams)
            anisotropic_electrode = LFPy.RecExtElectrode(**anisotropic_electrodeParams)

            stick = LFPy.Cell(**stickParams)
            stick.set_pos(z=-stick.zstart[0])

            synapse = LFPy.StimIntElectrode(stick, stick.get_closest_idx(0, 0, 1000),
                                   **stimParams)
            stick.simulate([isotropic_electrode, anisotropic_electrode],
                           rec_imem=True, rec_vmem=True)

            np.testing.assert_allclose(isotropic_electrode.LFP,
                                       anisotropic_electrode.LFP)

    def test_compare_anisotropic_lfp_methods(self):

        stickParams = {
            'morphology' : os.path.join(LFPy.__path__[0], 'test', 'stick.hoc'),
            'passive_parameters' : {'g_pas' : 1./30000, 'e_pas' : -65},
            'passive': True,
            'tstart' : 0,
            'tstop' : 20,
            'dt' : 2**-4,
            'nsegs_method' : 'lambda_f',
            'lambda_f' : 1000,

        }
        stimParams = {
            'pptype' : 'SinSyn',
            'delay' : -100.,
            'dur' : 1000.,
            'pkamp' : 1.,
            'freq' : 100.,
            'phase' : -np.pi/2,
            'bias' : 0.,
            'record_current' : True
        }

        electrodeParams = {
            'sigma' : [0.3, 0.3, 0.45],
            'x' : np.array([0, 1000]),
            'y' : np.zeros(2),
            'z' : np.zeros(2),

        }

        ps_electrodeParams = electrodeParams.copy()
        ls_electrodeParams = electrodeParams.copy()
        sap_electrodeParams = electrodeParams.copy()

        ps_electrodeParams["method"] = "pointsource"
        ls_electrodeParams["method"] = "linesource"
        sap_electrodeParams["method"] = "soma_as_point"

        electrode_ps = LFPy.RecExtElectrode(**ps_electrodeParams)
        electrode_ls = LFPy.RecExtElectrode(**ls_electrodeParams)
        electrode_sap = LFPy.RecExtElectrode(**sap_electrodeParams)

        stick = LFPy.Cell(**stickParams)
        stick.set_pos(z=-stick.zstart[0])

        synapse = LFPy.StimIntElectrode(stick, stick.get_closest_idx(0, 0, 1000),
                               **stimParams)
        stick.simulate([electrode_ps, electrode_ls, electrode_sap],
                       rec_imem=True, rec_vmem=True)

        # Test that distant electrode is independent of choice of method
        np.testing.assert_almost_equal(electrode_ps.LFP[1,:],
                                   electrode_ls.LFP[1,:])

        np.testing.assert_almost_equal(electrode_ps.LFP[1,:],
                                   electrode_sap.LFP[1,:])

        # Hack to test that LFP close to stick is dependent on choice of method
        np.testing.assert_raises(AssertionError, np.testing.assert_array_equal,
                                 electrode_ps.LFP[0,:], electrode_ls.LFP[0,:])

        np.testing.assert_raises(AssertionError, np.testing.assert_array_equal,
                                 electrode_ps.LFP[0,:], electrode_sap.LFP[0,:])

######## Functions used by tests: ##############################################


def stickSimulation(method):
    stickParams = {
        'morphology' : os.path.join(LFPy.__path__[0], 'test', 'stick.hoc'),
        'cm' : 1,
        'Ra' : 150,
        'v_init' : -65,
        'passive' : True,
        'passive_parameters' : {'g_pas' : 1./30000, 'e_pas' : -65},
        'tstart' : -100,
        'tstop' : 100,
        'dt' : 2**-6,
        'nsegs_method' : 'lambda_f',
        'lambda_f' : 1000,

    }

    electrodeParams = {
        'sigma' : 0.3,
        'x' : np.ones(11) * 100.,
        'y' : np.zeros(11),
        'z' : np.linspace(1000, 0, 11),
        'method' : method
    }

    stimParams = {
        'pptype' : 'SinSyn',
        'delay' : -100.,
        'dur' : 1000.,
        'pkamp' : 1.,
        'freq' : 100.,
        'phase' : -np.pi/2,
        'bias' : 0.,
        'record_current' : True
    }


    electrode = LFPy.RecExtElectrode(**electrodeParams)

    stick = LFPy.Cell(**stickParams)
    stick.set_pos(z=-stick.zstart[0])

    synapse = LFPy.StimIntElectrode(stick, stick.get_closest_idx(0, 0, 1000),
                           **stimParams)
    stick.simulate(electrode, rec_imem=True, rec_vmem=True)

    return electrode.LFP

def stickSimulationAveragingElectrode(contactRadius, contactNPoints, method):
    stickParams = {
        'morphology' : os.path.join(LFPy.__path__[0], 'test', 'stick.hoc'),
        'cm' : 1,
        'Ra' : 150,
        'v_init' : -65,
        'passive' : True,
        'passive_parameters' : {'g_pas' : 1./30000, 'e_pas' : -65},
        'tstart' : -100,
        'tstop' : 100,
        'dt' : 2**-6,
        'nsegs_method' : 'lambda_f',
        'lambda_f' : 1000,

    }

    N = np.empty((11, 3))
    for i in range(N.shape[0]): N[i,] = [1, 0, 0] #normal unit vec. to contacts
    electrodeParams = {
        'sigma' : 0.3,
        'x' : np.ones(11) * 100.,
        'y' : np.zeros(11),
        'z' : np.linspace(1000, 0, 11),
        'r' : contactRadius,
        'n' : 10,
        'N' : N,
        'method' : method
    }

    stimParams = {
        'pptype' : 'SinSyn',
        'delay' : -100.,
        'dur' : 1000.,
        'pkamp' : 1.,
        'freq' : 100.,
        'phase' : -np.pi/2,
        'bias' : 0.,
        'record_current' : True
    }


    electrode = LFPy.RecExtElectrode(**electrodeParams)

    stick = LFPy.Cell(**stickParams)
    stick.set_pos(z=-stick.zstart[0])

    synapse = LFPy.StimIntElectrode(stick, stick.get_closest_idx(0, 0, 1000),
                           **stimParams)
    stick.simulate(electrode, rec_imem=True, rec_vmem=True)

    return electrode.LFP

def stickSimulationDotprodcoeffs(method):
    stickParams = {
        'morphology' : os.path.join(LFPy.__path__[0], 'test', 'stick.hoc'),
        'cm' : 1,
        'Ra' : 150,
        'v_init' : -65,
        'passive' : True,
        'passive_parameters' : {'g_pas' : 1./30000, 'e_pas' : -65},
        'tstart' : -100,
        'tstop' : 100,
        'dt' : 2**-6,
        'nsegs_method' : 'lambda_f',
        'lambda_f' : 1000,

    }

    electrodeParams = {
        'sigma' : 0.3,
        'x' : np.ones(11) * 100.,
        'y' : np.zeros(11),
        'z' : np.linspace(1000, 0, 11),
        'method' : method
    }

    stimParams = {
        'pptype' : 'SinSyn',
        'delay' : -100.,
        'dur' : 1000.,
        'pkamp' : 1.,
        'freq' : 100.,
        'phase' : -np.pi/2,
        'bias' : 0.,
        'record_current' : True
    }



    stick = LFPy.Cell(**stickParams)
    stick.set_pos(z=-stick.zstart[0])
    
    #dummy variables for mapping
    stick.imem = np.eye(stick.totnsegs)
    stick.tvec = np.arange(stick.totnsegs)*stick.dt

    electrode = LFPy.RecExtElectrode(stick, **electrodeParams)
    electrode.calc_lfp()
    #not needed anymore:
    del stick.imem, stick.tvec

    synapse = LFPy.StimIntElectrode(stick, stick.get_closest_idx(0, 0, 1000),
                           **stimParams)
    stick.simulate(dotprodcoeffs=electrode.LFP,
                   rec_imem=True, rec_vmem=True)

    return stick.dotprodresults[0]


def analytical_LFP(time=np.linspace(0, 100, 1001),
                   stickLength=1000.,
                   stickDiam=2.,
                   Rm=30000.,
                   Cm=1.,
                   Ri=150.,
                   stimFrequency=100.,
                   stimAmplitude=1.,
                   # stimPos=1.,
                   sigma=0.3,
                   electrodeR=100.,
                   electrodeZ=0.,
                   ):
    """
    Will calculate the analytical LFP from a dendrite stick aligned with z-axis.
    The synaptic current is always assumed to be at the end of the stick, i.e.
    Zin = stickLength.

    Parameters
    ----------
    time : ndarray
        The LFP is calculated for values in this np.array (ms)
    stickLength : float
        length of stick (mum)
    stickDiam : float
        diameter of stick (mum)
    Rm : float
        Membrane resistivity (Ohm * cm2)
    Cm : float
        Membrane capacitance (muF/cm2)
    Ri : float
        Intracellular resistivity (Ohm*cm)
    stimFrequency : float
        Frequency of cosine synapse current (Hz)
    stimAmplitude : float
        Amplitude of cosine synapse current (nA)
    # stimPos : float in [0, 1]
    #     Relative stimulus current position from start (0) to end (1) of stick
    sigma : float
        Extracellular conductivity (muS/mum)
    electrodeR : float
        Radial distance from stick (mum)
    electrodeZ : float
        Longitudal distance along stick(mum)
    """
    Gm = 1. / Rm            # specific membrane conductivity (S/cm2)
    gm = 1E2 * np.pi * stickDiam / Rm     # absolute membrane conductance (muS / mum)
    ri = 1E-2 * 4. * Ri / (np.pi * stickDiam**2) # intracellular resistance  (Mohm/mum)

    Lambda = 1E2 / np.sqrt(gm * ri) # Electrotonic length constant of stick (mum)
    Ginf = 10 / (ri * Lambda)   # infinite stick input cond (10*muS)?

    tau_m = Rm * Cm / 1000        # membrane time constant (ms)
    Omega = 2 * np.pi * stimFrequency * tau_m / 1000 #impedance
    Zel = electrodeZ / Lambda    # z-position of extracellular point, in units of Lambda
    L = stickLength / Lambda      # Length of stick in units of Lambda
    Rel = electrodeR / Lambda    # extracellular, location along x-axis, or radius, in units of Lambda
    q = np.sqrt(1 + 1j*Omega)	    # Note: j is sqrt(-1)
    Yin = q * Ginf * np.tanh(q * L)	    # Admittance
    Zin = stickLength / Lambda  # unitless location of input current
    # Zin = stickLength / Lambda * stimPos  # unitless location of input current

    PhiExImem = np.empty(time.size)
    PhiExInput = np.empty(time.size)

    def i_mem(z): #z is location at stick
        return gm * q**2 * np.cosh(q * z) / np.cosh(q * L) * stimAmplitude / Yin

    def f_to_integrate(z):
        return 1E-3 / (4 * np.pi * sigma) * i_mem(z) \
            / np.sqrt(Rel**2 + (z - Zel)**2)

    #calculate contrib from membrane currents
    Vex_imem = -complex_quadrature(f_to_integrate, 0, L, epsabs=1E-20)

    #adding contrib from input current to Vex
    Vex_input = stimAmplitude / (4 * np.pi * sigma * Lambda * np.sqrt(Rel**2 + (Zin-Zel)**2))

    PhiExImemComplex = Vex_imem * np.exp(1j * 2 * np.pi * stimFrequency *
                                              time / 1000)
    PhiExInputComplex = Vex_input * np.exp(1j * 2 * np.pi * stimFrequency *
                                             time / 1000)

    #Using only real component
    PhiExImem = PhiExImemComplex.real
    PhiExInput = PhiExInputComplex.real

    PhiEx = PhiExImem + PhiExInput
    return PhiEx

def complex_quadrature(func, a, b, **kwargs):
    """
    Will return the complex integral value.
    """
    def real_func(x):
        return real(func(x))
    def imag_func(x):
        return imag(func(x))
    real_integral = quad(real_func, a, b, **kwargs)
    imag_integral = quad(imag_func, a, b, **kwargs)
    return real_integral[0] + 1j*imag_integral[0]


