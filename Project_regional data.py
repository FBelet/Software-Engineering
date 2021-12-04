
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

## DATA PREPARATION ##

# Regional data for Germany #
# define data names

DATA1 = 'Schutzsuchende_Deutschland_Bundesländer.xlsx'
DATA2 = 'Bevölkerungsentwicklung_Deutschland_Bundesländer.xlsx'
DATA3 = 'Arbeitslose_Quote_Deutschland.xlsx'
DATA4 = 'Beschäftigte_Thüringen.xlsx'
DATA5 = 'Beschäftigte_Schleswig-Holstein.xlsx'
DATA6 = 'Beschäftigte_Sachsen-Anhalt.xlsx'
DATA7 = 'Beschäftigte_Sachsen.xlsx'
DATA8 = 'Beschäftigte_Saarland.xlsx'
DATA9 = 'Beschäftigte_Rheinland-Pfalz.xlsx'
DATA10 = 'Beschäftigte_Nordrhein-Westfalen.xlsx'
DATA11 = 'Beschäftigte_Niedersachsen.xlsx'
DATA12 = 'Beschäftigte_Mecklenburg-Vorpommern.xlsx'
DATA13 = 'Beschäftigte_Hessen.xlsx'
DATA14 = 'Beschäftigte_Hamburg.xlsx'
DATA15 = 'Beschäftigte_Bremen.xlsx'
DATA16 = 'Beschäftigte_Brandenburg.xlsx'
DATA17 = 'Beschäftigte_Berlin.xlsx'
DATA18 = 'Beschäftigte_Bayern.xlsx'
DATA19 = 'Beschäftigte_Baden-Württemberg.xlsx'

# load in data using pandas
data_germany_foreigners = pd.read_excel(PATH + DATA1)
data_germany_pop = pd.read_excel(PATH + DATA2)
data_germany_unempl = pd.ExcelFile(PATH + DATA3)
data_germany_unempl = pd.read_excel(data_germany_unempl, sheet_name = [2,3], header=None)

xls1 = pd.ExcelFile(PATH + DATA4)
Empl_Thüringen = pd.read_excel(xls1, sheet_name = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
                               header=None)

xls2 = pd.ExcelFile(PATH + DATA5)
Empl_Schleswig_Holstein = pd.read_excel(xls2, sheet_name = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
                                        header=None)

xls3 = pd.ExcelFile(PATH + DATA6)
Empl_Sachsen_Anhalt = pd.read_excel(xls3, sheet_name = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
                                    header=None)

xls4 = pd.ExcelFile(PATH + DATA7)
Empl_Sachsen = pd.read_excel(xls4, sheet_name = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 
                             header=None)

xls5 = pd.ExcelFile(PATH + DATA8)
Empl_Saarland = pd.read_excel(xls5, sheet_name = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
                              header=None)

xls6 = pd.ExcelFile(PATH + DATA9)
Empl_Rheinland_Pfalz = pd.read_excel(xls6, sheet_name = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
                                     header=None)

xls7 = pd.ExcelFile(PATH + DATA10)
Empl_Nordrhein_Westfalen = pd.read_excel(xls7, sheet_name = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 
                                         header=None)

xls8 = pd.ExcelFile(PATH + DATA11)
Empl_Niedersachsen = pd.read_excel(xls8, sheet_name = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
                                   header=None)

xls9 = pd.ExcelFile(PATH + DATA12)
Empl_Mecklenburg_Vorpommern = pd.read_excel(xls9, sheet_name = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
                                            header=None)

xls10 = pd.ExcelFile(PATH + DATA13)
Empl_Hessen = pd.read_excel(xls10, sheet_name = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
                            header=None)

xls11 = pd.ExcelFile(PATH + DATA14)
Empl_Hamburg = pd.read_excel(xls11, sheet_name = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
                             header=None)

xls12 = pd.ExcelFile(PATH + DATA15)
Empl_Bremen = pd.read_excel(xls12, sheet_name = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
                            header=None)

