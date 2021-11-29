
"""

## SOFTWARE ENGINEERING ##
      ### GROUP 3 ###

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

# load in data using pandas (evtl. hier function mit loop über alle files erstellen, damit alles durch function importiert wird?)
data_germany_foreigners = pd.read_excel(PATH + DATANAME1)
data_germany_pop = pd.read_excel(PATH + DATANAME2)

xls13 = pd.ExcelFile(PATH + DATANAME3)
data_empl_13 = pd.read_excel(xls13, sheet_name=[0,1], header=None) # including first two sheets

xls14 = pd.ExcelFile(PATH + DATANAME4)
data_empl_14 = pd.read_excel(xls14, sheet_name=[0,1], header=None)

xls15 = pd.ExcelFile(PATH + DATANAME5)
data_empl_15 = pd.read_excel(xls15, sheet_name=[0,1], header=None)

xls16 = pd.ExcelFile(PATH + DATANAME6)
data_empl_16 = pd.read_excel(xls16, sheet_name=[0,1], header=None)

xls17 = pd.ExcelFile(PATH + DATANAME7)
data_empl_17 = pd.read_excel(xls17, sheet_name=[0,1], header=None)

xls18 = pd.ExcelFile(PATH + DATANAME8)
data_empl_18 = pd.read_excel(xls18, sheet_name=[0,1], header=None)

xls19 = pd.ExcelFile(PATH + DATANAME9)
data_empl_19 = pd.read_excel(xls19, sheet_name=[0,1], header=None)

xls20 = pd.ExcelFile(PATH + DATANAME10)
data_empl_20 = pd.read_excel(xls20, sheet_name=[0,1], header=None)

xls21 = pd.ExcelFile(PATH + DATANAME11)
data_empl_21 = pd.read_excel(xls21, sheet_name=[0,1], header=None)

# check for missing values and deal with them
## link for data preparation: https://towardsdatascience.com/essential-commands-for-data-preparation-with-pandas-ed01579cf214
pc.my_summary_stats(data_germany_foreigners)
data_germany_foreigners = data_germany_foreigners.dropna()
data_germany_foreigners = data_germany_foreigners.drop(['weiblich', 'männlich'], axis = 1)
data_germany_foreigners = data_germany_foreigners.rename(columns = {'Jahr':'Year', 'Insgesamt':'Total refugees'})

pc.my_summary_stats(data_germany_pop)
data_germany_pop = data_germany_pop.dropna()
data_germany_pop = data_germany_pop.drop(['weiblich', 'männlich'], axis = 1)
data_germany_pop = data_germany_pop.rename(columns = {'Datum':'Year', 'Insgesamt':'Total Population'})

# create a table with population and refugee information/ values 
table_germany_pop = pd.merge(data_germany_foreigners, data_germany_pop)

# structure and organize employment information for 2013
drop_values_1 = [2,3,6,7,8,9]
column_names_1 = ['Year', 'Total Empl', 'German', 'Foreigners']
values13 = pc.organize(data_empl_13, 0, drop_values_1, column_names_1)
drop_values_2 = [1]
column_names_2= ['Year', 'Helper', 'Skilled worker', 'Specialist', 'Expert', 'without educ', 'with educ', 'with academic educ', 'educ unknown']
values13_1 = pc.organize(data_empl_13, 1, drop_values_2, column_names_2)
table13 = pd.merge(values13, values13_1)

# structure and organize employment information for 2014
drop_values_3 = [2,3,6,7,8,9,10]
values14 = pc.organize(data_empl_14, 0, drop_values_3, column_names_1)
values14_1 = pc.organize(data_empl_14, 1, drop_values_2, column_names_2)
table14 = pd.merge(values14, values14_1)

# structure and organize employment information for 2015
values15 = pc.organize(data_empl_15, 0, drop_values_3, column_names_1)
values15_1 = pc.organize(data_empl_15, 1, drop_values_2, column_names_2)
table15 = pd.merge(values15, values15_1)

# structure and organize employment information for 2016
values16 = pc.organize(data_empl_16, 0, drop_values_3, column_names_1)
values16_1 = pc.organize(data_empl_16, 1, drop_values_2, column_names_2)
table16 = pd.merge(values16, values16_1)

# structure and organize employment information for 2017
values17 = pc.organize(data_empl_17, 0, drop_values_3, column_names_1)
values17_1 = pc.organize(data_empl_17, 1, drop_values_2, column_names_2)
table17 = pd.merge(values17, values17_1)

# structure and organize employment information for 2018
values18 = pc.organize(data_empl_18, 0, drop_values_3, column_names_1)
values18_1 = pc.organize(data_empl_18, 1, drop_values_2, column_names_2)
table18 = pd.merge(values18, values18_1)

# structure and organize employment information for 2019
values19 = pc.organize(data_empl_19, 0, drop_values_3, column_names_1)
values19_1 = pc.organize(data_empl_19, 1, drop_values_2, column_names_2)
table19 = pd.merge(values19, values19_1)

# structure and organize employment information for 2020
values20 = pc.organize(data_empl_20, 0, drop_values_3, column_names_1)
values20_1 = pc.organize(data_empl_20, 1, drop_values_2, column_names_2)
table20 = pd.merge(values20, values20_1)

#combining all the single dataframes with information on specific year to one big dataframe containing all the years
table_germany_empl = pd.concat([table13, table14, table15, table16, table17, table18, table19, table20], axis=0)

# merging population information and employment information to a final table with german information - Table Germany
table_germany = pd.merge(table_germany_pop, table_germany_empl)

# save dataframe as a table to the working directory


# Switzerland #
# define data names
dataname1 = 'Erwerbstätige_Schweiz_1960-2020_Infos.xlsx'
dataname2 = 'Erwerbstätige_Schweiz_1991-2020_Nationalität.xlsx'  
dataname3 = 'Erwerbstätige_Schweiz_1991-2020_Wirtschaftszweige.xlsx' # not needed for the analysis
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

XLS10 = pd.ExcelFile(PATH + dataname5)
data_asyl_10 = pd.read_excel(XLS10, sheet_name=['CH-Nati'], header=None) # including first sheets
data_asyl_10 = data_asyl_10['CH-Nati']

XLS11 = pd.ExcelFile(PATH + dataname6)
data_asyl_11 = pd.read_excel(XLS11, sheet_name=['CH-Nati'], header=None)
data_asyl_11 = data_asyl_11['CH-Nati']

XLS12 = pd.ExcelFile(PATH + dataname7)
data_asyl_12 = pd.read_excel(XLS12, sheet_name=['CH-Nati'], header=None)
data_asyl_12 = data_asyl_12['CH-Nati']

XLS13 = pd.ExcelFile(PATH + dataname8)
data_asyl_13 = pd.read_excel(XLS13, sheet_name=['CH-Nati'], header=None)
data_asyl_13 = data_asyl_13['CH-Nati']

XLS14 = pd.ExcelFile(PATH + dataname9)
data_asyl_14 = pd.read_excel(XLS14, sheet_name=['CH-Nati'], header=None)
data_asyl_14 = data_asyl_14['CH-Nati']

XLS15 = pd.ExcelFile(PATH + dataname10)
data_asyl_15 = pd.read_excel(XLS15, sheet_name=['CH-Nati'], header=None)
data_asyl_15 = data_asyl_15['CH-Nati']

XLS16 = pd.ExcelFile(PATH + dataname11)
data_asyl_16 = pd.read_excel(XLS16, sheet_name=['CH-Nati'], header=None)
data_asyl_16 = data_asyl_16['CH-Nati']

XLS17 = pd.ExcelFile(PATH + dataname12)
data_asyl_17 = pd.read_excel(XLS17, sheet_name=['CH-Nati'], header=None)
data_asyl_17 = data_asyl_17['CH-Nati']

XLS18 = pd.ExcelFile(PATH + dataname13)
data_asyl_18 = pd.read_excel(XLS18, sheet_name=['CH-Nati'], header=None)
data_asyl_18 = data_asyl_18['CH-Nati']

XLS19 = pd.ExcelFile(PATH + dataname14)
data_asyl_19 = pd.read_excel(XLS19, sheet_name=['CH-Nati'], header=None)
data_asyl_19 = data_asyl_19['CH-Nati']

XLS20 = pd.ExcelFile(PATH + dataname15)
data_asyl_20 = pd.read_excel(XLS20, sheet_name=['CH-Nati'], header=None)
data_asyl_20 = data_asyl_20['CH-Nati']

# check for missing values and deal with them
pc.my_summary_stats(data_swiss_pop) # no missing values and nan values found

pc.my_summary_stats(data_swiss_nat_sec) # missing values and need to change rows to columns

drop_values_CH = data_swiss_nat_sec.iloc[:, 13:57]
drop_rows = [0,1,2,3,4,5,6,7,8]
column_names_CH = ['Year', 'Total Empl', 'Total Sec.1', 'Total Sec.2', 
                   'Total Sec.3', 'Total Swiss', 'Total Swiss Sec.1', 
                   'Total Swiss Sec.2', 'Total Swiss Sec.3', 'Total Foreigners',
                   'Total Foreign Sec. 1', 'Total Foreign Sec.2', 'Total Foreign Sec.3']

data_swiss_nat_sec = pc.organize_CH(data_swiss_nat_sec, drop_rows, drop_values_CH, column_names_CH)
pc.my_summary_stats(data_swiss_nat_sec) # no missing values and nan values left

pc.my_summary_stats(data_swiss_nat)
data_swiss_nat = data_swiss_nat.drop(data_swiss_nat.iloc[:, 1:8], axis=1)
drop_values_CH1 = data_swiss_nat.iloc[:, 7: ]
column_names_CH1 = ['Year', 'Empl settled', 'Empl resident', 'Empl saison', 
                    'Empl border', 'Empl shortterm', 'Empl other']
data_swiss_nat = pc.organize_CH(data_swiss_nat, drop_rows, drop_values_CH1, column_names_CH1)
pc.my_summary_stats(data_swiss_nat)

# structure and organize information for 2010
drop_values_CH2 = [2,3,5,6,8,9,11,12,14,15]
column_names_CH2 = ['Year', 'Refugees Total', 'Residents Permit B Total', 
                    'Residents Permit B employed', 'Residents Permit B unempl', 
                    'Settled Total']

data_asyl_10 = pc.organize_CH_2(data_asyl_10, drop_values_CH2, column_names_CH2)

# combine all the datafiles into one single file for Switzerland