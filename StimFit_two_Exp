# -*- coding: utf-8 -*-
"""
Created on Fri May  7 14:02:15 2021

For fitting of gating current raw traces in stimfit

To use this in Stimfit, write:
    
import StimFit_two_Exp (Or whatever name you save it as)
StimFit_two_Exp.trace_fit()

"""
#make sure to set the start cursor as the peak
import stf

import csv

Result = []

file_header = ["SSE", "Tau_0", "Amp_0", "Offset"]       #Header that will be used when 


def trace_fit():
    
    stf.set_channel(3)                                   #chooses which trace to use
    
    f = open("<Your folder here>", 'wb')                 #Opens the folder where the data will be written

    for n in range(6, 27, 5):                            #parameter and trace selection
        stf.select_trace(n)
        stf.set_trace(n)
        stf.leastsq(0)
        Result.append(stf.leastsq(0))
        Name = stf.get_filename()    
    with f as file:                                       #Writing of data
        csv.writer(file).writerow([Name])
        csv.writer(file).writerow(file_header)
        
        for item in Result:
            csv.writer(file).writerow([item["SSE"], item["Tau_0"], item["Amp_0"], item["Offset"]])
    f.close()
    
   