xls13 = pd.ExcelFile(PATH + DATA16)
Empl_Brandenburg = pd.read_excel(xls13, sheet_name = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
                                 header=None)

xls14 = pd.ExcelFile(PATH + DATA17)
Empl_Berlin = pd.read_excel(xls14, sheet_name = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
                            header=None)

xls15 = pd.ExcelFile(PATH + DATA18)
Empl_Bayern = pd.read_excel(xls15, sheet_name = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
                            header=None)

xls16 = pd.ExcelFile(PATH + DATA19)
Empl_Baden_Württemberg = pd.read_excel(xls16, sheet_name = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
                                       header=None)

# check for missing values and organize the tables
pc.my_summary_stats(data_germany_foreigners) # no missing values
drop_values = [1,2,4,5,7,8,10,11,13,14,16,17,19,20,22,23,25,26,28,29,31,32,34,35,37,38,40,41,43,44,46,47]
column_names = ['Year', 'Baden-Württemberg', 'Bayern', 'Berlin', 'Brandenburg', 'Bremen', 
                'Hamburg', 'Hessen', 'Mecklenburg-Vorpommern', 'Niedersachsen', 
                'Nordrhein-Westfalen', 'Rheinland-Pfalz', 'Saarland', 'Sachsen', 
                'Sachsen-Anhalt', 'Schleswig-Holstein', 'Thüringen']
data_germany_foreigners = pc.organize_regional(data_germany_foreigners, drop_values, column_names)

pc.my_summary_stats(data_germany_pop) # no missing values
drop_rows = [1,2,4,5,7,8,10,11,13,14,16,17,19,20,22,23,25,26,28,29,31,32]
drop_values1 = ['Aufteilung', 'Deutschland']
data_germany_pop = pc.organize_CH1(data_germany_pop, drop_rows, drop_values1)

column_names1 = ['Year', 'Schleswig-Holstein', 'Hamburg', 'Niedersachsen', 'Bremen',
                'Nordrhein-Westfalen', 'Hessen', 'Rheinland-Pfalz', 'Saarland',
                'Baden-Württemberg', 'Bayern', 'Mecklenburg-Vorpommern', 'Brandenburg',
                'Berlin', 'Sachsen-Anhalt', 'Thüringen', 'Sachsen']
data_germany_unemployment = pc.organize_unempl(data_germany_unempl, 2, column_names1)
pc.my_summary_stats(data_germany_unemployment) # no missing values
data_germany_unempl_rate = pc.organize_unempl(data_germany_unempl, 3, column_names1)
pc.my_summary_stats(data_germany_unempl_rate) # no missing values

# Thüringen
Values1 = {1: Empl_Thüringen[5], 2: Empl_Thüringen[7], 3: Empl_Thüringen[9], 4: Empl_Thüringen[11], 5: Empl_Thüringen[13], 6: Empl_Thüringen[15], 7: Empl_Thüringen[17], 8: Empl_Thüringen[19]}
drop_values2 = [2,3,6,7,8,9]
column_names_1 = ['Year', 'Total Empl', 'German', 'Foreigners']
Values2 = {1: Empl_Thüringen[6], 2: Empl_Thüringen[8], 3: Empl_Thüringen[10], 4: Empl_Thüringen[12], 5: Empl_Thüringen[14], 6: Empl_Thüringen[16], 7: Empl_Thüringen[18], 8: Empl_Thüringen[20]}
drop_values3 = [1]
column_names_3 = ['Year', 'Helper', 'Skilled worker', 'Specialist', 'Expert', 'without educ', 'with educ', 'with academic educ', 'educ unknown']

Thüringen20 = {}
pc.organize_Bundesländer(Thüringen20, Values1, drop_values2, column_names_1)

Thüringen20_1 = {}
pc.organize_Bundesländer(Thüringen20_1, Values2, drop_values3, column_names_3)

# Schleswig-Holstein
Values3 = {1: Empl_Schleswig_Holstein[5]}