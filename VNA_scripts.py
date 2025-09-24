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
    
    Input Parameters:
        None
    
    Output parameters:
        None
'''
def set_showCMD():
    global ShowCMD
    ShowCMD = True



'''
    do not show command line output
    
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



###############################################################################
############################ Rohde und Schwarz ZVL ############################
###############################################################################

'''
    ZVL spectrum analyzer: device settings
    
    A class to allow easy access to the measurement settings of the ZVL in
    spectrum analyzer mode. The description of the attributes is taken from
    the ZVL-K1 manual (see: ASCII file export format).
    
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
        xAx_stop_unit (string): Stop frequency of the display range (unit)
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
class ZVL_spectrum_setting_device:
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


'''
    ZVL spectrum analyzer: trace settings
    
    A class to allow easy access to the trace settings of the Rohde und Schwarz
    ZVL for a one trace measurements.

    Attributes:
        x_unit (string): Unit of the x values
        y_unit (string): Unit of the y values
        preamp (string): Preamplifier present
        transducer (string): Transducer present
        meas_number (int): Number of measurement points

    Methods:
        None
'''        
class ZVL_spectrum_settings_one_trace:
    def __init__(self, x_unit, y_unit, preamp, transducer, meas_number):
        
        self.x_unit = x_unit
        self.y_unit = y_unit
        self.preamp = preamp
        self.transducer = transducer
        self.meas_number = int(meas_number)       


'''
    ZVL spectrum analyzer: read a one trace measurement (with/without AUTOPEAK)
    
    This function reads a .dat file for a spectrum analyzer measurement with 
    one trace. It uses the ZVL_spectrum_setting_device and  the
    ZVL_spectrum_setting_one_trace class to give the settings of the instrument
    and the settings of the trace.

    Input Parameters:
        filename (string): Filename (including path) of the .dat file
        autopeak (int): flag which indicates if the autopeak setting was set.
                        Autopeak adds another output (yval2), which gives the
                        smallest of the two measured values (see ZVL manual)
    
    Output parameters:
        device_setting (ZVL_spectrum_setting_device): Settings of the instrument
        trace_setting  (ZVL_spectrum_settings_one_trace): Settings of the trace
        frequency (list): Contains the frequency points
        yval1 (list): Contains the measured values
        yval2 (list): Contains the smallest of the two measured values
                      (only if AUTOPEAK is enabled, otherwise emtpy)
