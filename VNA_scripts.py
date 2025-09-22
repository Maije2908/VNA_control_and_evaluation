# -*- coding: utf-8 -*-
"""
author: Maier Christoph
date: 22.09.2025

This module is a selection of functions for the control of the different VNAs
we are using, and also for the manipulation of the generated measurement data.
"""

###############################################################################
################################### Imports ###################################
###############################################################################

import numpy as np
import matplotlib.pyplot as plt


###############################################################################
################################## Constants ##################################
###############################################################################

eps = np.finfo(np.float64).eps # define epsilon (a very small number)


###############################################################################
################################## Defaults ###################################
###############################################################################

ShowCMD = False # Flag if output in the command line should be shown
ShowdB = False # Flag if results should be given in dB


###############################################################################
############################### Global functions ##############################
###############################################################################

'''
    show command line output
    
    This function sets the global ShowCMD flag. The flag controls, if results
    will be shown in the command line. 
'''
#%%
'''
    Input Parameters:
        None
    
    Output parameters:
        None
'''
def set_showCMD():
    global ShowCMD
    ShowCMD = True
#%%


'''
    do not show command line output
    
    This function resets sets the global ShowCMD flag. The flag controls, if
    results will be shown in the command line. 
'''
#%%
'''
    Input Parameters:
        None
    
    Output parameters:
        None
'''
def reset_showCMD():
    global ShowCMD
    ShowCMD = False
#%%


###############################################################################
############################ Rohde und Schwarz ZVL ############################
###############################################################################

'''
    ZVL spectrum analyzer settings
    
    A class to allow easy access to the measurement settings of the ZVL in
    spectrum analyzer mode. The description of the attributes is taken from
    the ZVL-K1 manual (see: ASCII file export format).
'''
#%%%
'''
    Attributes:
        dev_type (string): Instrument model
        version (string): Firmware version
        date (string): Date of data set storage
        mode (string): Instrument mode
        center_freq (float): Center frequency (value)
        center_unit (string): Center frequency (unit)
        offset (float): Frequency offset (value)
        offset_unit (string): Frequency offset (unit)
        span (float): Frequency range (value)
        span_unit (string): Frequency range (unit)
        xAx_type (string): Scaling of x-axis (linear (LIN) or logarithmic (LOG))
        xAx_start (float): Start frequency of the display range (value)
        xAx_start_unit (string): Start frequency of the display range (unit)
        xAx_stop (float): Stop frequency of the display range (value)
        xAx_stop (string): Stop frequency of the display range (unit)
        reflvl (float): Reference level (value)
        reflvl_unit (string): Reference level (unit)
        offsetlvl (float): Level Offset (value)
        offsetlvl_unit (string): Level Offset (unit)
        refpos (float): Position of reference level reffered to diagram limits (value)
        refpos_unit (string): Position of reference level reffered to diagram limits (unit)
        yAx_type (string): Scaling of y-axis (linear (LIN) or logarithmic (LOG))
        rangelvl (float): Display range in y direction (value)
        rangelvl_unit (string): Display range in y direction (unit)        
        rfatt (float): Input attenuation (value)
        rfatt_unit (string): Input attenuation (unit)
        RBW (float): Resolution bandwidth (value)
        RBW_unit (string): Resolution bandwidth (unit)
        VBW (float): Video bandwidth (value)
        VBW_unit (string): Video bandwidth (unit)
        SWT (float): Sweep time (value)
        SWT_unit (string): Sweep time (unit)
        trace_mode (string): Display mode of trace
        detector (string): Detector setting
        sweep_cnt (int): Number of sweeps set

    Methods:
        None
'''
class ZVL_spectrum_setting:
    def __init__(self, dev_type, version, date, mode, center_freq, center_unit,
                 offset, offset_unit, span, span_unit, xAx_type, xAx_start,
                 xAx_start_unit, xAx_stop, xAx_stop_unit, reflvl, reflvl_unit,
                 offsetlvl, offsetlvl_unit, refpos, refpos_unit, yAx_type,
                 rangelvl, rangelvl_unit, rfatt, rfatt_unit, RBW, RBW_unit,
                 VBW, VBW_unit, SWT, SWT_unit, trace_mode, detector, sweep_cnt):
        
        self.dev_type = dev_type
        self.version = version
        self.date = date
        self.mode = mode
        self.center_freq = float(center_freq)
        self.center_unit = center_unit
        self.offset = float(offset)
        self.offset_unit = offset_unit
        self.span = float(span)
        self.span_unit = span_unit
        self.xAx_type = xAx_type
        self.xAx_start = float(xAx_start)
        self.xAx_start_unit = xAx_start_unit
        self.xAx_stop = float(xAx_stop)
        self.xAx_stop_unit = xAx_stop_unit
        self.reflvl = float(reflvl)
        self.reflvl_unit = reflvl_unit
        self.offsetlvl = float(offsetlvl)
        self.offsetlvl_unit = offsetlvl_unit
        self.refpos = float(refpos)
        self.refpos_unit = refpos_unit
        self.yAx_type = yAx_type
        self.rangelvl = float(rangelvl)
        self.rangelvl_unit = rangelvl_unit
        self.rfatt = float(rfatt)
        self.rfatt_unit = rfatt_unit
        self.RBW = float(RBW)
        self.RBW_unit = RBW_unit
        self.VBW = float(VBW)
        self.VBW_unit = VBW_unit
        self.SWT = float(SWT)
        self.SWT_unit = SWT_unit
        self.trace_mode = trace_mode
        self.detector = detector
        self.sweep_cnt = int(sweep_cnt)
