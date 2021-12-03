"""

## SOFTWARE ENGINEERING ##
      ### GROUP 3 ###
      
# regression on national data #

Berenice Flumenbaum & Fabienne Belet


"""

# import modules
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# set working directory
PATH = '/Users/bereniceflumenbaum/Documents/GitHub/Software Engineering/'
sys.path.append(PATH)


# load functions
import Project_Functions as pc

# define the name for the output file
OUTPUT_NAME = 'Project_Output_Regression'

# save the console output in parallel to a txt file
orig_stdout = sys.stdout
sys.stdout = pc.Output(path=PATH, name=OUTPUT_NAME)


# import data on germany 
table_germany = pd.read_csv(PATH + 'table_germany.csv')
table_germany = table_germany.drop('Unnamed: 0', axis=1)
# rename columns
table_germany.rename(columns = {'German':'National Pop (CH/DE)'}, inplace = True)

# import data on switzerland
table_switzerland = pd.read_csv(PATH + 'table_switzerland.csv')
table_switzerland = table_switzerland.drop('Unnamed: 0', axis=1)
# rename columns
table_switzerland.rename(columns = {'Total Pop Swiss':'National Pop (CH/DE)', 'Population Total': 'Total Population'}, inplace = True)
# drop 2010 to 2012 so that datasets can be merged
table_switzerland2 = table_switzerland.drop(table_switzerland.index[[0,1,2]], axis=0)

# merge tables into one dataset
table_all = pd.concat([table_germany, table_switzerland2])