'''
def ZVL_spectrum_read_1trace(filepath, filename, autopeak):
    
    file_data = []
    file_header = []
    frequency = []
    yval1 = []
    yval2 = []
    
    # Basic idea is to test if the entry of the line is a ditig (aka a measured
    # value). If not, it has to be part of the header.
    with open(filepath + filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line and line[0].isdigit():
                row = [float(x) for x in line.split(';')]
                file_data.append(row)
            else:
                row = [str(x) for x in line.split(';')]
                file_header.append(row)
        
    # Assuming the header is always the same and will stay the same forever!
    # This should be the case, if the manual is right...
    # store device settings
    dev_type = file_header[0][1]
    dev_version = file_header[1][1]
    dev_date = file_header[2][1]
    dev_mode = file_header[3][1]
    dev_center_freq = file_header[4][1]
    dev_center_unit= file_header[4][2] 
    dev_offset = file_header[5][1]
    dev_offset_unit = file_header[5][2]
    dev_span = file_header[6][1]
    dev_span_unit = file_header[6][2]
    dev_xAx_type = file_header[7][1]
    dev_xAx_start = file_header[8][1]
    dev_xAx_start_unit = file_header[8][2]
    dev_xAx_stop = file_header[9][1]
    dev_xAx_stop_unit = file_header[9][2]
    dev_reflvl = file_header[10][1]
    dev_reflvl_unit = file_header[10][2]
    dev_offsetlvl = file_header[11][1]
    dev_offsetlvl_unit = file_header[11][2]
    dev_refpos = file_header[12][1]
    dev_refpos_unit = file_header[12][2]
    dev_yAx_type = file_header[13][1]
    dev_rangelvl = file_header[14][1]
    dev_rangelvl_unit = file_header[14][2]
    dev_rfatt = file_header[15][1]
    dev_rfatt_unit = file_header[15][2]
    dev_RBW = file_header[16][1]
    dev_RBW_unit = file_header[16][2]
    dev_VBW = file_header[17][1]
    dev_VBW_unit = file_header[17][2]
    dev_SWT = file_header[18][1]
    dev_SWT_unit = file_header[18][2]
    dev_trace_mode = file_header[19][1]
    dev_detector = file_header[20][1]
    dev_sweep_cnt = file_header[21][1]
    
    # store trace settings
    tr_x_unit = file_header[23][1]
    tr_y_unit = file_header[24][1]
    tr_preamp = file_header[25][1]
    tr_transducer = file_header[26][1]
    tr_meas_number = file_header[27][1]
    
    # There is a class for every device (and for all kinds of measurements).
    # Here, the assignment of the variables is done (Varies for every device).
    # To be honest, there are two classes: device settings and trace settings.
    device_setting = ZVL_spectrum_setting_device(
        dev_type, dev_version, dev_date, dev_mode, dev_center_freq,
        dev_center_unit, dev_offset, dev_offset_unit, dev_span, dev_span_unit,
        dev_xAx_type, dev_xAx_start, dev_xAx_start_unit, dev_xAx_stop,
        dev_xAx_stop_unit, dev_reflvl, dev_reflvl_unit, dev_offsetlvl,
        dev_offsetlvl_unit, dev_refpos, dev_refpos_unit, dev_yAx_type,
        dev_rangelvl, dev_rangelvl_unit, dev_rfatt, dev_rfatt_unit, dev_RBW,
        dev_RBW_unit, dev_VBW, dev_VBW_unit, dev_SWT, dev_SWT_unit,
        dev_trace_mode, dev_detector, dev_sweep_cnt)

    trace_setting = ZVL_spectrum_settings_one_trace(
        tr_x_unit, tr_y_unit, tr_preamp, tr_transducer, tr_meas_number)
    
    # Measured data is stored here in two (three if AUTOPEAK is set) separate lists.
    for cnt in range(len(file_data)):
        frequency.append(file_data[cnt][0])
        yval1.append(file_data[cnt][1])
        
        if autopeak == 1:
            yval2.append(file_data[cnt][2])
                         
    return [device_setting, trace_setting, frequency, yval1, yval2]


'''
    This function takes the filename of multiple .dat file from a 1 trace
    spectrum analyzer measurement, extracts the data and stores them in a
    matrix. It uses the function 'ZVL_spectrum_read_1trace' for the extraction
    of the data.
    
    Input Parameters:
        filepath (string): filepath for the stored data
        filenames (list, string): list of strings which containsthe filenames
        autopeak (int): flag which indicates if the AUTOPEAK option was used. 
                        
    Output parameters:
        device_setting (list, ZVL_spectrum_setting_device): Settings of the instrument
        trace_setting  (list, ZVL_spectrum_settings_one_trace): Settings of the trace
        frequency (list): Contains the frequency points
        yval1 (list): Contains the measured values
        yval2 (list): Contains the smallest of the two measured values
                      (only if AUTOPEAK is enabled, otherwise emtpy)
'''
def ZVL_spectrum_read_multrace(filepath, filenames, autopeak):
    
    device_setting = []
    trace_setting = []
    frequency = []
    yval1 = []
    yval2 = []  
    
    for file in filenames:
        [device_temp, trace_temp, frequency_temp, yval1_temp, yval2_temp] = ZVL_spectrum_read_1trace(filepath, file, autopeak)
        device_setting.append(device_temp)
        trace_setting.append(trace_temp)
        frequency.append(frequency_temp)
        yval1.append(yval1_temp)
        yval2.append(yval2_temp)

    return [device_setting, trace_setting, frequency, yval1, yval2]



###############################################################################
############################ Rohde und Schwarz ZNL ############################
###############################################################################

'''
    ZNL spectrum analyzer: device settings
    
    A class to allow easy access to the measurement settings of the ZNL in
    spectrum analyzer mode. The description of the attributes is taken from
    the ZNL analog demodulation mode manual (see: 11.7.5 Reference: ASCII file
    export format).

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
        xAx_stop_unit (string): Stop frequency of the display range (unit)
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

    Methods:
        None
