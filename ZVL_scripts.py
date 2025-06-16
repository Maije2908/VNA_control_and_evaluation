# -*- coding: utf-8 -*-
"""
author: Maier Christoph
date: 12.06.2025

This module is a selection of functions for the control of the ZVL VNA, and the 
manipulation of the generate measurement data.
"""

# import needed packages
import numpy as np
import matplotlib.pyplot as plt

# definition of constants
eps = np.finfo(np.float64).eps # define epsilon (a very small number)

# set default values of the variables
ShowCMD = False # Flag if output in the command line should be shown
ShowdB = False # Flag if results should be given in dB


"""
    A class to represent mixed-mode S-parameters (scattering parameters) for 
    a network over a range of frequencies. Mixed-mode parameters are a special
    kind of S-parameters, calculating the response to differential-mode (DM) 
    and common-mode (CM) signals. 

    Attributes:
        frequency (list): A list of the frequency points.
        value (list): 
        value_AP (list): 

    Methods:
        None
"""
class ZVL_settings:
    def __init__(self, dev_device, dev_version, dev_date, dev_mode,
                 dev_center_freq, dev_center_unit):
        
        """
        Initializes the MixedModeParameter class by combining the real and
        imaginary parts of the S-parameters into lists of complex numbers for
        each parameter.
    
        Parameters:
            frequency (list): A list of frequency points.
            sdd11_re, sdd11_im, ..., scc22_im (list): Real and imaginary parts
                                                    of the S-parameters.
    
        Each S-parameter is represented as a list of complex numbers
        corresponding to each frequency point.
        """
        self.device = dev_device
        self.version = dev_version
        self.date = dev_date
        self.mode = dev_mode



'''
    This function sets the global ShowCMD flag. The flag controls, if results
    will be shown in the command line. 
    
    Input Parameters:
        None
    
    Output parameters:
        None
'''
def set_showCMD():
    global ShowCMD
    ShowCMD = True



'''
    This function resets sets the global ShowCMD flag. The flag controls, if
    results will be shown in the command line. 
    
    Input Parameters:
        None
    
    Output parameters:
        None
'''
def reset_showCMD():
    global ShowCMD
    ShowCMD = False







'''
    This function reads the 

    This function calculates the normalized mean-square error (NMSE) of two
    S-parameter objects by comparing the transmission and the reflection
    coefficients separately.
    
    Input Parameters:
        SComp   network object of the S-parameter block which is
                compared to the reference one
        SRef    network object used as reference. The frequency grid
                and the number of ports of the two S-parameter objects
                must be the same
                If this variable is left empty, a comparison to a
                infinitesimally small, perfecly matched line
    
    Output parameters:
        NMSERef     Calculated NMSE for the reflection coefficients 
        NMSETrans   Calculated NMSE for the transmission coefficients
'''
def read_dat_file_spec(filename, autopeak):
    
    data = []
    header = []
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line and line[0].isdigit():
                row = [float(x) for x in line.split(';')]
                data.append(row)
            else:
                row = [str(x) for x in line.split(';')]
                header.append(row)
                
        print(header)
        
        # Assuming the header is always the same and will stay the same forever
        dev_type = header[0][1]
        dev_version = header[1][1]
        dev_date = header[2][1]
        dev_mode = header[3][1]
        dev_center_freq = header[4][1]
        dev_center_unit= header[4][2] 
        dev_offset = header[5][1]
        dev_offset_unit = header[5][2]
        dev_span = header[6][1]
        dev_span_unit = header[6][2]
        dev_xAx_type = header[7][1]
        dev_xAx_start = header[8][1]
        dev_xAx_start_unit = header[8][2]
        dev_xAx_stop = header[9][1]
        dev_xAx_stop_unit = header[9][2]
        dev_reflvl = header[10][1]
        dev_reflvl_unit = header[10][2]
        dev_offsetlvl = header[11][1]
        dev_offsetlvl_unit = header[11][2]
        dev_refpos = header[12][1]
        dev_refpos_unit = header[12][2]
        dev_yAx_type = header[13][1]
        dev_rangelvl = header[14][1]
        dev_rangelvl_unit = header[14][2]
        dev_rfatt = header[15][1]
        dev_rfatt_unit = header[15][2]
        dev_RBW = header[16][1]
        dev_RBW_unit = header[16][2]
        dev_VBW = header[17][1]
        dev_VBW_unit = header[17][2]
        dev_SWT = header[18][1]
        dev_SWT_unit = header[18][2]
        dev_trace_mode = header[19][1]
        dev_detector = header[20][1]
        dev_sweep_cnt = header[21][1]
        
        
        dev_trace_1 = header[22][1]
        
        print(dev_trace_1)
        
        settings = ZVL_settings(dev_type, dev_version, dev_date, dev_mode, 
                                dev_center_freq, dev_center_unit)
                
        return settings   
    
    
    
            
# if __name__ =='__main__':
#     # define files to evaluate
#     filepath = 'Spectrum_Analyzer/'
    
#     filename_1MHz = ['Noise_9kHz-1MHz.DAT',
#                      'Vin_150V_no_load_9kHz-1MHz.DAT',
#                      'Vin_150V_15mA_9kHz-1MHz.DAT',
#                      'Vin_150V_50mA_9kHz-1MHz.DAT',
#                      'Vin_150V_100mA_9kHz-1MHz.DAT',
#                      'Vin_150V_200mA_9kHz-1MHz.DAT']

#     filename_10MHz = ['Noise_9kHz-10MHz.DAT',
#                       'Vin_150V_no_load_9kHz-10MHz.DAT',
#                       'Vin_150V_15mA_9kHz-10MHz.DAT',
#                       'Vin_150V_50mA_9kHz-10MHz.DAT',
#                       'Vin_150V_100mA_9kHz-10MHz.DAT',
#                       'Vin_150V_200mA_9kHz-10MHz.DAT']
    
#     value_1MHz = []
#     value_10MHz = []
     
#     for file in filename_1MHz:
#         value_1MHz.append(read_input(filepath + file))
        
#     for file in filename_10MHz:
#         value_10MHz.append(read_input(filepath + file))

        
#     # creating plot
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
    
