
"""

## SOFTWARE ENGINEERING ##
      ### GROUP 3 ###

Berenice Flumenbaum & Fabienne Belet


"""

# import modules
import sys
import pandas as pd
import numpy as np


# set working directory
PATH = 'C:/Users/fabie/Universität St.Gallen/Software-Engineering/'
sys.path.append(PATH)

# load functions
import Project_Functions as pc

# define the name for the output file
OUTPUT_NAME = 'Project_Output'

# save the console output in parallel to a txt file
orig_stdout = sys.stdout
sys.stdout = pc.Output(path=PATH, name=OUTPUT_NAME)

## DATA PREPARATION ##

# Germany #
# define data names
DATANAME1 = 'Schutzsuchende_Deutschland_2010-2020.xlsx'
DATANAME2 = 'Bevölkerungsentwicklung_Deutschland_2010-2020.xlsx'
DATANAME3 = 'Beschäftigte_Deutschland_201312.xlsx'
DATANAME4 = 'Beschäftigte_Deutschland_201412.xlsx'
DATANAME5 = 'Beschäftigte_Deutschland_201512.xlsx'
DATANAME6 = 'Beschäftigte_Deutschland_201612.xlsx'
DATANAME7 = 'Beschäftigte_Deutschland_201712.xlsx'
DATANAME8 = 'Beschäftigte_Deutschland_201812.xlsx'
DATANAME9 = 'Beschäftigte_Deutschland_201912.xlsx'
DATANAME10 = 'Beschäftigte_Deutschland_202012.xlsx'
DATANAME11 = 'Beschäftigte_Deutschland_202103.xlsx'

# load in data using pandas
data_germany_foreigners = pd.read_excel(PATH + DATANAME1)
data_germany_pop = pd.read_excel(PATH + DATANAME2)

xls13 = pd.ExcelFile(PATH + DATANAME3)
data_empl_13 = pd.read_excel(xls13, sheet_name=None)

xls14 = pd.ExcelFile(PATH + DATANAME4)
data_empl_14 = pd.read_excel(xls14, sheet_name=None)

xls15 = pd.ExcelFile(PATH + DATANAME5)
data_empl_15 = pd.read_excel(xls15, sheet_name=None)

xls16 = pd.ExcelFile(PATH + DATANAME6)
data_empl_15 = pd.read_excel(xls16, sheet_name=None)

xls17 = pd.ExcelFile(PATH + DATANAME7)
data_empl_17 = pd.read_excel(xls17, sheet_name=None)

xls18 = pd.ExcelFile(PATH + DATANAME8)
data_empl_18 = pd.read_excel(xls18, sheet_name=None)

xls19 = pd.ExcelFile(PATH + DATANAME9)
data_empl_19 = pd.read_excel(xls19, sheet_name=None)

xls20 = pd.ExcelFile(PATH + DATANAME10)
data_empl_20 = pd.read_excel(xls20, sheet_name=None)

xls21 = pd.ExcelFile(PATH + DATANAME11)
data_empl_21 = pd.read_excel(xls21, sheet_name=None)

# check for missing values and deal with them



# Switzerland #
# define data names

# load in data using pandas