# -*- coding: utf-8 -*-
"""
author: Maier Christoph
date: 22.09.2025

This script is a test function to show and test the various functions defined
in "VNA_scripts".
"""

import skrf as rf
import numpy as np
import matplotlib.pyplot as plt

import VNA_scripts as VNA

if __name__ =='__main__':
    
    ###########################################################################
    ############################### Definitions ###############################
    ###########################################################################
    
    # general definitions
    autopeak = 1
    save_flag = 0
    
    
    # ZVL test definitions
    filepath_ZVL = 'Testdata/ZVL/Spectrum_Analyzer/'
    filenames_ZVL = ['TESTDATA_ZVL.dat']
    
    number_of_files_ZVL = len(filenames_ZVL)
    device_setting_ZVL = []
    trace_setting_ZVL = []
    frequency_ZVL = []
    yval1_ZVL = []
    yval2_ZVL = []    
    
    
    # ZNL test definitions
    filepath_ZNL = 'Testdata/ZNL/Spectrum_Analyzer/'
    filenames_ZNL = ['TESTDATA_ZNL.dat']
    
    number_of_files_ZNL = len(filenames_ZVL)
    device_setting_ZNL = []
    trace_setting_ZNL = []
    frequency_ZNL = []
    yval1_ZNL = []
    yval2_ZNL = []    
    
    ###########################################################################
    ################################## Tests ##################################
    ###########################################################################
    
    ### ZVL test ###
    for name in filenames_ZVL:
        
        temp_device_setting, temp_trace_setting, temp_frequency, temp_yval1, temp_yval2 = VNA.read_dat_1trace_spec(filepath_ZVL + name, autopeak)
        device_setting_ZVL.append(temp_device_setting)
        trace_setting_ZVL.append(temp_trace_setting)
        frequency_ZVL.append(temp_frequency)
        yval1_ZVL.append(temp_yval1)
        yval2_ZVL.append(temp_yval2)
        
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
            
           
            
        ### ZNL test ###
        for name in filenames_ZNL:
            
            temp_device_setting, temp_trace_setting, temp_frequency, temp_yval1, temp_yval2 = VNA.read_dat_1trace_spec(filepath_ZVL + name, autopeak)
            device_setting_ZVL.append(temp_device_setting)
            trace_setting_ZVL.append(temp_trace_setting)
            frequency_ZVL.append(temp_frequency)
            yval1_ZVL.append(temp_yval1)
            yval2_ZVL.append(temp_yval2)
            
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
        