'''
class ZNL_spectrum_setting_device:
    def __init__(self, dev_type, version, date, mode, preamp, transducer,
                 center_freq, center_unit, offset, offset_unit,  xAx_start, 
                 xAx_start_unit, xAx_stop, xAx_stop_unit, span, span_unit,
                 reflvl, reflvl_unit, offsetlvl, offsetlvl_unit, rfatt,
                 rfatt_unit, elatt, elatt_unit, RBW, RBW_unit, VBW, VBW_unit,
                 SWT, SWT_unit, sweep_cnt):
        
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
        self.elatt = float(elatt)
        self.elatt_unit = elatt_unit
        self.RBW = float(RBW)
        self.RBW_unit = RBW_unit
        self.VBW = float(VBW)
        self.VBW_unit = VBW_unit
        self.SWT = float(SWT)
        self.SWT_unit = SWT_unit
        self.sweep_cnt = int(sweep_cnt)


'''
    ZNL spectrum analyzer: trace settings
    
    A class to allow easy access to the trace settings of the Rohe und Schwarz
    ZNL for a one trace measurements.

    Attributes:
        window (string): selected window
        refpos (float): Position of reference level reffered to diagram limits (value)
        refpos_unit (string): Position of reference level reffered to diagram limits (unit)
        rangelvl (float): Display range in y direction (value)
        rangelvl_unit (string): Display range in y direction (unit)   
        xAx_type (string): Scaling of x-axis (linear (LIN) or logarithmic (LOG))
        yAx_type (string): Scaling of y-axis (linear (LIN) or logarithmic (LOG))  
        xAx_unit (string): Unit of x values
        yAx_unit (string): Unit of y values
        trace (string): Selected trace
        trace_mode (string): Display mode of trace
        detector (string): selected detector
        meas_number (int): Number of measurement points

    Methods:
        None
'''        
class ZNL_spectrum_settings_one_trace:
    def __init__(self, window, refpos, refpos_unit, rangelvl, rangelvl_unit,
                 xAx_type, yAx_type, xAx_unit, yAx_unit, trace, trace_mode,
                 detector, meas_number):
        
        self.window = window
        self.refpos = float(refpos)
        self.refpos_unit = refpos_unit
        self.rangelvl = float(rangelvl)
        self.rangelvl_unit = rangelvl_unit
        self.xAx_type = xAx_type
        self.yAx_type = yAx_type
        self.xAx_unit = xAx_unit
        self.yAx_unit = yAx_unit
        self.trace = trace
        self.trace_mode = trace_mode
        self.detector = detector
        self.meas_number = int(meas_number)       


'''
    ZNL spectrum analyzer: read a one trace measurement (with/without AUTOPEAK)
    
    This function reads a .dat file for a spectrum analyzer measurement with 
    one trace. It uses the ZNL_spectrum_setting_device and  the
    ZNL_spectrum_setting_one_trace class to give the settings of the instrument
    and the settings of the trace.

    Input Parameters:
        filename (string): Filename (including path) of the .dat file
        autopeak (int): flag which indicates if the autopeak setting was set.
                        Autopeak adds another output (yval2), which gives the
                        smallest of the two measured values (see ZVL manual)
    
    Output parameters:
        device_setting (ZVL_spectrum_setting_device): Settings of the instrument
        trace_setting  (ZVL_spectrum_settings_one_trace): Settings of the trace
        frequency (list): Contains the frequency points
        yval1 (list): Contains the measured values
        yval2 (list): Contains the smallest of the two measured values
                      (only if AUTOPEAK is enabled, otherwise emtpy)
