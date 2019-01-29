# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 10:38:22 2019

@author: Robert Schuldt
@email: rfschuldt@uams.edu

Cleaning Chronic Conidtions Warehouse Data for analysis. 
"""

#Import useful libraries

import pandas as pd
import os

#We are going to bring in the main data set. We are looking for the
#first patient episode of care and evaluation in the OASIS file. 

filename = "hha_assessment_summary.sas7bdat"
lines_number = sum(1 for line in open(filename))

chunk_size = 100000

counter = 0
completed = 0

oasis_df = pd.read_sas(filename, format = 'sas7bdat', encoding='latin1', chunksize = chunk_size)

for chunk in oasis_df:
    counter += chunk_size
    new_completed = int(round(float(counter)/lines_number*100))
    if (new_completed > completed):
        completed = new_completed
        print("Completed" , completed , "%")
