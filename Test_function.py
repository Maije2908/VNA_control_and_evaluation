# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 10:56:46 2024

@author: christoph_m
"""

import skrf as rf
import numpy as np
import matplotlib.pyplot as plt

import ZVL_scripts as ZVL

if __name__ =='__main__':
        
    filename = 'Testdata/Spectrum_Analyzer/TESTDATA.dat'
    autopeak = 0
    
    a = ZVL.read_dat_file_spec(filename, autopeak)

    