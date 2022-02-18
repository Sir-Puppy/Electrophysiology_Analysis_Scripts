# -*- coding: utf-8 -*-
"""
Created on Fri May  7 14:02:15 2021

For fitting of gating current raw traces in stimfit

To use this in Stimfit, write:
    
import Batch_fitting2
Batch_fitting2.trace_fit()

Warning, Naming is not yet perfected!!
"""
#make sure to set the start cursor as the peak
import stf

import csv

Result = []

file_header = ["SSE", "Tau_0", "Amp_0", "Offset"]


def trace_fit():
    
    stf.set_channel(3)
    
    f = open("C:\\Users\HPNote2019\Desktop\Stim fit trial\Stimfit.csv", 'wb')

    for n in range(6, 27, 5):
        stf.select_trace(n)
        stf.set_trace(n)
        stf.leastsq(0)
        Result.append(stf.leastsq(0))
        Name = stf.get_filename()    
    with f as file:
        csv.writer(file).writerow([Name])
        csv.writer(file).writerow(file_header)
        
        for item in Result:
            csv.writer(file).writerow([item["SSE"], item["Tau_0"], item["Amp_0"], item["Offset"]])
    f.close()
    

