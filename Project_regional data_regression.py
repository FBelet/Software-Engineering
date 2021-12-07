"""

## SOFTWARE ENGINEERING ##
      ### GROUP 3 ###
      
# analysis and regression of regional data #

Berenice Flumenbaum & Fabienne Belet


"""

# import modules
import sys
import pandas as pd
import os

# set working directory
PATH = '/Users/bereniceflumenbaum/Documents/GitHub/Software Engineering/'
sys.path.append(PATH)


# load functions
import Project_Functions as pc

# define the name for the output file
OUTPUT_NAME = 'Project_Output_Regression2'

# save the console output in parallel to a txt file
orig_stdout = sys.stdout
sys.stdout = pc.Output(path=PATH, name=OUTPUT_NAME)

# import datasets of the Bundesländer 
PATH2 = r'/Users/bereniceflumenbaum/Documents/GitHub/Software Engineering/Final Datasets/'
folderpath = PATH2
filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]
all_files = []

for path in filepaths:
    with open(path, 'r') as f:
        file = f.readlines()
        all_files.append(file)

pd.read_csv(all_files[0])

    
