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
    save_flag = 1
    
    
    # ZVL test definitions
    filepath_ZVL = 'Testdata/ZVL/Spectrum_Analyzer/'
    filenames_ZVL = ['TESTDATA_ZVL-1.dat', 'TESTDATA_ZVL-2.dat']
    number_of_files_ZVL = len(filenames_ZVL)
    file_range_ZVL = range(number_of_files_ZVL)
    
    
    # ZNL test definitions
    filepath_ZNL = 'Testdata/ZNL/Spectrum_Analyzer/'
    filenames_ZNL = ['TESTDATA_ZNL-1.dat']
    number_of_files_ZNL = len(filenames_ZNL)
    file_range_ZNL = range(number_of_files_ZNL)
    
    
    
    ###########################################################################
    ################################## Tests ##################################
    ###########################################################################
    
    ########## ZVL single file test ##########        
    # extract the data from the file and store it in various variables
    device_setting_ZVL, trace_setting_ZVL, frequency_ZVL, yval1_ZVL, temp_yval2_ZVL = VNA.ZVL_spectrum_read_1trace(
        filepath_ZVL, filenames_ZVL[0], autopeak)
    
    # Create plot
    fig = plt.figure()

    plt.semilogx(frequency_ZVL, yval1_ZVL)
        
    plt.title(filenames_ZVL[0])
    plt.xlabel('Frequency in ' + trace_setting_ZVL.x_unit)
    plt.ylabel('Power in ' + trace_setting_ZVL.y_unit)
    plt.xlim(min(frequency_ZVL), max(frequency_ZVL))
    #plt.ylim(-10, 50)
    plt.grid(which='both', axis='both')
       
    plt.tight_layout()
    plt.show
    
    if save_flag == 1:
        plt.savefig(filenames_ZVL[0][:-4] + '_log.png')
           
    
    ########## ZVL multi file test ##########    
    device_setting_ZVL, trace_setting_ZVL, frequency_ZVL, yval1_ZVL, temp_yval2_ZVL = VNA.ZVL_spectrum_read_multrace(
        filepath_ZVL, filenames_ZVL, autopeak)
 
    # create plot
    for cnt in file_range_ZVL:
        print(cnt)
            
            
            
            
            
            
            
            
              
            
    
    ########## ZNL single file test ##########
    device_setting_ZNL, trace_setting_ZNL, frequency_ZNL, yval1_ZNL, yval2_ZNL = VNA.ZNL_spectrum_read_1trace(
        filepath_ZNL, filenames_ZNL[0], autopeak)
    
    # create individual plots
    fig = plt.figure()

    plt.semilogx(frequency_ZNL, yval1_ZNL)
        
    plt.title(filenames_ZNL[0])
    plt.xlabel('Frequency in Hz')
    plt.ylabel('Power in ')
    plt.xlim(min(frequency_ZNL), max(frequency_ZNL))
    #plt.ylim(-10, 50)
    plt.grid(which='both', axis='both')
       
    plt.tight_layout()
    plt.show
    
    if save_flag == 1:
        plt.savefig(filenames_ZNL[0][:-4] + '_log.png')
            