'''
def ZNL_spectrum_read_1trace(filepath, filename, autopeak):
    
    file_data = []
    file_header = []
    frequency = []
    yval1 = []
    yval2 = []
    
    # Basic idea is to test if the entry of the line is a ditig (aka a measured
    # value). If not, it has to be part of the header.
    with open(filepath + filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line and line[0].isdigit():
                row = [float(x) for x in line.split(';')]
                file_data.append(row)
            else:
                row = [str(x) for x in line.split(';')]
                file_header.append(row)
        
    # Assuming the header is always the same and will stay the same forever!
    # This should be the case, if the manual is right...
    # store device settings
    dev_type = file_header[0][1]
    dev_version = file_header[1][1]
    dev_date = file_header[2][1]
    dev_mode = file_header[3][1]
    dev_preamp = file_header[4][1]
    dev_transducer = file_header[5][1]
    dev_center_freq = file_header[6][1]
    dev_center_unit= file_header[6][2] 
    dev_offset = file_header[7][1]
    dev_offset_unit = file_header[7][2]
    dev_xAx_start = file_header[8][1]
    dev_xAx_start_unit = file_header[8][2]
    dev_xAx_stop = file_header[9][1]
    dev_xAx_stop_unit = file_header[9][2]
    dev_span = file_header[10][1]
    dev_span_unit = file_header[10][2]
    dev_reflvl = file_header[11][1]
    dev_reflvl_unit = file_header[11][2]
    dev_offsetlvl = file_header[12][1]
    dev_offsetlvl_unit = file_header[12][2]
    dev_rfatt = file_header[13][1]
    dev_rfatt_unit = file_header[13][2]
    dev_elatt = file_header[14][1]
    dev_elatt_unit = file_header[14][2]
    dev_RBW = file_header[15][1]
    dev_RBW_unit = file_header[15][2]
    dev_VBW = file_header[16][1]
    dev_VBW_unit = file_header[16][2]
    dev_SWT = file_header[17][1]
    dev_SWT_unit = file_header[17][2]
    dev_sweep_cnt = file_header[18][1]
    
    # store trace settings
    tr_window = file_header[19][1]
    tr_refpos = file_header[20][1]
    tr_refpos_unit = file_header[20][2]
    tr_rangelvl = file_header[21][1]
    tr_rangelvl_unit = file_header[21][2]
    tr_xAx_type = file_header[22][1]
    tr_yAx_type = file_header[23][1]
    tr_xAx_unit = file_header[24][1]
    tr_yAx_unit = file_header[25][1]
    tr_trace = file_header[26][1]
    tr_trace_mode = file_header[27][1]
    tr_detector = file_header[28][1]
    tr_meas_number = file_header[29][1]
    
    # There is a class for every device (and for all kinds of measurements).
    # Here, the assignment of the variables is done (Varies for every device).
    # To be honest, there are two classes: device settings and trace settings.
    device_setting = ZNL_spectrum_setting_device(
        dev_type, dev_version, dev_date, dev_mode, dev_preamp, dev_transducer,
        dev_center_freq, dev_center_unit, dev_offset, dev_offset_unit,
        dev_xAx_start, dev_xAx_start_unit, dev_xAx_stop, dev_xAx_stop_unit, 
        dev_span, dev_span_unit, dev_reflvl, dev_reflvl_unit, dev_offsetlvl,
        dev_offsetlvl_unit, dev_rfatt, dev_rfatt_unit, dev_elatt,
        dev_elatt_unit, dev_RBW, dev_RBW_unit, dev_VBW, dev_VBW_unit, dev_SWT,
        dev_SWT_unit, dev_sweep_cnt)

    trace_setting = ZNL_spectrum_settings_one_trace(
        tr_window, tr_refpos, tr_refpos_unit, tr_rangelvl, tr_rangelvl_unit,
        tr_xAx_type, tr_yAx_type, tr_xAx_unit, tr_yAx_unit, tr_trace,
        tr_trace_mode, tr_detector, tr_meas_number)
    
    # Measured data is stored here in two (three if AUTOPEAK is set) separate lists.
    for cnt in range(len(file_data)):
        frequency.append(file_data[cnt][0])
        yval1.append(file_data[cnt][1])
        
        if autopeak == 1:
            yval2.append(file_data[cnt][2])
                         
    return [device_setting, trace_setting, frequency, yval1, yval2]


'''
    This function takes the filename of multiple .dat file from a 1 trace
    spectrum analyzer measurement, extracts the data and stores them in a
    matrix. It uses the function 'ZNL_spectrum_read_1trace' for the extraction
    of the data.
    
    Input Parameters:
        filepath (string): filepath for the stored data
        filenames (list, string): list of strings which containsthe filenames
        autopeak (int): flag which indicates if the AUTOPEAK option was used. 
                        
    Output parameters:
        device_setting (list, ZNL_spectrum_setting_device): Settings of the instrument
        trace_setting  (list, ZNL_spectrum_settings_one_trace): Settings of the trace
        frequency (list): Contains the frequency points
        yval1 (list): Contains the measured values
        yval2 (list): Contains the smallest of the two measured values
                      (only if AUTOPEAK is enabled, otherwise emtpy)
'''
def ZNL_spectrum_read_multrace(filepath, filenames, autopeak):
    
    device_setting = []
    trace_setting = []
    frequency = []
    yval1 = []
    yval2 = []  
    
    for file in filenames:
        [device_temp, trace_temp, frequency_temp, yval1_temp, yval2_temp] = ZNL_spectrum_read_1trace(filepath, file, autopeak)
        device_setting.append(device_temp)
        trace_setting.append(trace_temp)
        frequency.append(frequency_temp)
        yval1.append(yval1_temp)
        yval2.append(yval2_temp)

    return [device_setting, trace_setting, frequency, yval1, yval2]



###############################################################################
############################ independent functions ############################
###############################################################################

'''
    This function plots multiple traces in one plot.
    
    Input Parameters:
        frequency (list):  frequency points of different measurements
        yval (list): measured values of differetn measurements
        title (string): title of the plot
        xlabel (string): label of the x-axis
        ylabel (string): label of the y-axis
        legend (list, string): legend entries
        xfit (int): optional argument for the left and right xlim

        
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