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
    autopeak = 1
    
    [a,b,c,d,e] = ZVL.read_dat_1trace_spec(filename, autopeak)
    


    # creating plot
    #     fig = plt.figure()

    #     for cnt in range(len(value_1MHz)):
    #         #plt.semilogx(value_1MHz[cnt][:,0], value_1MHz[cnt][:,1])
    #         plt.semilogx(value_1MHz[cnt][:,0], value_1MHz[cnt][:,2])
            
    #     plt.title('Disturbances for 9kHz to 1MHz')
    #     plt.xlabel('Frequency in Hz')
    #     plt.ylabel('dBm')
    #     plt.legend(['noise','0mA','15mA','50mA','100mA','200mA'])
    #     plt.xlim(min(value_1MHz[0][:,0]), max(value_1MHz[0][:,0]))
    #     plt.grid(which='both', axis='both')
           
    #     plt.tight_layout()
    #     plt.show
        
    #     # creating plot
    #     fig = plt.figure()

    #     for cnt in range(len(value_10MHz)):
    #         #plt.semilogx(value_10MHz[cnt][:,0], value_10MHz[cnt][:,1])
    #         plt.semilogx(value_10MHz[cnt][:,0], value_10MHz[cnt][:,2])
            
    #     plt.title('Disturbances for 9kHz to 10MHz')
    #     plt.xlabel('Frequency in Hz')
    #     plt.legend(['noise','0mA','15mA','50mA','100mA','200mA'])
    #     plt.xlim(min(value_10MHz[0][:,0]), max(value_10MHz[0][:,0]))
    #     plt.grid(which='both', axis='both')
           
    #     plt.tight_layout()
    #     plt.show
    
    