#%%


'''
    ZVL spectrum analyzer trace settings
    
    A class to allow easy access to the trace settings of the Rohde und Schwarz
    ZVL for a one trace measurements.
'''
#%%
'''
    Attributes:
        x_unit (string): Unit of the x values
        y_unit (string): Unit of the y values
        preamp (string): Preamplifier present
        transducer (string): Transducer present
        meas_number (int): Number of measurement points

    Methods:
        None
'''        
class ZVL_spectrum_one_trace:
    def __init__(self, x_unit, y_unit, preamp, transducer, meas_number):
        
        self.x_unit = x_unit
        self.y_unit = y_unit
        self.preamp = preamp
        self.transducer = transducer
        self.meas_number = int(meas_number)       
#%%


###############################################################################
############################ Rohde und Schwarz ZNL ############################
###############################################################################

'''
    ZNL spectrum analyzer settings
    
    A class to allow easy access to the measurement settings of the ZNL in
    spectrum analyzer mode. The description of the attributes is taken from
    the ZNL analog demodulation mode manual (see: 11.7.5 Reference: ASCII file
    export format).
'''
#%%%
'''
    Attributes:
        dev_type (string): Instrument model
        version (string): Firmware version
        date (string): Date of data set storage
        mode (string): Instrument mode
        preamp (string): Preamplifier status
        transducer (string): Transducer status
        center_freq (float): Center frequency (value)
        center_unit (string): Center frequency (unit)
        offset (float): Frequency offset (value)
        offset_unit (string): Frequency offset (unit)
        xAx_start (float): Start frequency of the display range (value)
        xAx_start_unit (string): Start frequency of the display range (unit)
        xAx_stop (float): Stop frequency of the display range (value)
        xAx_stop (string): Stop frequency of the display range (unit)
        span (float): Frequency range (value)
        span_unit (string): Frequency range (unit)
        reflvl (float): Reference level (value)
        reflvl_unit (string): Reference level (unit)
        offsetlvl (float): Level Offset (value)
        offsetlvl_unit (string): Level Offset (unit)
        rfatt (float): Input attenuation (value)
        rfatt_unit (string): Input attenuation (unit)
        elatt (float): Electrical attenuation (value)
        elatt_unit (string): Electrical attenuation (unit)
        RBW (float): Resolution bandwidth (value)
        RBW_unit (string): Resolution bandwidth (unit)
        VBW (float): Video bandwidth (value)
        VBW_unit (string): Video bandwidth (unit)
        SWT (float): Sweep time (value)
        SWT_unit (string): Sweep time (unit)
        sweep_cnt (int): Number of sweeps set
        refpos (float): Position of reference level reffered to diagram limits (value)
        refpos_unit (string): Position of reference level reffered to diagram limits (unit)
        rangelvl (float): Display range in y direction (value)
        rangelvl_unit (string): Display range in y direction (unit)   
        xAx_type (string): Scaling of x-axis (linear (LIN) or logarithmic (LOG))
        yAx_type (string): Scaling of y-axis (linear (LIN) or logarithmic (LOG))  
        xAx_unit (string): Unit of x values
        yAx_unit (string): Unit of y values

    Methods:
        None
'''
class ZNL_spectrum_setting:
    def __init__(self, dev_type, version, date, mode, preamp, transducer,
                 center_freq, center_unit, offset, offset_unit,  xAx_start, 
                 xAx_start_unit, xAx_stop, xAx_stop_unit, span, span_unit,
                 reflvl, reflvl_unit, offsetlvl, offsetlvl_unit, rfatt,
                 rfatt_unit, elatt, elatt_unit, RBW, RBW_unit, VBW, VBW_unit,
                 SWT, SWT_unit, sweep_cnt, refpos, refpos_unit, rangelvl,
                 rangelvl_unit, xAx_type, yAx_type, xAx_unit, yAx_unit):
        
        self.dev_type = dev_type
        self.version = version
        self.date = date
        self.mode = mode
        self.preamp = preamp
        self.transducer = transducer
        self.center_freq = float(center_freq)
        self.center_unit = center_unit
        self.offset = float(offset)
        self.offset_unit = offset_unit
        self.xAx_start = float(xAx_start)
        self.xAx_start_unit = xAx_start_unit
        self.xAx_stop = float(xAx_stop)
        self.xAx_stop_unit = xAx_stop_unit
        self.span = float(span)
        self.span_unit = span_unit
        self.reflvl = float(reflvl)
        self.reflvl_unit = reflvl_unit
        self.offsetlvl = float(offsetlvl)
        self.offsetlvl_unit = offsetlvl_unit
        self.rfatt = float(rfatt)
        self.rfatt_unit = rfatt_unit
        self.elatt = elatt
        self.elatt_unit = elatt_unit
        self.RBW = float(RBW)
        self.RBW_unit = RBW_unit
        self.VBW = float(VBW)
        self.VBW_unit = VBW_unit
        self.SWT = float(SWT)
        self.SWT_unit = SWT_unit
        self.sweep_cnt = int(sweep_cnt)
        self.refpos = float(refpos)
        self.refpos_unit = refpos_unit
        self.rangelvl = float(rangelvl)
        self.rangelvl_unit = rangelvl_unit
        self.xAx_type = xAx_type
        self.yAx_type = yAx_type
        self.xAx_unit = xAx_unit
        self.yax_unit = yAx_unit
