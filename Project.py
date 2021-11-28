
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

# load in data using pandas (evtl. hier function erstellen, damit alles durch function importiert wird?)
data_germany_foreigners = pd.read_excel(PATH + DATANAME1)
data_germany_pop = pd.read_excel(PATH + DATANAME2)

xls13 = pd.ExcelFile(PATH + DATANAME3)
data_empl_13 = pd.read_excel(xls13, sheet_name=[0,1], header=None) # including all sheets

xls14 = pd.ExcelFile(PATH + DATANAME4)
data_empl_14 = pd.read_excel(xls14, sheet_name=[0,1], header=None)

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
## link for data preparation: https://towardsdatascience.com/essential-commands-for-data-preparation-with-pandas-ed01579cf214
data_germany_foreigners.isnull()
data_germany_foreigners = data_germany_foreigners.dropna()
data_germany_foreigners = data_germany_foreigners.drop(['weiblich', 'männlich'], axis = 1)
data_germany_foreigners = data_germany_foreigners.rename(columns = {'Jahr':'Year', 'Insgesamt':'Total refugees'})
data_germany_pop.isnull()
data_germany_pop = data_germany_pop.dropna()
data_germany_pop = data_germany_pop.drop(['weiblich', 'männlich'], axis = 1)
data_germany_pop = data_germany_pop.rename(columns = {'Datum':'Year', 'Insgesamt':'Total Population'})

# create a table with population and refugee information/ values 
table_germany_pop = pd.merge(data_germany_foreigners, data_germany_pop)

# structure and organize employment information for 2013
values13 = data_empl_13[0]
values13 = values13.head(2)
values13 = values13.dropna(axis = 1)
values13 = values13.drop(values13[[2,3,6,7,8,9]], axis=1)
values13 = values13.drop(0)
values13.columns = ['Year', 'Total Empl', 'German', 'Foreigners']

values13_1 = data_empl_13[1]
values13_1 = values13_1.head(2)
values13_1 = values13_1.dropna(axis = 1)
values13_1 = values13_1.drop(1, axis=1)
values13_1 = values13_1.drop(0)
values13_1.columns = ['Year', 'Helper', 'Skilled worker', 'Specialist', 'Expert', 'without educ', 'with educ', 'with academic educ', 'educ unknown']

table13 = pd.merge(values13, values13_1)

# structure and organize employment information for 2014
values14 = data_empl_14[0]
values14 = values14.head(2)
values14 = values14.dropna(axis = 1)
values14 = values14.drop(values14[[2,3,6,7,8,9,10]], axis=1)
values14 = values14.drop(0)
values14.columns = ['Year', 'Total Empl', 'German', 'Foreigners']

values14_1 = data_empl_14[1]
values14_1 = values14_1.head(2)
values14_1 = values14_1.dropna(axis = 1)
values14_1 = values14_1.drop(1, axis=1)
values14_1 = values14_1.drop(0)
values14_1.columns = ['Year', 'Helper', 'Skilled worker', 'Specialist', 'Expert', 'without educ', 'with educ', 'with academic educ', 'educ unknown']

table14 = pd.merge(values14, values14_1)


#combining all the single dataframes with information on specific year to one big dataframe containing all the years
table_germany_empl = pd.concat([table13, table14], axis=0)

# merging population information and employment information to a final table with german information - Table Germany





# Switzerland #
# define data names
dataname1 = 'Erwerbstätige_Schweiz_1960-2020_Nationalität & Wirtschaftssektoren.xlsx' ##welcher davon (1,2,3) nutzen?
dataname2 = 'Erwerbstätige_Schweiz_1991-2020_Nationalität.xlsx'  ##welcher davon (1,2,3) nutzen?
dataname3 = 'Erwerbstätige_Schweiz_1991-2020_Wirtschaftszweige.xlsx' ##welcher davon (1,2,3) nutzen?
dataname4 = 'Bevölkerungsentwicklung_Schweiz_2000-2020.xlsx'

dataname5 = 'Asylstatistik_Schweiz_201012.xlsx'
dataname6 = 'Asylstatistik_Schweiz_201112.xlsx'
dataname7 = 'Asylstatistik_Schweiz_201212.xlsx'
dataname8 = 'Asylstatistik_Schweiz_201312.xlsx'
dataname9 = 'Asylstatistik_Schweiz_201412.xlsx'
dataname10 = 'Asylstatistik_Schweiz_201512.xlsx'
dataname11 = 'Asylstatistik_Schweiz_201612.xlsx'
dataname12 = 'Asylstatistik_Schweiz_201712.xlsx'
dataname13 = 'Asylstatistik_Schweiz_201812.xlsx'
dataname14 = 'Asylstatistik_Schweiz_201912.xlsx'
dataname15 = 'Asylstatistik_Schweiz_202012.xlsx'

# load in data using pandas
data_swiss_pop = pd.read_excel(PATH + dataname4)
data_swiss_nat_sec = pd.read_excel(PATH + dataname1) #nationality and economic sectors
data_swiss_nat = pd.read_excel(PATH + dataname2) #nationality
data_swiss_sec = pd.read_excel(PATH + dataname3) #economic secotrs

XLS10 = pd.ExcelFile(PATH + dataname5)
data_asyl_10 = pd.read_excel(XLS10, sheet_name=None) # including all sheets

XLS11 = pd.ExcelFile(PATH + dataname6)
data_asyl_11 = pd.read_excel(XLS11, sheet_name=None)

XLS12 = pd.ExcelFile(PATH + dataname7)
data_asyl_12 = pd.read_excel(XLS12, sheet_name=None)

XLS13 = pd.ExcelFile(PATH + dataname8)
data_asyl_13 = pd.read_excel(XLS13, sheet_name=None)

XLS14 = pd.ExcelFile(PATH + dataname9)
data_asyl_14 = pd.read_excel(XLS14, sheet_name=None)

XLS15 = pd.ExcelFile(PATH + dataname10)
data_asyl_15 = pd.read_excel(XLS15, sheet_name=None)

XLS16 = pd.ExcelFile(PATH + dataname11)
data_asyl_16 = pd.read_excel(XLS16, sheet_name=None)

XLS17 = pd.ExcelFile(PATH + dataname12)
data_asyl_17 = pd.read_excel(XLS17, sheet_name=None)

XLS18 = pd.ExcelFile(PATH + dataname13)
data_asyl_18 = pd.read_excel(XLS18, sheet_name=None)

XLS19 = pd.ExcelFile(PATH + dataname14)
data_asyl_19 = pd.read_excel(XLS19, sheet_name=None)

XLS20 = pd.ExcelFile(PATH + dataname15)
data_asyl_20 = pd.read_excel(XLS20, sheet_name=None)

# check for missing values and deal with them


# combine all the datafiles into one single file for Switzerland