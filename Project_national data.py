
"""

## SOFTWARE ENGINEERING ##
      ### GROUP 3 ###
      
# data preparation national data #

Berenice Flumenbaum & Fabienne Belet


"""

# import modules
import sys
import pandas as pd

# set working directory
PATH = '/Users/bereniceflumenbaum/Documents/GitHub/Software Engineering/'
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
DATANAME12 = 'Arbeitslose_Quote_Deutschland.xlsx'

# load in data using pandas
data_germany_foreigners = pd.read_excel(PATH + DATANAME1)
data_germany_pop = pd.read_excel(PATH + DATANAME2)
data_germany_unempl = pd.ExcelFile(PATH + DATANAME12)
data_germany_unempl = pd.read_excel(data_germany_unempl, sheet_name = [0,1], header=None)

xls13 = pd.ExcelFile(PATH + DATANAME3)
data_empl_13 = pd.read_excel(xls13, sheet_name=[0,1,2], header=None) # including first three sheets

xls14 = pd.ExcelFile(PATH + DATANAME4)
data_empl_14 = pd.read_excel(xls14, sheet_name=[0,1,2], header=None)

xls15 = pd.ExcelFile(PATH + DATANAME5)
data_empl_15 = pd.read_excel(xls15, sheet_name=[0,1,2], header=None)

xls16 = pd.ExcelFile(PATH + DATANAME6)
data_empl_16 = pd.read_excel(xls16, sheet_name=[0,1,2], header=None)

xls17 = pd.ExcelFile(PATH + DATANAME7)
data_empl_17 = pd.read_excel(xls17, sheet_name=[0,1,2], header=None)

xls18 = pd.ExcelFile(PATH + DATANAME8)
data_empl_18 = pd.read_excel(xls18, sheet_name=[0,1,2], header=None)

xls19 = pd.ExcelFile(PATH + DATANAME9)
data_empl_19 = pd.read_excel(xls19, sheet_name=[0,1,2], header=None)

xls20 = pd.ExcelFile(PATH + DATANAME10)
data_empl_20 = pd.read_excel(xls20, sheet_name=[0,1,2], header=None)

xls21 = pd.ExcelFile(PATH + DATANAME11)
data_empl_21 = pd.read_excel(xls21, sheet_name=[0,1,2], header=None)

# check for missing values and deal with them
pc.my_summary_stats(data_germany_foreigners)
data_germany_foreigners = data_germany_foreigners.dropna() # drop nan values
data_germany_foreigners = data_germany_foreigners.drop(['weiblich', 'männlich'], axis = 1) # drop column weiblich and männlich
data_germany_foreigners = data_germany_foreigners.rename(columns = {'Jahr':'Year', 'Insgesamt':'Total Refugees'}) # rename columns

pc.my_summary_stats(data_germany_pop)
data_germany_pop = data_germany_pop.dropna() # drop nan values
data_germany_pop = data_germany_pop.drop(['weiblich', 'männlich'], axis = 1) # drop column weiblich and männlich
data_germany_pop = data_germany_pop.rename(columns = {'Datum':'Year', 'Insgesamt':'Total Population'}) # rename columns

germany_unempl = data_germany_unempl[0] # choose specific dataframe from dictionary
germany_unempl.columns = ['Year', 'Unemployment'] # name columns
germany_unempl = germany_unempl.drop(0) # drop row 0
pc.my_summary_stats(germany_unempl) # no missing values
germany_unempl_rate = data_germany_unempl[1] # choose specific dataframe from dictionary
germany_unempl_rate.columns = ['Year', 'Unemployment Rate'] # name columns
germany_unempl_rate = germany_unempl_rate.drop(0) # drop row 0
pc.my_summary_stats(germany_unempl_rate) # no missing values

table_unempl = pd.merge(germany_unempl, germany_unempl_rate)
table_unempl = table_unempl.drop([0,1,2])

# create a table with population and refugee information/ values 
table_germany_pop = pd.merge(data_germany_foreigners, data_germany_pop)
table_germany_pop = table_germany_pop.drop([0,1,2])
table_all = pd.merge(table_germany_pop, table_unempl)

# structure and organize employment information for 2013
drop_values_1 = [2,3,6,7,8,9]
column_names_1 = ['Year', 'Total Empl (geringfügig)', 'Total Empl German (geringfügig)', 'Total Empl Foreigners (geringfügig)']
values13 = pc.organize_D(data_empl_13, 0, drop_values_1, column_names_1)
drop_values_2 = [1]
column_names_2= ['Year', 'Helper', 'Skilled worker', 'Specialist', 'Expert', 'without educ', 'with educ', 'with academic educ', 'educ unknown']
values13_1 = pc.organize_D(data_empl_13, 1, drop_values_2, column_names_2)
table13 = pd.merge(values13, values13_1)
pc.my_summary_stats(table13) # no missing values