#%%


'''
    ZNL spectrum analyzer trace settings
    
    A class to allow easy access to the trace settings of the Rohe und Schwarz
    ZNL for a one trace measurements.
'''
#%%
'''
    Attributes:
        trace (string): Selected trace
        trace_mode (string): Display mode of trace
        detector (string): selected detector
        meas_number (int): Number of measurement points

    Methods:
        None
'''        
class ZNL_spectrum_one_trace:
    def __init__(self, trace, trace_mode, detector, meas_number):
        
        self.trace = trace
        self.trace_mode = trace_mode
        self.detector = detector
        self.meas_number = int(meas_number)       
#%%

























    

       
 





'''
    This function reads a .dat file for a spectrum analyzer measurement with 
    one trace. It uses the ZVL device and ZVL trace class to give the 
    settings of the instrument and the trace. 
    
    Input Parameters:
        filename    string which stores the filename (including path) of the
                    .dat file
        autopeak    flag which indicates if the autopeak setting was set.
                    Autopeak adds another output (yval2), which gives the
                    smallest of the two measured values (see ZVL manual)
    
    Output parameters:
        device_setting    The settings of the instrument (using ZVL device class)
        trace_setting     The settings of the trace (using ZVL trace class)
        frequency         vector (list) containing the frequency points
        yval1             vector (list) containing the measurement values
        yval2             vector (list) contining the smallest of the two values
                          (only if AUTOPEAK is enabled, otherwise emtpy)
'''
def read_dat_1trace_spec(filename, autopeak):
    
    data = []
    header = []
    frequency = []
    yval1 = []
    yval2 = []
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line and line[0].isdigit():
                row = [float(x) for x in line.split(';')]
                data.append(row)
            else:
                row = [str(x) for x in line.split(';')]
                header.append(row)
        
    # Assuming the header is always the same and will stay the same forever
    # Device settings
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
    
    # Settings of the trace
    x_unit = header[23][1]
    y_unit = header[24][1]
    preamp = header[25][1]
    transducer = header[26][1]
    meas_number = header[27][1]
    
    device_setting = ZVL_spectrum_setting(dev_type, dev_version, dev_date, dev_mode, 
                            dev_center_freq, dev_center_unit, dev_offset,
                            dev_offset_unit, dev_span, dev_span_unit,
                            dev_xAx_type, dev_xAx_start, dev_xAx_start_unit,
                            dev_xAx_stop, dev_xAx_stop_unit, dev_reflvl,
                            dev_reflvl_unit, dev_offsetlvl, dev_offsetlvl_unit,
                            dev_refpos, dev_refpos_unit, dev_yAx_type,
                            dev_rangelvl, dev_rangelvl_unit, dev_rfatt,
                            dev_rfatt_unit, dev_RBW, dev_RBW_unit,
                            dev_VBW, dev_VBW_unit, dev_SWT, dev_SWT_unit,
                            dev_trace_mode, dev_detector, dev_sweep_cnt)

    trace_setting = ZVL_spectrum_one_trace(x_unit, y_unit, preamp,
                                      transducer, meas_number)
    
    for cnt in range(len(data)):
        frequency.append(data[cnt][0])
        yval1.append(data[cnt][1])
        
        if autopeak == 1:
            yval2.append(data[cnt][2])
                            
    return [device_setting, trace_setting, frequency, yval1, yval2]



