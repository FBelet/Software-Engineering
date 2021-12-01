
"""

## SOFTWARE ENGINEERING ##
      ### GROUP 3 ###
      
# data preparation regional data #

Berenice Flumenbaum & Fabienne Belet


"""

# import modules
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# set working directory
PATH = 'C:/Users/fabie/Universität St.Gallen/Software-Engineering/'
sys.path.append(PATH)


# load functions
import Project_Functions as pc

# define the name for the output file
OUTPUT_NAME = 'Project_Output2'

# save the console output in parallel to a txt file
orig_stdout = sys.stdout
sys.stdout = pc.Output(path=PATH, name=OUTPUT_NAME)