# structure and organize employment information for 2014 (only employment information for "geringfügig Beschäftigte")
drop_values_3 = [2,3,6,7,8,9,10]
values14 = pc.organize_D(data_empl_14, 0, drop_values_3, column_names_1)
values14_1 = pc.organize_D(data_empl_14, 1, drop_values_2, column_names_2)
table14 = pd.merge(values14, values14_1)
pc.my_summary_stats(table14) # no missing values

# structure and organize employment information for 2015
values15 = pc.organize_D(data_empl_15, 0, drop_values_3, column_names_1)
values15_1 = pc.organize_D(data_empl_15, 1, drop_values_2, column_names_2)
table15 = pd.merge(values15, values15_1)
pc.my_summary_stats(table15) # no missing values

# structure and organize employment information for 2016
values16 = pc.organize_D(data_empl_16, 0, drop_values_3, column_names_1)
values16_1 = pc.organize_D(data_empl_16, 1, drop_values_2, column_names_2)
table16 = pd.merge(values16, values16_1)
pc.my_summary_stats(table16) # no missing values

# structure and organize employment information for 2017
values17 = pc.organize_D(data_empl_17, 0, drop_values_3, column_names_1)
values17_1 = pc.organize_D(data_empl_17, 1, drop_values_2, column_names_2)
table17 = pd.merge(values17, values17_1)
pc.my_summary_stats(table17) # no missing values

# structure and organize employment information for 2018
values18 = pc.organize_D(data_empl_18, 0, drop_values_3, column_names_1)
values18_1 = pc.organize_D(data_empl_18, 1, drop_values_2, column_names_2)
table18 = pd.merge(values18, values18_1)
pc.my_summary_stats(table18) # no missing values

# structure and organize employment information for 2019
values19 = pc.organize_D(data_empl_19, 0, drop_values_3, column_names_1)
values19_1 = pc.organize_D(data_empl_19, 1, drop_values_2, column_names_2)
table19 = pd.merge(values19, values19_1)
pc.my_summary_stats(table19) # no missing values

# structure and organize employment information for 2020
values20 = pc.organize_D(data_empl_20, 0, drop_values_3, column_names_1)
values20_1 = pc.organize_D(data_empl_20, 1, drop_values_2, column_names_2)
table20 = pd.merge(values20, values20_1)
pc.my_summary_stats(table20) # no missing values

# combine information for total employment from 2013-2020
table_empl_total = pd.concat([data_empl_13[2], data_empl_14[2], data_empl_15[2],
                              data_empl_16[2], data_empl_17[2], data_empl_18[2],
                              data_empl_19[2], data_empl_20[2]])
table_empl_total = table_empl_total.drop(0)
table_empl_total.columns = ['Year', 'Total Empl', 'Total Empl German', 'Total Empl Foreigners']

#combining all the single dataframes with information on specific year to one big dataframe containing all the years
table_germany_empl = pd.concat([table13, table14, table15, table16, table17, table18, table19, table20], axis=0)

# merging population information and employment information to a final table with german information - Table Germany
table_germany = pd.merge(pd.merge(table_all, table_germany_empl, on='Year'), table_empl_total, on='Year')

# save dataframe as a table to the working directory
PATH2 = '/Users/bereniceflumenbaum/Documents/GitHub/Software Engineering/Final Datasets/'
table_germany.to_csv(PATH2 + 'table_germany.csv')

################################################################################

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
dataname16 = 'Arbeitslosenquote_Schweiz.xlsx'
dataname17 = 'Arbeitslose_Schweiz.xlsx'

# load in data using pandas
data_swiss_pop = pd.read_excel(PATH + dataname4)
data_swiss_nat_sec = pd.read_excel(PATH + dataname1) #nationality and economic sectors
data_swiss_nat = pd.read_excel(PATH + dataname2) #nationality

data_swiss_unempl = pd.ExcelFile(PATH + dataname17)
data_swiss_unempl = pd.read_excel(data_swiss_unempl, sheet_name=['Overview'], header=None)
data_swiss_unempl = data_swiss_unempl['Overview']
data_swiss_unempl_quote = pd.ExcelFile(PATH + dataname16)
data_swiss_unempl_quote = pd.read_excel(data_swiss_unempl_quote, sheet_name=['Overview'], header=None)
data_swiss_unempl_quote = data_swiss_unempl_quote['Overview']

XLS10 = pd.ExcelFile(PATH + dataname5)
data_asyl_10 = pd.read_excel(XLS10, sheet_name=['CH-Nati'], header=None) # including specific sheet
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
data_swiss_pop.columns = ['Year', 'Total Population', 'Total Pop Swiss', 'Total Pop Foreigners']

pc.my_summary_stats(data_swiss_nat_sec) # some missing values, but not in relevant columns
drop_values_CH = data_swiss_nat_sec.iloc[:, 13:57]
drop_rows = [0,1,2,3,4,5,6,7,8]
column_names_CH = ['Year', 'Total Empl', 'Total Sec.1', 'Total Sec.2', 
                   'Total Sec.3', 'Total Empl Swiss', 'Total Swiss Sec.1', 
                   'Total Swiss Sec.2', 'Total Swiss Sec.3', 'Total Empl Foreigners',
                   'Total Foreign Sec. 1', 'Total Foreign Sec.2', 'Total Foreign Sec.3']