'''
    This function takes the filename of multiple .dat file from a 1 trace
    spectrum analyzer measurement, extracts the data and stores them in a
    matrix. It uses the function 'read_dat_1trace_spec' for the extraction of
    the data.
    
    Input Parameters:
        filename        string which stores the filename of the .csv file
        filepath        filepath for the stored data
        autopek         flag which indicates if the AUTOPEAK option was used. 
                        
    Output parameters:
        device_setting    The settings of the instrument (using ZVL device class)
        trace_setting     The settings of the trace (using ZVL trace class)
        frequency         matrix (list) containing the frequency points
        yval1             matrix (list) containing the measurement values
        yval2             matrix (list) contining the smallest of the two values
                          (only if AUTOPEAK is enabled, otherwise emtpy)
'''
def mul_measurements_1ch(filename, filepath, autopeak):
    
    device_setting = []
    trace_setting = []
    frequency = []
    yval1 = []
    yval2 = []  
    
    for file in filename:
        [device_temp, trace_temp, frequency_temp, yval1_temp, yval2_temp] = read_dat_1trace_spec(filepath + file, autopeak)
        device_setting.append(device_temp)
        trace_setting.append(trace_temp)
        frequency.append(frequency_temp)
        yval1.append(yval1_temp)
        yval2.append(yval2_temp)

    return [device_setting, trace_setting, frequency, yval1, yval2]



'''
    This function plots multiple traces in one plot.
    
    Input Parameters:
        frequency  frequency matrix, consisting of the time data vectors
        yval       voltage matrix, consisting of the measured voltage vecotrs
        title      string consisting the title of the plot
        xlabel     string including the label of the x-axis
        ylabel     string including the label of the y-axis
        legend     vector of strings consisting of the legend
        xfit       optional argument for the left and right xlim
        
    Output Parameters:
        NONE
'''
def multiplot(frequency, yval, title, xlabel, ylabel, legend, xfit = None):
        
    plt.figure()

    for cnt in range(len(frequency)):
        plt.semilogx(frequency[cnt], yval[cnt])
        
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(legend)
    if xfit != None:
        plt.xlim(xfit)
    plt.grid(which='both', axis='both')
       
    plt.tight_layout()
    plt.show







