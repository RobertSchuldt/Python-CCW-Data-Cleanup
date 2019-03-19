# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 10:38:22 2019

@author: Robert Schuldt
@email: rfschuldt@uams.edu

Cleaning Chronic Conidtions Warehouse Data for analysis. 
"""

#Import useful libraries

from sas7bdat import SAS7BDAT
from itertools import islice
import pandas as pd
#We are going to bring in the main data set. We are looking for the
#first patient episode of care and evaluation in the OASIS file. 




filename = "pqi_icd10.sas7bdat"



#Now import file and turn into a pandas df
with SAS7BDAT(filename) as reader:
    df = reader.to_data_frame()
    for line_number, line in enumerate(reader,1000):
        print(line_number)
      




        
    
    
        
            