data_swiss_nat_sec = pc.organize_CH1(data_swiss_nat_sec, drop_rows, drop_values_CH, column_names_CH)
pc.my_summary_stats(data_swiss_nat_sec) # no missing values and nan values left

# create a table 
table_swiss_nat = pd.merge(data_swiss_pop, data_swiss_nat_sec)

pc.my_summary_stats(data_swiss_nat) # some missing values, but not in relevant columns
data_swiss_nat = data_swiss_nat.drop(data_swiss_nat.iloc[:, 1:8], axis=1)
drop_values_CH1 = data_swiss_nat.iloc[:, 7: ]
column_names_CH1 = ['Year', 'Empl settled', 'Empl resident', 'Empl saison', 
                    'Empl border', 'Empl shortterm', 'Empl other']
data_swiss_nat = pc.organize_CH1(data_swiss_nat, drop_rows, drop_values_CH1, column_names_CH1)
pc.my_summary_stats(data_swiss_nat)

# create a table
table_swiss_nat = pd.merge(table_swiss_nat, data_swiss_nat)

data_swiss_unempl.columns = ['Year', 'Unemployment']
data_swiss_unempl = data_swiss_unempl.drop(0)
pc.my_summary_stats(data_swiss_unempl) # no missing values
data_swiss_unempl_quote.columns = ['Year', 'Unemployment Rate']
data_swiss_unempl_quote = data_swiss_unempl_quote.drop(0)
pc.my_summary_stats(data_swiss_unempl_quote) # no missing values
table_swiss_unempl = pd.merge(data_swiss_unempl, data_swiss_unempl_quote)

#create a table with all relevant information
table_swiss_general = pd.merge(table_swiss_nat, table_swiss_unempl)

# structure and organize information for 2010
drop_values_CH2 = [2,3,5,6,8,9,11,12,14,15]
column_names_CH2 = ['Year', 'Total Refugees', 'Residents Permit B Total', 
                    'Residents Permit B employed', 'Residents Permit B unempl', 
                    'Settled Total']

data_asyl_10 = pc.organize_CH2(data_asyl_10, drop_values_CH2, column_names_CH2)
pc.my_summary_stats(data_asyl_10) # no missing values

# structure and organize information for 2011
data_asyl_11 = pc.organize_CH2(data_asyl_11, drop_values_CH2, column_names_CH2)
pc.my_summary_stats(data_asyl_11) # no missing values

# structure and organize information for 2012
data_asyl_12 = pc.organize_CH2(data_asyl_12, drop_values_CH2, column_names_CH2)
pc.my_summary_stats(data_asyl_12) # no missing values

# structure and organize information for 2013
data_asyl_13 = pc.organize_CH2(data_asyl_13, drop_values_CH2, column_names_CH2)
pc.my_summary_stats(data_asyl_13) # no missing values
 
# struture and organize information for 2014
data_asyl_14 = pc.organize_CH2(data_asyl_14, drop_values_CH2, column_names_CH2)
pc.my_summary_stats(data_asyl_14) # no missing values

# structure and organize information for 2015
data_asyl_15 = pc.organize_CH2(data_asyl_15, drop_values_CH2, column_names_CH2)
pc.my_summary_stats(data_asyl_15) # no missing values

# structure and organize information for 2016
data_asyl_16 = pc.organize_CH2(data_asyl_16, drop_values_CH2, column_names_CH2)
pc.my_summary_stats(data_asyl_16) # no missing values

# structure and organize information for 2017
data_asyl_17 = pc.organize_CH2(data_asyl_17, drop_values_CH2, column_names_CH2)
pc.my_summary_stats(data_asyl_17) # no missing values
 
# structure and organize information for 2018
data_asyl_18 = pc.organize_CH2(data_asyl_18, drop_values_CH2, column_names_CH2)
pc.my_summary_stats(data_asyl_18) # no missing values

# structure and organize infromation for 2019
data_asyl_19 = pc.organize_CH2(data_asyl_19, drop_values_CH2, column_names_CH2)
pc.my_summary_stats(data_asyl_19) # no missing values

# structure and organize information for 2020
data_asyl_20 = pc.organize_CH2(data_asyl_20, drop_values_CH2, column_names_CH2) 
pc.my_summary_stats(data_asyl_20) # no missing values

# combine all the datafiles into one single file/table for Switzerland
table_swiss_asyl = pd.concat([data_asyl_10, data_asyl_11, data_asyl_12,
                              data_asyl_13, data_asyl_14, data_asyl_15,
                              data_asyl_16, data_asyl_17, data_asyl_18, 
                              data_asyl_19, data_asyl_20], axis=0)

table_switzerland = pd.merge(table_swiss_general, table_swiss_asyl)
table_switzerland = table_switzerland.drop('Empl saison', axis=1)

# save dataframe as a table to the working directory
table_switzerland.to_csv(PATH2 + 'table_switzerland.csv')

# closing the output file
sys.stdout.output.close()
sys.stdout = orig_stdout

######## End of national data preparation ########