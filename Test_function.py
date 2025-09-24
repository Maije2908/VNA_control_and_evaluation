# -*- coding: utf-8 -*-
"""
author: Maier Christoph
date: 22.09.2025

This script is a test function to show and test the various functions defined
in "VNA_scripts".
"""

###############################################################################
################################### Imports ###################################
###############################################################################

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
    
    
    # ZNL test definitions
    filepath_ZNL = 'Testdata/ZNL/Spectrum_Analyzer/'
    filenames_ZNL = ['TESTDATA_ZNL.dat']
    number_of_files_ZNL = len(filenames_ZNL)
    
    
    
    ###########################################################################
    ################################## Tests ##################################
    ###########################################################################
    
    ### ZVL test ###
    for name in filenames_ZVL:
        
        # extract the data from the file and store it in various variables
        device_setting_ZVL, trace_setting_ZVL, frequency_ZVL, yval1_ZVL, temp_yval2_ZVL = VNA.ZVL_spectrum_read_1trace(
            filepath_ZVL + name, autopeak)
        
        # Create plot
        fig = plt.figure()
    
        plt.semilogx(frequency_ZVL, yval1_ZVL)
            
        plt.title(name)
        plt.xlabel('Frequency in ' + trace_setting_ZVL.x_unit)
        plt.ylabel('Power in ' + trace_setting_ZVL.y_unit)
        plt.xlim(min(frequency_ZVL), max(frequency_ZVL))
        #plt.ylim(-10, 50)
        plt.grid(which='both', axis='both')
           
        plt.tight_layout()
        plt.show
        
        if save_flag == 1:
            plt.savefig(name[:-4] + '_log.png')
              
            
    ### ZNL test ###
    for name in filenames_ZNL:
        
        device_setting_ZNL, trace_setting_ZNL, frequency_ZNL, yval1_ZNL, yval2_ZNL = VNA.ZNL_spectrum_read_1trace(
            filepath_ZNL + name, autopeak)
        
        # create individual plots
        fig = plt.figure()
    
        plt.semilogx(frequency_ZNL, yval1_ZNL)
            
        plt.title(name)
        plt.xlabel('Frequency in Hz')
        plt.ylabel('Power in ')
        plt.xlim(min(frequency_ZNL), max(frequency_ZNL))
        #plt.ylim(-10, 50)
        plt.grid(which='both', axis='both')
           
        plt.tight_layout()
        plt.show
        
        if save_flag == 1:
            plt.savefig(name[:-4] + '_log.png')
            