# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 10:56:46 2024

@author: christoph_m
"""

import skrf as rf
import numpy as np
import matplotlib.pyplot as plt

import VNA_scripts as VNA

if __name__ =='__main__':
        
    filepath_ZVL = 'Testdata/ZVL/Spectrum_Analyzer/'
    filenames_ZVL = ['TESTDATA.dat'] # could of course be more than one
    autopeak = 1
    save_flag = 0
    
    number_of_files = len(filenames_ZVL)
    device_setting = []
    trace_setting = []
    frequency = []
    yval1 = []
    yval2 = []
        
    for name in filenames_ZVL:
        
        temp_device_setting, temp_trace_setting, temp_frequency, temp_yval1, temp_yval2 = VNA.read_dat_1trace_spec(filepath_ZVL + name, autopeak)
        device_setting.append(temp_device_setting)
        trace_setting.append(temp_trace_setting)
        frequency.append(temp_frequency)
        yval1.append(temp_yval1)
        yval2.append(temp_yval2)
        
        # create individual plots
        fig = plt.figure()
    
        plt.semilogx(temp_frequency, temp_yval1)
            
        plt.title(name)
        plt.xlabel('Frequency in Hz')
        plt.ylabel('dBuV')
        plt.xlim(min(temp_frequency), max(temp_frequency))
        #plt.ylim(-10, 50)
        plt.grid(which='both', axis='both')
           
        plt.tight_layout()
        plt.show
        
        if save_flag == 1:
            plt.savefig(name[:-4] + '_log.png')
        