
"""

## SOFTWARE ENGINEERING ##
      ### GROUP 3 ###
      
# data preparation regional data #

Berenice Flumenbaum & Fabienne Belet


"""

# import modules
import sys
import pandas as pd

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
Empl_Baden_Württemberg = pd.read_excel(xls16, sheet_name = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
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
data_germany_pop.columns = ['Year', 'Schleswig-Holstein', 'Hamburg', 'Niedersachsen', 'Bremen', 
                            'Nordrhein-Westfalen', 'Hessen', 'Rheinland-Pfalz','Baden-Württemberg', 'Bayern',
                            'Saarland', 'Berlin', 'Brandenburg', 'Mecklenburg-Vorpommern', 'Sachsen',
                            'Sachsen-Anhalt', 'Thüringen']

column_names1 = ['Year', 'Schleswig-Holstein', 'Hamburg', 'Niedersachsen', 'Bremen',
                'Nordrhein-Westfalen', 'Hessen', 'Rheinland-Pfalz', 'Saarland',
                'Baden-Württemberg', 'Bayern', 'Mecklenburg-Vorpommern', 'Brandenburg',
                'Berlin', 'Sachsen-Anhalt', 'Thüringen', 'Sachsen']
data_germany_unemployment = pc.organize_unempl(data_germany_unempl, 2, column_names1)
pc.my_summary_stats(data_germany_unemployment) # no missing values
data_germany_unempl_rate = pc.organize_unempl(data_germany_unempl, 3, column_names1)
pc.my_summary_stats(data_germany_unempl_rate) # no missing values

# Thüringen #
# organizing employment data by looping through dictionary and deleting unnecessary columns/rows
Values1 = {key: Empl_Thüringen[key] for key in [5,7,9,11,13,15,17,19]}
drop_values2 = [2,3,6,7,8,9]
column_names_1 = ['Year', 'Total Empl', 'Empl German', 'Empl Foreigners']
Values2 = {key: Empl_Thüringen[key] for key in [6,8,10,12,14,16,18,20]}
drop_values3 = [1]
column_names_3 = ['Year', 'Helper', 'Skilled worker', 'Specialist', 'Expert', 'without educ', 'with educ', 'with academic educ', 'educ unknown']

Thüringen = {}
pc.organize_Bundesländer(Thüringen, Values1, drop_values2, column_names_1)
Thüringen_1 = {}
pc.organize_Bundesländer(Thüringen_1, Values2, drop_values3, column_names_3)

# creating a table for employment data for Thüringen
Thüringen = pc.create_table(Thüringen)
Thüringen_1 = pc.create_table2(Thüringen_1)
names = ['Year', 'Foreigners']
names2 = ['Year', 'Population']
names3 = ['Year', 'Unemployment']
names4 = ['Year', 'Unemployment Rate']
Thüringen_2 = pc.extract_values('Thüringen', data_germany_foreigners, names)
Thüringen_3 = pc.extract_values('Thüringen', data_germany_pop, names2)
Thüringen_4 = pc.extract_values('Thüringen', data_germany_unemployment, names3)
Thüringen_5 = pc.extract_values('Thüringen', data_germany_unempl_rate, names4)
Thüringen_unempl = pd.merge(Thüringen_4, Thüringen_5, on='Year')

Table_Thüringen = pd.merge(pd.merge(Thüringen_3, Thüringen_2, on='Year'), Thüringen, on='Year')
Table_Thüringen = pd.merge(pd.merge(Table_Thüringen, Thüringen_1), Thüringen_unempl, on='Year' )

# saving the final dataset for further analysis
PATH2 = '/Users/bereniceflumenbaum/Documents/GitHub/Software Engineering/Final Datasets/'
Table_Thüringen.to_csv(PATH2 + 'table_thüringen.csv')


# Schleswig-Holstein #
# organizing employment data by looping through dictionary and deleting unnecessary columns/rows
Values3 = {key: Empl_Schleswig_Holstein[key] for key in [5,7,9,11,13,15,17,19]}
Values4 = {key: Empl_Schleswig_Holstein[key] for key in [6,8,10,12,14,16,18,20]}

Schleswig_Holstein = {}
pc.organize_Bundesländer(Schleswig_Holstein, Values3, drop_values2, column_names_1)

Schleswig_Holstein_1 = {}
pc.organize_Bundesländer(Schleswig_Holstein_1, Values4, drop_values3, column_names_3)

# creating a table for employment data for Schleswig-Holstein
Schleswig_Holstein = pc.create_table(Schleswig_Holstein)
Schleswig_Holstein_1 = pc.create_table2(Schleswig_Holstein_1)
Schleswig_Holstein_2 = pc.extract_values('Schleswig-Holstein', data_germany_foreigners, names)
Schleswig_Holstein_3 = pc.extract_values('Schleswig-Holstein', data_germany_pop, names2)
Schleswig_Holstein_4 = pc.extract_values('Schleswig-Holstein', data_germany_unemployment, names3)
Schleswig_Holstein_5 = pc.extract_values('Schleswig-Holstein', data_germany_unempl_rate, names4)
Schleswig_Holstein_unempl = pd.merge(Schleswig_Holstein_4, Schleswig_Holstein_5)

Table_Schleswig_Holstein = pd.merge(pd.merge(Schleswig_Holstein_3, Schleswig_Holstein_2, on='Year'), Schleswig_Holstein, on='Year')
Table_Schleswig_Holstein = pd.merge(pd.merge(Table_Schleswig_Holstein, Schleswig_Holstein_1, on='Year'), Schleswig_Holstein_unempl, on='Year')

# saving the final dataset for further analysis
Table_Schleswig_Holstein.to_csv(PATH2 + 'table_schleswig_holstein.csv')

# Sachsen-Anhalt #
# organizing employment data by looping through dictionary and deleting unnecessary columns/rows
Values5 = {key: Empl_Sachsen_Anhalt[key] for key in [5,7,9,11,13,15,17,19]}
Values6 = {key: Empl_Sachsen_Anhalt[key] for key in [6,8,10,12,14,16,18,20]}

Sachsen_Anhalt = {}
pc.organize_Bundesländer(Sachsen_Anhalt, Values5, drop_values2, column_names_1)
Sachsen_Anhalt_1 = {}
pc.organize_Bundesländer(Sachsen_Anhalt_1, Values6, drop_values3, column_names_3)

# creating a table for employment data for Sachsen-Anhalt
Sachsen_Anhalt = pc.create_table(Sachsen_Anhalt)
Sachsen_Anhalt_1 = pc.create_table2(Sachsen_Anhalt_1)
Sachsen_Anhalt_2 = pc.extract_values('Sachsen-Anhalt', data_germany_foreigners, names)
Sachsen_Anhalt_3 = pc.extract_values('Sachsen-Anhalt', data_germany_pop, names2)
Sachsen_Anhalt_4 = pc.extract_values('Sachsen-Anhalt', data_germany_unemployment, names3)
Sachsen_Anhalt_5 = pc.extract_values('Sachsen-Anhalt', data_germany_unempl_rate, names4)
Sachsen_Anhalt_unempl = pd.merge(Sachsen_Anhalt_4, Sachsen_Anhalt_5)

Table_Sachsen_Anhalt = pd.merge(pd.merge(Sachsen_Anhalt_3, Sachsen_Anhalt_2, on='Year'), Sachsen_Anhalt, on='Year')
Table_Sachsen_Anhalt = pd.merge(pd.merge(Table_Sachsen_Anhalt, Sachsen_Anhalt_1, on='Year'), Sachsen_Anhalt_unempl, on='Year')

# saving the final dataset for further analysis
Table_Sachsen_Anhalt.to_csv(PATH2 + 'table_sachsen_anhalt.csv')

# Sachsen #
# organizing employment data by looping through dictionary and deleting unnecessary columns/rows
Values7 = {key: Empl_Sachsen[key] for key in [5,7,9,11,13,15,17,19]}
Values8 = {key: Empl_Sachsen[key] for key in [6,8,10,12,14,16,18,20]}

Sachsen = {}
pc.organize_Bundesländer(Sachsen, Values7, drop_values2, column_names_1)
Sachsen_1 = {}
pc.organize_Bundesländer(Sachsen_1, Values8, drop_values3, column_names_3)

# creating a table for employment data for Sachsen
Sachsen = pc.create_table(Sachsen)
Sachsen_1 = pc.create_table2(Sachsen_1)
Sachsen_2 = pc.extract_values('Sachsen', data_germany_foreigners, names)
Sachsen_3 = pc.extract_values('Sachsen', data_germany_pop, names2)
Sachsen_4 = pc.extract_values('Sachsen', data_germany_unemployment, names3)
Sachsen_5 = pc.extract_values('Sachsen', data_germany_unempl_rate, names4)
Sachsen_unempl = pd.merge(Sachsen_4, Sachsen_5)

Table_Sachsen = pd.merge(pd.merge(Sachsen_3, Sachsen_2, on='Year'), Sachsen, on='Year')
Table_Sachsen = pd.merge(pd.merge(Table_Sachsen, Sachsen_1, on='Year'), Sachsen_unempl, on='Year')

# saving the final dataset for further analysis
Table_Sachsen.to_csv(PATH2 + 'table_sachsen.csv')

# Saarland #
# organizing employment data by looping through dictionary and deleting unnecessary columns/rows
Values9 = {key: Empl_Saarland[key] for key in [5,7,9,11,13,15,17,19]}
Values10 = {key: Empl_Saarland[key] for key in [6,8,10,12,14,16,18,20]}

Saarland = {}
pc.organize_Bundesländer(Saarland, Values9, drop_values2, column_names_1)
Saarland_1 = {}
pc.organize_Bundesländer(Saarland_1, Values10, drop_values3, column_names_3)

# creating a table for employment data for Saarland
Saarland = pc.create_table(Saarland)
Saarland_1 = pc.create_table2(Saarland_1)
Saarland_2 = pc.extract_values('Saarland', data_germany_foreigners, names)
Saarland_3 = pc.extract_values('Saarland', data_germany_pop, names2)
Saarland_4 = pc.extract_values('Saarland', data_germany_unemployment, names3)
Saarland_5 = pc.extract_values('Saarland', data_germany_unempl_rate, names4)
Saarland_unempl = pd.merge(Saarland_4, Saarland_5)

Table_Saarland = pd.merge(pd.merge(Saarland_3, Saarland_2, on='Year'), Saarland, on='Year')
Table_Saarland = pd.merge(pd.merge(Table_Saarland, Saarland_1, on='Year'), Saarland_unempl, on='Year')

# saving the final dataset for further analysis
Table_Saarland.to_csv(PATH2 + 'table_saarland.csv')

# Rheinland-Pfalz #
# organizing employment data by looping through dictionary and deleting unnecessary columns/rows
Values11 = {key: Empl_Rheinland_Pfalz[key] for key in [5,7,9,11,13,15,17,19]}
Values12 = {key: Empl_Rheinland_Pfalz[key] for key in [6,8,10,12,14,16,18,20]}

Rheinland_Pfalz = {}
pc.organize_Bundesländer(Rheinland_Pfalz, Values11, drop_values2, column_names_1)

Rheinland_Pfalz_1 = {}
pc.organize_Bundesländer(Rheinland_Pfalz_1, Values12, drop_values3, column_names_3)

# creating a table for employment data for Rheinland-Pfalz
Rheinland_Pfalz = pc.create_table(Rheinland_Pfalz)
Rheinland_Pfalz_1 = pc.create_table2(Rheinland_Pfalz_1)
Rheinland_Pfalz_2 = pc.extract_values('Rheinland-Pfalz', data_germany_foreigners, names)
Rheinland_Pfalz_3 = pc.extract_values('Rheinland-Pfalz', data_germany_pop, names2)
Rheinland_Pfalz_4 = pc.extract_values('Rheinland-Pfalz', data_germany_unemployment, names3)
Rheinland_Pfalz_5 = pc.extract_values('Rheinland-Pfalz', data_germany_unempl_rate, names4)
Rheinland_Pfalz_unempl = pd.merge(Rheinland_Pfalz_4, Rheinland_Pfalz_5)

Table_Rheinland_Pfalz = pd.merge(pd.merge(Rheinland_Pfalz_3, Rheinland_Pfalz_2, on='Year'), Rheinland_Pfalz, on='Year')
Table_Rheinland_Pfalz = pd.merge(pd.merge(Table_Rheinland_Pfalz, Rheinland_Pfalz_1, on='Year'), Rheinland_Pfalz_unempl, on='Year')

# saving the final dataset for further analysis
Table_Rheinland_Pfalz.to_csv(PATH2 + 'table_rheinland_pfalz.csv')

# Nordrhein-Westfalen #
# organizing employment data by looping through dictionary and deleting unnecessary columns/rows
Values13 = {key: Empl_Nordrhein_Westfalen[key] for key in [5,7,9,11,13,15,17,19]}
Values14 = {key: Empl_Nordrhein_Westfalen[key] for key in [6,8,10,12,14,16,18,20]}

Nordrhein_Westfalen = {}
pc.organize_Bundesländer(Nordrhein_Westfalen, Values13, drop_values2, column_names_1)

Nordrhein_Westfalen_1 = {}
pc.organize_Bundesländer(Nordrhein_Westfalen_1, Values14, drop_values3, column_names_3)

# creating a table for employment data for Nordrhein-Westfalen
Nordrhein_Westfalen = pc.create_table(Nordrhein_Westfalen)
Nordrhein_Westfalen_1 = pc.create_table2(Nordrhein_Westfalen_1)
Nordrhein_Westfalen_2 = pc.extract_values('Nordrhein-Westfalen', data_germany_foreigners, names)
Nordrhein_Westfalen_3 = pc.extract_values('Nordrhein-Westfalen', data_germany_pop, names2)
Nordrhein_Westfalen_4 = pc.extract_values('Nordrhein-Westfalen', data_germany_unemployment, names3)
Nordrhein_Westfalen_5 = pc.extract_values('Nordrhein-Westfalen', data_germany_unempl_rate, names4)
Nordrhein_Westfalen_unempl = pd.merge(Nordrhein_Westfalen_4, Nordrhein_Westfalen_5)

Table_Nordrhein_Westfalen = pd.merge(pd.merge(Nordrhein_Westfalen_3, Nordrhein_Westfalen_2, on='Year'), Nordrhein_Westfalen, on='Year')
Table_Nordrhein_Westfalen = pd.merge(pd.merge(Table_Nordrhein_Westfalen, Nordrhein_Westfalen_1, on='Year'), Nordrhein_Westfalen_unempl, on='Year')

# saving the final dataset for further analysis
Table_Nordrhein_Westfalen.to_csv(PATH2 + 'table_NRW.csv')

# Niedersachsen #
# organizing employment data by looping through dictionary and deleting unnecessary columns/rows
Values15 = {key: Empl_Niedersachsen[key] for key in [5,7,9,11,13,15,17,19]}
Values16 = {key: Empl_Niedersachsen[key] for key in [6,8,10,12,14,16,18,20]}

Niedersachsen = {}
pc.organize_Bundesländer(Niedersachsen, Values15, drop_values2, column_names_1)

Niedersachsen_1 = {}
pc.organize_Bundesländer(Niedersachsen_1, Values16, drop_values3, column_names_3)

# creating a table for employment data for Niedersachsen
Niedersachsen = pc.create_table(Niedersachsen)
Niedersachsen_1 = pc.create_table2(Niedersachsen_1)
Niedersachsen_2 = pc.extract_values('Niedersachsen', data_germany_foreigners, names)
Niedersachsen_3 = pc.extract_values('Niedersachsen', data_germany_pop, names2)
Niedersachsen_4 = pc.extract_values('Niedersachsen', data_germany_unemployment, names3)
Niedersachsen_5 = pc.extract_values('Niedersachsen', data_germany_unempl_rate, names4)
Niedersachsen_unempl = pd.merge(Niedersachsen_4, Niedersachsen_5)

Table_Niedersachsen = pd.merge(pd.merge(Niedersachsen_3, Niedersachsen_2, on='Year'), Niedersachsen, on='Year')
Table_Niedersachsen = pd.merge(pd.merge(Table_Niedersachsen, Niedersachsen_1, on='Year'), Niedersachsen_unempl, on='Year')

# saving the final dataset for further analysis
Table_Niedersachsen.to_csv(PATH2 + 'table_niedersachsen.csv')

# Mecklenburg-Vorpommern #
# organizing employment data by looping through dictionary and deleting unnecessary columns/rows
Values17 = {key: Empl_Mecklenburg_Vorpommern[key] for key in [5,7,9,11,13,15,17,19]}
Values18 = {key: Empl_Mecklenburg_Vorpommern[key] for key in [6,8,10,12,14,16,18,20]}

Mecklenburg_Vorpommern = {}
pc.organize_Bundesländer(Mecklenburg_Vorpommern, Values17, drop_values2, column_names_1)
Mecklenburg_Vorpommern_1 = {}
pc.organize_Bundesländer(Mecklenburg_Vorpommern_1, Values18, drop_values3, column_names_3)

# creating a table for employment data for Mecklenburg-Vorpommern
Mecklenburg_Vorpommern = pc.create_table(Mecklenburg_Vorpommern)
Mecklenburg_Vorpommern_1 = pc.create_table2(Mecklenburg_Vorpommern_1)
Mecklenburg_Vorpommern_2 = pc.extract_values('Mecklenburg-Vorpommern', data_germany_foreigners, names)
Mecklenburg_Vorpommern_3 = pc.extract_values('Mecklenburg-Vorpommern', data_germany_pop, names2)
Mecklenburg_Vorpommern_4 = pc.extract_values('Mecklenburg-Vorpommern', data_germany_unemployment, names3)
Mecklenburg_Vorpommern_5 = pc.extract_values('Mecklenburg-Vorpommern', data_germany_unempl_rate, names4)
Mecklenburg_Vorpommern_unempl = pd.merge(Mecklenburg_Vorpommern_4, Mecklenburg_Vorpommern_5)

Table_Mecklenburg_Vorpommern = pd.merge(pd.merge(Mecklenburg_Vorpommern_3, Mecklenburg_Vorpommern_2, on='Year'), Mecklenburg_Vorpommern, on='Year')
Table_Mecklenburg_Vorpommern = pd.merge(pd.merge(Table_Mecklenburg_Vorpommern, Mecklenburg_Vorpommern_1, on='Year'), Mecklenburg_Vorpommern_unempl, on='Year')

# saving the final dataset for further analysis
Table_Mecklenburg_Vorpommern.to_csv(PATH2 + 'table_mecklenburg_vorpommern.csv')

# Hessen #
# organizing employment data by looping through dictionary and deleting unnecessary columns/rows
Values19 = {key: Empl_Hessen[key] for key in [5,7,9,11,13,15,17,19]}
Values20 = {key: Empl_Hessen[key] for key in [6,8,10,12,14,16,18,20]}

Hessen = {}
pc.organize_Bundesländer(Hessen, Values19, drop_values2, column_names_1)
Hessen_1 = {}
pc.organize_Bundesländer(Hessen_1, Values20, drop_values3, column_names_3)

# creating a table for employment data for Hessen
Hessen = pc.create_table(Hessen)
Hessen_1 = pc.create_table2(Hessen_1)
Hessen_2 = pc.extract_values('Hessen', data_germany_foreigners, names)
Hessen_3 = pc.extract_values('Hessen', data_germany_pop, names2)
Hessen_4 = pc.extract_values('Hessen', data_germany_unemployment, names3)
Hessen_5 = pc.extract_values('Hessen', data_germany_unempl_rate, names4)
Hessen_unempl = pd.merge(Hessen_4, Hessen_5)

Table_Hessen = pd.merge(pd.merge(Hessen_3, Hessen_2, on='Year'), Hessen, on='Year')
Table_Hessen = pd.merge(pd.merge(Table_Hessen, Hessen_1, on='Year'), Hessen_unempl, on='Year')

# saving the final dataset for further analysis
Table_Hessen.to_csv(PATH2 + 'table_hessen.csv')

# Hamburg #
# organizing employment data by looping through dictionary and deleting unnecessary columns/rows
Values21 = {key: Empl_Hamburg[key] for key in [5,7,9,11,13,15,17,19]}
Values22 = {key: Empl_Hamburg[key] for key in [6,8,10,12,14,16,18,20]}

Hamburg = {}
pc.organize_Bundesländer(Hamburg, Values21, drop_values2, column_names_1)
Hamburg_1 = {}
pc.organize_Bundesländer(Hamburg_1, Values22, drop_values3, column_names_3)

# creating a table for employment data for Hamburg
Hamburg = pc.create_table(Hamburg)
Hamburg_1 = pc.create_table2(Hamburg_1)
Hamburg_2 = pc.extract_values('Hamburg', data_germany_foreigners, names)
Hamburg_3 = pc.extract_values('Hamburg', data_germany_pop, names2)
Hamburg_4 = pc.extract_values('Hamburg', data_germany_unemployment, names3)
Hamburg_5 = pc.extract_values('Hamburg', data_germany_unempl_rate, names4)
Hamburg_unempl = pd.merge(Hamburg_4, Hamburg_5)

Table_Hamburg = pd.merge(pd.merge(Hamburg_3, Hamburg_2, on='Year'), Hamburg, on='Year')
Table_Hamburg = pd.merge(pd.merge(Table_Hamburg, Hamburg_1, on='Year'), Hamburg_unempl, on='Year')

# saving the final dataset for further analysis
Table_Hamburg.to_csv(PATH2 + 'table_HH.csv')

# Bremen #
# organizing employment data by looping through dictionary and deleting unnecessary columns/rows
Values23 = {key: Empl_Bremen[key] for key in [5,7,9,11,13,15,17,19]}
Values24 = {key: Empl_Bremen[key] for key in [6,8,10,12,14,16,18,20]}

Bremen = {}
pc.organize_Bundesländer(Bremen, Values23, drop_values2, column_names_1)
Bremen_1 = {}
pc.organize_Bundesländer(Bremen_1, Values24, drop_values3, column_names_3)

# creating a table for employment data for Bremen
Bremen = pc.create_table(Bremen)
Bremen_1 = pc.create_table2(Bremen_1)
Bremen_2 = pc.extract_values('Bremen', data_germany_foreigners, names)
Bremen_3 = pc.extract_values('Bremen', data_germany_pop, names2)
Bremen_4 = pc.extract_values('Bremen', data_germany_unemployment, names3)
Bremen_5 = pc.extract_values('Bremen', data_germany_unempl_rate, names4)
Bremen_unempl = pd.merge(Bremen_4, Bremen_5)

Table_Bremen= pd.merge(pd.merge(Bremen_3, Bremen_2, on='Year'), Bremen, on='Year')
Table_Bremen = pd.merge(pd.merge(Table_Bremen, Bremen_1, on='Year'), Bremen_unempl, on='Year')

# saving the final dataset for further analysis
Table_Bremen.to_csv(PATH2 + 'table_bremen.csv')

# Brandenburg #
# organizing employment data by looping through dictionary and deleting unnecessary columns/rows
Values25 = {key: Empl_Brandenburg[key] for key in [5,7,9,11,13,15,17,19]}
Values26 = {key: Empl_Brandenburg[key] for key in [6,8,10,12,14,16,18,20]}

Brandenburg = {}
pc.organize_Bundesländer(Brandenburg, Values25, drop_values2, column_names_1)
Brandenburg_1 = {}
pc.organize_Bundesländer(Brandenburg_1, Values26, drop_values3, column_names_3)

# creating a table for employment data for Brandenburg
Brandenburg = pc.create_table(Brandenburg)
Brandenburg_1 = pc.create_table2(Brandenburg_1)
Brandenburg_2 = pc.extract_values('Brandenburg', data_germany_foreigners, names)
Brandenburg_3 = pc.extract_values('Brandenburg', data_germany_pop, names2)
Brandenburg_4 = pc.extract_values('Brandenburg', data_germany_unemployment, names3)
Brandenburg_5 = pc.extract_values('Brandenburg', data_germany_unempl_rate, names4)
Brandenburg_unempl = pd.merge(Brandenburg_4, Brandenburg_5)

Table_Brandenburg = pd.merge(pd.merge(Brandenburg_3, Brandenburg_2, on='Year'), Brandenburg, on='Year')
Table_Brandenburg = pd.merge(pd.merge(Table_Brandenburg, Brandenburg_1, on='Year'), Brandenburg_unempl, on='Year')

# saving the final dataset for further analysis
Table_Brandenburg.to_csv(PATH2 + 'table_brandenburg.csv')

# Berlin #
# organizing employment data by looping through dictionary and deleting unnecessary columns/rows
Values27 = {key: Empl_Berlin[key] for key in [5,7,9,11,13,15,17,19]}
Values28 = {key: Empl_Berlin[key] for key in [6,8,10,12,14,16,18,20]}

Berlin = {}
pc.organize_Bundesländer(Berlin, Values27, drop_values2, column_names_1)
Berlin_1 = {}
pc.organize_Bundesländer(Berlin_1, Values28, drop_values3, column_names_3)

# creating a table for employment data for Berlin
Berlin = pc.create_table(Berlin)
Berlin_1 = pc.create_table2(Berlin_1)
Berlin_2 = pc.extract_values('Berlin', data_germany_foreigners, names)
Berlin_3 = pc.extract_values('Berlin', data_germany_pop, names2)
Berlin_4 = pc.extract_values('Berlin', data_germany_unemployment, names3)
Berlin_5 = pc.extract_values('Berlin', data_germany_unempl_rate, names4)
Berlin_unempl = pd.merge(Berlin_4, Berlin_5)

Table_Berlin = pd.merge(pd.merge(Berlin_3, Berlin_2, on='Year'), Berlin, on='Year')
Table_Berlin = pd.merge(pd.merge(Table_Berlin, Berlin_1, on='Year'), Berlin_unempl, on='Year')

# saving the final dataset for further analysis
Table_Berlin.to_csv(PATH2 + 'table_berlin.csv')

# Bayern #
# organizing employment data by looping through dictionary and deleting unnecessary columns/rows
Values29 = {key: Empl_Bayern[key] for key in [5,7,9,11,13,15,17,19]}
Values30 = {key: Empl_Bayern[key] for key in [6,8,10,12,14,16,18,20]}

Bayern = {}
pc.organize_Bundesländer(Bayern, Values29, drop_values2, column_names_1)
Bayern_1 = {}
pc.organize_Bundesländer(Bayern_1, Values30, drop_values3, column_names_3)

# creating a table for employment data for Bayern
Bayern = pc.create_table(Bayern)
Bayern_1 = pc.create_table2(Bayern_1)
Bayern_2 = pc.extract_values('Bayern', data_germany_foreigners, names)
Bayern_3 = pc.extract_values('Bayern', data_germany_pop, names2)
Bayern_4 = pc.extract_values('Bayern', data_germany_unemployment, names3)
Bayern_5 = pc.extract_values('Bayern', data_germany_unempl_rate, names4)
Bayern_unempl = pd.merge(Bayern_4, Bayern_5)

Table_Bayern = pd.merge(pd.merge(Bayern_3, Bayern_2, on='Year'), Bayern, on='Year')
Table_Bayern = pd.merge(pd.merge(Table_Bayern, Bayern_1, on='Year'), Bayern_unempl, on='Year')

# saving the final dataset for further analysis
Table_Bayern.to_csv(PATH2 + 'table_bayern.csv')

# Baden-Württemberg #
# organizing employment data by looping through dictionary and deleting unnecessary columns/rows
Values31 = {key: Empl_Baden_Württemberg[key] for key in [3,5,7,9,11,13,15,17]}
Values32 = {key: Empl_Baden_Württemberg[key] for key in [4,6,8,10,12,14,16,18]}

Baden_Württemberg = {}
pc.organize_Bundesländer(Baden_Württemberg, Values31, drop_values2, column_names_1)
Baden_Württemberg_1 = {}
pc.organize_Bundesländer(Baden_Württemberg_1, Values32, drop_values3, column_names_3)

# creating a table for employment data for Baden-Würrtemberg
Baden_Württemberg = pd.concat([Baden_Württemberg[3], Baden_Württemberg[5], Baden_Württemberg[7], Baden_Württemberg[9], Baden_Württemberg[11], Baden_Württemberg[13], Baden_Württemberg[15], Baden_Württemberg[17]])
Baden_Württemberg_1 = pd.concat([Baden_Württemberg_1[4], Baden_Württemberg_1[6], Baden_Württemberg_1[8], Baden_Württemberg_1[10], Baden_Württemberg_1[12], Baden_Württemberg_1[14], Baden_Württemberg_1[16], Baden_Württemberg_1[18]])
Baden_Württemberg_2 = pc.extract_values('Baden-Württemberg', data_germany_foreigners, names)
Baden_Württemberg_3 = pc.extract_values('Baden-Württemberg', data_germany_pop, names2)
Baden_Württemberg_4 = pc.extract_values('Baden-Württemberg', data_germany_unemployment, names3)
Baden_Württemberg_5 = pc.extract_values('Baden-Württemberg', data_germany_unempl_rate, names4)
Baden_Württemberg_unempl = pd.merge(Baden_Württemberg_4, Baden_Württemberg_5)

Table_Baden_Württemberg = pd.merge(pd.merge(Baden_Württemberg_3, Baden_Württemberg_2, on='Year'), Baden_Württemberg, on='Year')
Table_Baden_Württemberg = pd.merge(pd.merge(Table_Baden_Württemberg, Baden_Württemberg_1, on='Year'), Baden_Württemberg_unempl, on='Year')

# saving the final dataset for further analysis
Table_Baden_Württemberg.to_csv(PATH2 + 'table_BaWü.csv')

##############################################################################

# Regional data for Switzerland #
# define data names
dataname1 = 'Bevölkerungsentwicklung_Schweiz_2000-2020.xlsx'
dataname2 = 'Asylstatistik_Schweiz_201012.xlsx'
dataname3 = 'Asylstatistik_Schweiz_201112.xlsx'
dataname4 = 'Asylstatistik_Schweiz_201212.xlsx'
dataname5 = 'Asylstatistik_Schweiz_201312.xlsx'
dataname6 = 'Asylstatistik_Schweiz_201412.xlsx'
dataname7 = 'Asylstatistik_Schweiz_201512.xlsx'
dataname8 = 'Asylstatistik_Schweiz_201612.xlsx'
dataname9 = 'Asylstatistik_Schweiz_201712.xlsx'
dataname10 = 'Asylstatistik_Schweiz_201812.xlsx'
dataname11 = 'Asylstatistik_Schweiz_201912.xlsx'
dataname12 = 'Asylstatistik_Schweiz_202012.xlsx'
dataname13 = 'Arbeitslosenquote_Schweiz.xlsx'
dataname14 = 'Arbeitslose_Schweiz.xlsx'

# load in data using pandas
data_swiss_pop = pd.ExcelFile(PATH + dataname1)
data_swiss_pop = pd.read_excel(data_swiss_pop, sheet_name=['Overview_regional'], header=None)
data_swiss_pop = data_swiss_pop['Overview_regional']

data_swiss_unempl = pd.ExcelFile(PATH + dataname14)
data_swiss_unempl = pd.read_excel(data_swiss_unempl, sheet_name=['Overview_regional'], header=None)
data_swiss_unempl = data_swiss_unempl['Overview_regional']

data_swiss_unempl_rate = pd.ExcelFile(PATH + dataname13)
data_swiss_unempl_rate = pd.read_excel(data_swiss_unempl_rate, sheet_name=['Overview_regional'], header=None)
data_swiss_unempl_rate = data_swiss_unempl_rate['Overview_regional']

XLS10 = pd.ExcelFile(PATH + dataname2)
data_asyl_10 = pd.read_excel(XLS10, sheet_name=['CH-Kt'], header=None) 
data_asyl_10 = data_asyl_10['CH-Kt']

XLS11 = pd.ExcelFile(PATH + dataname3)
data_asyl_11 = pd.read_excel(XLS11, sheet_name=['CH-Kt'], header=None)
data_asyl_11 = data_asyl_11['CH-Kt']

XLS12 = pd.ExcelFile(PATH + dataname4)
data_asyl_12 = pd.read_excel(XLS12, sheet_name=['CH-Kt'], header=None)
data_asyl_12 = data_asyl_12['CH-Kt']

XLS13 = pd.ExcelFile(PATH + dataname5)
data_asyl_13 = pd.read_excel(XLS13, sheet_name=['CH-Kt'], header=None)
data_asyl_13 = data_asyl_13['CH-Kt']

XLS14 = pd.ExcelFile(PATH + dataname6)
data_asyl_14 = pd.read_excel(XLS14, sheet_name=['CH-Kt'], header=None)
data_asyl_14 = data_asyl_14['CH-Kt']

XLS15 = pd.ExcelFile(PATH + dataname7)
data_asyl_15 = pd.read_excel(XLS15, sheet_name=['CH-Kt'], header=None)
data_asyl_15 = data_asyl_15['CH-Kt']

XLS16 = pd.ExcelFile(PATH + dataname8)
data_asyl_16 = pd.read_excel(XLS16, sheet_name=['CH-Kt'], header=None)
data_asyl_16 = data_asyl_16['CH-Kt']

XLS17 = pd.ExcelFile(PATH + dataname9)
data_asyl_17 = pd.read_excel(XLS17, sheet_name=['CH-Kt'], header=None)
data_asyl_17 = data_asyl_17['CH-Kt']

XLS18 = pd.ExcelFile(PATH + dataname10)
data_asyl_18 = pd.read_excel(XLS18, sheet_name=['CH-Kt'], header=None)
data_asyl_18 = data_asyl_18['CH-Kt']

XLS19 = pd.ExcelFile(PATH + dataname11)
data_asyl_19 = pd.read_excel(XLS19, sheet_name=['CH-Kt'], header=None)
data_asyl_19 = data_asyl_19['CH-Kt']

XLS20 = pd.ExcelFile(PATH + dataname12)
data_asyl_20 = pd.read_excel(XLS20, sheet_name=['CH-Kt'], header=None)
data_asyl_20 = data_asyl_20['CH-Kt']

# check for missing values and deal with them
pc.my_summary_stats(data_swiss_pop) # no missing values and nan values found
pc.my_summary_stats(data_swiss_unempl) # no missing values
pc.my_summary_stats(data_swiss_unempl_rate) # no missing values

drop_rows = [0,1,2,3,4,5,6]
drop_values = [3,4,6,7,9,10,12,13,15,16]
column_names = ['Canton', 'Year', 'Refugees Total', 'Residents Permit B Total', 
                    'Residents Permit B employed', 'Residents Permit B unempl', 
                    'Settled Total']
data_asyl_10 = pc.organize_CH_asyl(data_asyl_10, drop_rows, drop_values, column_names)
drop_rows1 = [0,1,2,3,4]
data_asyl_11 = pc.organize_CH_asyl(data_asyl_11, drop_rows1, drop_values, column_names)
data_asyl_12 = pc.organize_CH_asyl(data_asyl_12, drop_rows, drop_values, column_names)
data_asyl_13 = pc.organize_CH_asyl(data_asyl_13, drop_rows, drop_values, column_names)
data_asyl_14 = pc.organize_CH_asyl(data_asyl_14, drop_rows, drop_values, column_names)
data_asyl_15 = pc.organize_CH_asyl(data_asyl_15, drop_rows, drop_values, column_names)
data_asyl_16 = pc.organize_CH_asyl(data_asyl_16, drop_rows, drop_values, column_names)
data_asyl_17 = pc.organize_CH_asyl(data_asyl_17, drop_rows, drop_values, column_names)
data_asyl_18 = pc.organize_CH_asyl(data_asyl_18, drop_rows, drop_values, column_names)
data_asyl_19 = pc.organize_CH_asyl(data_asyl_19, drop_rows, drop_values, column_names)
drop_rows2 = [0,1,2,3,4,5]
data_asyl_20 = pc.organize_CH_asyl(data_asyl_20, drop_rows2, drop_values, column_names)

# Aargau #
Aargau_empl = data_swiss_pop[[0,31,32,33]]
Aargau_empl = Aargau_empl.drop([0,1])
Empl = ['Year', 'Employment', 'Emplyoment Swiss', 'Employment Foreigners']
Aargau_empl.columns = Empl

Aargau_unempl = data_swiss_unempl[[0,11]]
Aargau_unempl = Aargau_unempl.drop(0)
Unempl = ['Year', 'Unemployment']
Aargau_unempl.columns = Unempl
Aargau_unempl_rate = data_swiss_unempl_rate[[0,11]]
Aargau_unempl_rate = Aargau_unempl_rate.drop(0)
Unempl_rate = ['Year', 'Unemployment Rate']
Aargau_unempl_rate.columns = Unempl_rate

table_Aargau_asyl = pd.concat([data_asyl_10.iloc[[0]], data_asyl_11.iloc[[0]], 
                               data_asyl_12.iloc[[0]], data_asyl_13.iloc[[0]],
                               data_asyl_14.iloc[[0]], data_asyl_15.iloc[[0]],
                               data_asyl_16.iloc[[0]], data_asyl_17.iloc[[0]],
                               data_asyl_18.iloc[[0]], data_asyl_19.iloc[[0]],
                               data_asyl_20.iloc[[0]]])
table_Aargau_asyl = table_Aargau_asyl.drop('Canton', axis=1)

table_Aargau = pd.merge(pd.merge(Aargau_empl, Aargau_unempl, on='Year'), Aargau_unempl_rate, on='Year')
table_Aargau = pd.merge(table_Aargau, table_Aargau_asyl, on='Year')

# Appenzell A. Rh. #
AppenzellA_empl = data_swiss_pop[[0, 43, 44, 45]]
AppenzellA_empl = AppenzellA_empl.drop([0,1])
AppenzellA_empl.columns = Empl

AppenzellA_unempl = data_swiss_unempl[[0,15]]
AppenzellA_unempl = AppenzellA_unempl.drop(0)
AppenzellA_unempl.columns = Unempl

AppenzellA_unempl_rate = data_swiss_unempl[[0,15]]
AppenzellA_unempl_rate = AppenzellA_unempl_rate.drop(0)
AppenzellA_unempl_rate.columns = Unempl_rate

table_AppenzellA_asyl = pd.concat([data_asyl_10.iloc[[1]], data_asyl_11.iloc[[1]], 
                               data_asyl_12.iloc[[1]], data_asyl_13.iloc[[1]],
                               data_asyl_14.iloc[[1]], data_asyl_15.iloc[[1]],
                               data_asyl_16.iloc[[1]], data_asyl_17.iloc[[1]],
                               data_asyl_18.iloc[[1]], data_asyl_19.iloc[[1]],
                               data_asyl_20.iloc[[1]]])
table_AppenzellA_asyl = table_AppenzellA_asyl.drop('Canton', axis=1)

table_AppenzellA = pd.merge(pd.merge(AppenzellA_empl, AppenzellA_unempl, on='Year'), AppenzellA_unempl_rate, on='Year')
table_AppenzellA = pd.merge(table_AppenzellA, table_AppenzellA_asyl, on='Year')

# Appenzell I. Rh. #
AppenzellI_empl = data_swiss_pop[[0,46,47,48]]
AppenzellI_empl = AppenzellI_empl.drop([0,1])
AppenzellI_empl.columns = Empl

AppenzellI_unempl = data_swiss_unempl[[0,16]]
AppenzellI_unempl = AppenzellI_unempl.drop(0)
AppenzellI_unempl.columns = Unempl

AppenzellI_unempl_rate = data_swiss_unempl[[0,16]]
AppenzellI_unempl_rate = AppenzellI_unempl_rate.drop(0)
AppenzellI_unempl_rate.columns = Unempl_rate

table_AppenzellI_asyl = pd.concat([data_asyl_10.iloc[[2]], data_asyl_11.iloc[[2]], 
                               data_asyl_12.iloc[[2]], data_asyl_13.iloc[[2]],
                               data_asyl_14.iloc[[2]], data_asyl_15.iloc[[2]],
                               data_asyl_16.iloc[[2]], data_asyl_17.iloc[[2]],
                               data_asyl_18.iloc[[2]], data_asyl_19.iloc[[2]],
                               data_asyl_20.iloc[[2]]])
table_AppenzellI_asyl = table_AppenzellI_asyl.drop('Canton', axis=1)

table_AppenzellI = pd.merge(pd.merge(AppenzellI_empl, AppenzellI_unempl, on='Year'), AppenzellI_unempl_rate, on='Year')
table_AppenzellI = pd.merge(table_AppenzellI, table_AppenzellI_asyl, on='Year')

# Basel-Land #
Basel_Land_empl = data_swiss_pop[[0,28,29,30]]
Basel_Land_empl = Basel_Land_empl.drop([0,1])
Basel_Land_empl.columns = Empl

Basel_Land_unempl = data_swiss_unempl[[0,10]]
Basel_Land_unempl = Basel_Land_unempl.drop(0)
Basel_Land_unempl.columns = Unempl

Basel_Land_unempl_rate = data_swiss_unempl[[0,10]]
Basel_Land_unempl_rate = Basel_Land_unempl_rate.drop(0)
Basel_Land_unempl_rate.columns = Unempl_rate

table_Basel_Land_asyl = pd.concat([data_asyl_10.iloc[[3]], data_asyl_11.iloc[[3]], 
                               data_asyl_12.iloc[[3]], data_asyl_13.iloc[[3]],
                               data_asyl_14.iloc[[3]], data_asyl_15.iloc[[3]],
                               data_asyl_16.iloc[[3]], data_asyl_17.iloc[[3]],
                               data_asyl_18.iloc[[3]], data_asyl_19.iloc[[3]],
                               data_asyl_20.iloc[[3]]])
table_Basel_Land_asyl = table_Basel_Land_asyl.drop('Canton', axis=1)

table_Basel_Land = pd.merge(pd.merge(Basel_Land_empl, Basel_Land_unempl, on='Year'), Basel_Land_unempl_rate, on='Year')
table_Basel_Land = pd.merge(table_Basel_Land, table_Basel_Land_asyl, on='Year')

# Basel-Stadt #
Basel_Stadt_empl = data_swiss_pop[[0,25,26,37]]
Basel_Stadt_empl = Basel_Stadt_empl.drop([0,1])
Basel_Stadt_empl.columns = Empl

Basel_Stadt_unempl = data_swiss_unempl[[0,9]]
Basel_Stadt_unempl = Basel_Stadt_unempl.drop(0)
Basel_Stadt_unempl.columns = Unempl

Basel_Stadt_unempl_rate = data_swiss_unempl[[0,9]]
Basel_Stadt_unempl_rate = Basel_Stadt_unempl_rate.drop(0)
Basel_Stadt_unempl_rate.columns = Unempl_rate

table_Basel_Stadt_asyl = pd.concat([data_asyl_10.iloc[[4]], data_asyl_11.iloc[[4]],
                               data_asyl_12.iloc[[4]], data_asyl_13.iloc[[4]],
                               data_asyl_14.iloc[[4]], data_asyl_15.iloc[[4]],
                               data_asyl_16.iloc[[4]], data_asyl_17.iloc[[4]],
                               data_asyl_18.iloc[[4]], data_asyl_19.iloc[[4]],
                               data_asyl_20.iloc[[4]]])
table_Basel_Stadt_asyl = table_Basel_Stadt_asyl.drop('Canton', axis=1)

table_Basel_Stadt = pd.merge(pd.merge(Basel_Stadt_empl, Basel_Stadt_unempl, on='Year'), Basel_Stadt_unempl_rate, on='Year')
table_Basel_Stadt = pd.merge(table_Basel_Stadt, table_Basel_Stadt_asyl, on='Year')

# Bern #
Bern_empl = data_swiss_pop[[0,10,11,12]]
Bern_empl = Bern_empl.drop([0,1])
Bern_empl.columns = Empl

Bern_unempl = data_swiss_unempl[[0,4]]
Bern_unempl = Bern_unempl.drop(0)
Bern_unempl.columns = Unempl

Bern_unempl_rate = data_swiss_unempl[[0,4]]
Bern_unempl_rate = Bern_unempl_rate.drop(0)
Bern_unempl_rate.columns = Unempl_rate

table_Bern_asyl = pd.concat([data_asyl_10.iloc[[5]], data_asyl_11.iloc[[5]], 
                               data_asyl_12.iloc[[5]], data_asyl_13.iloc[[5]],
                               data_asyl_14.iloc[[5]], data_asyl_15.iloc[[5]],
                               data_asyl_16.iloc[[5]], data_asyl_17.iloc[[5]],
                               data_asyl_18.iloc[[5]], data_asyl_19.iloc[[5]],
                               data_asyl_20.iloc[[5]]])
table_Bern_asyl = table_Bern_asyl.drop('Canton', axis=1)

table_Bern = pd.merge(pd.merge(Bern_empl, Bern_unempl, on='Year'), Bern_unempl_rate, on='Year')
table_Bern = pd.merge(table_Bern, table_Bern_asyl, on='Year')

# Freiburg #
Freiburg_empl = data_swiss_pop[[0,13,14,15]]
Freiburg_empl = Freiburg_empl.drop([0,1])
Freiburg_empl.columns = Empl

Freiburg_unempl = data_swiss_unempl[[0,5]]
Freiburg_unempl = Freiburg_unempl.drop(0)
Freiburg_unempl.columns = Unempl

Freiburg_unempl_rate = data_swiss_unempl[[0,5]]
Freiburg_unempl_rate = Freiburg_unempl_rate.drop(0)
Freiburg_unempl_rate.columns = Unempl_rate

table_Freiburg_asyl = pd.concat([data_asyl_10.iloc[[6]], data_asyl_11.iloc[[6]], 
                               data_asyl_12.iloc[[6]], data_asyl_13.iloc[[6]],
                               data_asyl_14.iloc[[6]], data_asyl_15.iloc[[6]],
                               data_asyl_16.iloc[[6]], data_asyl_17.iloc[[6]],
                               data_asyl_18.iloc[[6]], data_asyl_19.iloc[[6]],
                               data_asyl_20.iloc[[6]]])
table_Freiburg_asyl = table_Freiburg_asyl.drop('Canton', axis=1)

table_Freiburg = pd.merge(pd.merge(Freiburg_empl, Freiburg_unempl, on='Year'), Freiburg_unempl_rate, on='Year')
table_Freiburg = pd.merge(table_Freiburg, table_Freiburg_asyl, on='Year')

# Genf #
Genf_empl = data_swiss_pop[[0,7,8,9]]
Genf_empl = Genf_empl.drop([0,1])
Genf_empl.columns = Empl

Genf_unempl = data_swiss_unempl[[0,3]]
Genf_unempl = Genf_unempl.drop(0)
Genf_unempl.columns = Unempl

Genf_unempl_rate = data_swiss_unempl[[0,3]]
Genf_unempl_rate = Genf_unempl_rate.drop(0)
Genf_unempl_rate.columns = Unempl_rate

table_Genf_asyl = pd.concat([data_asyl_10.iloc[[7]], data_asyl_11.iloc[[7]], 
                               data_asyl_12.iloc[[7]], data_asyl_13.iloc[[7]],
                               data_asyl_14.iloc[[7]], data_asyl_15.iloc[[7]],
                               data_asyl_16.iloc[[7]], data_asyl_17.iloc[[7]],
                               data_asyl_18.iloc[[7]], data_asyl_19.iloc[[7]],
                               data_asyl_20.iloc[[7]]])
table_Genf_asyl = table_Genf_asyl.drop('Canton', axis=1)

table_Genf = pd.merge(pd.merge(Genf_empl, Genf_unempl, on='Year'), Genf_unempl_rate, on='Year')
table_Genf = pd.merge(table_Genf, table_Genf_asyl, on='Year')

# Glarus #
Glarus_empl = data_swiss_pop[[0,37,38,39]]
Glarus_empl = Glarus_empl.drop([0,1])
Glarus_empl.columns = Empl

Glarus_unempl = data_swiss_unempl[[0,13]]
Glarus_unempl = Glarus_unempl.drop(0)
Glarus_unempl.columns = Unempl

Glarus_unempl_rate = data_swiss_unempl[[0,13]]
Glarus_unempl_rate = Glarus_unempl_rate.drop(0)
Glarus_unempl_rate.columns = Unempl_rate

table_Glarus_asyl = pd.concat([data_asyl_10.iloc[[8]], data_asyl_11.iloc[[8]], 
                               data_asyl_12.iloc[[8]], data_asyl_13.iloc[[8]],
                               data_asyl_14.iloc[[8]], data_asyl_15.iloc[[8]],
                               data_asyl_16.iloc[[8]], data_asyl_17.iloc[[8]],
                               data_asyl_18.iloc[[8]], data_asyl_19.iloc[[8]],
                               data_asyl_20.iloc[[8]]])
table_Glarus_asyl = table_Glarus_asyl.drop('Canton', axis=1)

table_Glarus = pd.merge(pd.merge(Glarus_empl, Glarus_unempl, on='Year'), Glarus_unempl_rate, on='Year')
table_Glarus = pd.merge(table_Glarus, table_Glarus_asyl, on='Year')

# Graubünden #
Graubünden_empl = data_swiss_pop[[0,52,53,54]]
Graubünden_empl = Graubünden_empl.drop([0,1])
Graubünden_empl.columns = Empl

Graubünden_unempl = data_swiss_unempl[[0,18]]
Graubünden_unempl = Graubünden_unempl.drop(0)
Graubünden_unempl.columns = Unempl

Graubünden_unempl_rate = data_swiss_unempl[[0,18]]
Graubünden_unempl_rate = Graubünden_unempl_rate.drop(0)
Graubünden_unempl_rate.columns = Unempl_rate

table_Graubünden_asyl = pd.concat([data_asyl_10.iloc[[9]], data_asyl_11.iloc[[9]], 
                               data_asyl_12.iloc[[9]], data_asyl_13.iloc[[9]],
                               data_asyl_14.iloc[[9]], data_asyl_15.iloc[[9]],
                               data_asyl_16.iloc[[9]], data_asyl_17.iloc[[9]],
                               data_asyl_18.iloc[[9]], data_asyl_19.iloc[[9]],
                               data_asyl_20.iloc[[9]]])
table_Graubünden_asyl = table_Graubünden_asyl.drop('Canton', axis=1)

table_Graubünden = pd.merge(pd.merge(Graubünden_empl, Graubünden_unempl, on='Year'), Graubünden_unempl_rate, on='Year')
table_Graubünden = pd.merge(table_Graubünden, table_Graubünden_asyl, on='Year')

# Jura #
Jura_empl = data_swiss_pop[[0,22,23,24]]
Jura_empl = Jura_empl.drop([0,1])
Jura_empl.columns = Empl

Jura_unempl = data_swiss_unempl[[0,8]]
Jura_unempl = Jura_unempl.drop(0)
Jura_unempl.columns = Unempl

Jura_unempl_rate = data_swiss_unempl[[0,8]]
Jura_unempl_rate = Jura_unempl_rate.drop(0)
Jura_unempl_rate.columns = Unempl_rate

table_Jura_asyl = pd.concat([data_asyl_10.iloc[[10]], data_asyl_11.iloc[[10]], 
                               data_asyl_12.iloc[[10]], data_asyl_13.iloc[[10]],
                               data_asyl_14.iloc[[10]], data_asyl_15.iloc[[10]],
                               data_asyl_16.iloc[[10]], data_asyl_17.iloc[[10]],
                               data_asyl_18.iloc[[10]], data_asyl_19.iloc[[10]],
                               data_asyl_20.iloc[[10]]])
table_Jura_asyl = table_Jura_asyl.drop('Canton', axis=1)

table_Jura = pd.merge(pd.merge(Jura_empl, Jura_unempl, on='Year'), Jura_unempl_rate, on='Year')
table_Jura = pd.merge(table_Jura, table_Jura_asyl, on='Year')

# Luzern #
Luzern_empl = data_swiss_pop[[0,58,59,60]]
Luzern_empl = Luzern_empl.drop([0,1])
Luzern_empl.columns = Empl

Luzern_unempl = data_swiss_unempl[[0,20]]
Luzern_unempl = Luzern_unempl.drop(0)
Luzern_unempl.columns = Unempl

Luzern_unempl_rate = data_swiss_unempl[[0,20]]
Luzern_unempl_rate = Luzern_unempl_rate.drop(0)
Luzern_unempl_rate.columns = Unempl_rate

table_Luzern_asyl = pd.concat([data_asyl_10.iloc[[11]], data_asyl_11.iloc[[11]], 
                               data_asyl_12.iloc[[11]], data_asyl_13.iloc[[11]],
                               data_asyl_14.iloc[[11]], data_asyl_15.iloc[[11]],
                               data_asyl_16.iloc[[11]], data_asyl_17.iloc[[11]],
                               data_asyl_18.iloc[[11]], data_asyl_19.iloc[[11]],
                               data_asyl_20.iloc[[11]]])
table_Luzern_asyl = table_Luzern_asyl.drop('Canton', axis=1)

table_Luzern = pd.merge(pd.merge(Luzern_empl, Luzern_unempl, on='Year'), Luzern_unempl_rate, on='Year')
table_Luzern = pd.merge(table_Luzern, table_Luzern_asyl, on='Year')

# Neuenburg #
Neuenburg_empl = data_swiss_pop[[0,19,20,21]]
Neuenburg_empl = Neuenburg_empl.drop([0,1])
Neuenburg_empl.columns = Empl

Neuenburg_unempl = data_swiss_unempl[[0,7]]
Neuenburg_unempl = Neuenburg_unempl.drop(0)
Neuenburg_unempl.columns = Unempl

Neuenburg_unempl_rate = data_swiss_unempl[[0,7]]
Neuenburg_unempl_rate = Neuenburg_unempl_rate.drop(0)
Neuenburg_unempl_rate.columns = Unempl_rate

table_Neuenburg_asyl = pd.concat([data_asyl_10.iloc[[12]], data_asyl_11.iloc[[12]], 
                               data_asyl_12.iloc[[12]], data_asyl_13.iloc[[12]],
                               data_asyl_14.iloc[[12]], data_asyl_15.iloc[[12]],
                               data_asyl_16.iloc[[12]], data_asyl_17.iloc[[12]],
                               data_asyl_18.iloc[[12]], data_asyl_19.iloc[[12]],
                               data_asyl_20.iloc[[12]]])
table_Neuenburg_asyl = table_Neuenburg_asyl.drop('Canton', axis=1)

table_Neuenburg = pd.merge(pd.merge(Neuenburg_empl, Neuenburg_unempl, on='Year'), Neuenburg_unempl_rate, on='Year')
table_Neuenburg = pd.merge(table_Neuenburg, table_Neuenburg_asyl, on='Year')

# Nidwalden #
Nidwalden_empl = data_swiss_pop[[0,70,71,72]]
Nidwalden_empl = Nidwalden_empl.drop([0,1])
Nidwalden_empl.columns = Empl

Nidwalden_unempl = data_swiss_unempl[[0,24]]
Nidwalden_unempl = Nidwalden_unempl.drop(0)
Nidwalden_unempl.columns = Unempl

Nidwalden_unempl_rate = data_swiss_unempl[[0,24]]
Nidwalden_unempl_rate = Nidwalden_unempl_rate.drop(0)
Nidwalden_unempl_rate.columns = Unempl_rate

table_Nidwalden_asyl = pd.concat([data_asyl_10.iloc[[13]], data_asyl_11.iloc[[13]], 
                               data_asyl_12.iloc[[13]], data_asyl_13.iloc[[13]],
                               data_asyl_14.iloc[[13]], data_asyl_15.iloc[[13]],
                               data_asyl_16.iloc[[13]], data_asyl_17.iloc[[13]],
                               data_asyl_18.iloc[[13]], data_asyl_19.iloc[[13]],
                               data_asyl_20.iloc[[13]]])
table_Nidwalden_asyl = table_Nidwalden_asyl.drop('Canton', axis=1)

table_Nidwalden = pd.merge(pd.merge(Nidwalden_empl, Nidwalden_unempl, on='Year'), Nidwalden_unempl_rate, on='Year')
table_Nidwalden = pd.merge(table_Nidwalden, table_Nidwalden_asyl, on='Year')

# Obwalden #
Obwalden_empl = data_swiss_pop[[0,67,68,69]]
Obwalden_empl = Obwalden_empl.drop([0,1])
Obwalden_empl.columns = Empl

Obwalden_unempl = data_swiss_unempl[[0,23]]
Obwalden_unempl = Obwalden_unempl.drop(0)
Obwalden_unempl.columns = Unempl

Obwalden_unempl_rate = data_swiss_unempl[[0,23]]
Obwalden_unempl_rate = Obwalden_unempl_rate.drop(0)
Obwalden_unempl_rate.columns = Unempl_rate

table_Obwalden_asyl = pd.concat([data_asyl_10.iloc[[14]], data_asyl_11.iloc[[14]], 
                               data_asyl_12.iloc[[14]], data_asyl_13.iloc[[14]],
                               data_asyl_14.iloc[[14]], data_asyl_15.iloc[[14]],
                               data_asyl_16.iloc[[14]], data_asyl_17.iloc[[14]],
                               data_asyl_18.iloc[[14]], data_asyl_19.iloc[[14]],
                               data_asyl_20.iloc[[14]]])
table_Obwalden_asyl = table_Obwalden_asyl.drop('Canton', axis=1)

table_Obwalden = pd.merge(pd.merge(Obwalden_empl, Obwalden_unempl, on='Year'), Obwalden_unempl_rate, on='Year')
table_Obwalden = pd.merge(table_Obwalden, table_Obwalden_asyl, on='Year')

# Schaffhausen #
Schaffhausen_empl = data_swiss_pop[[0,40,41,42]]
Schaffhausen_empl = Schaffhausen_empl.drop([0,1])
Schaffhausen_empl.columns = Empl

Schaffhausen_unempl = data_swiss_unempl[[0,14]]
Schaffhausen_unempl = Schaffhausen_unempl.drop(0)
Schaffhausen_unempl.columns = Unempl

Schaffhausen_unempl_rate = data_swiss_unempl[[0,14]]
Schaffhausen_unempl_rate = Schaffhausen_unempl_rate.drop(0)
Schaffhausen_unempl_rate.columns = Unempl_rate

table_Schaffhausen_asyl = pd.concat([data_asyl_10.iloc[[15]], data_asyl_11.iloc[[15]], 
                               data_asyl_12.iloc[[15]], data_asyl_13.iloc[[15]],
                               data_asyl_14.iloc[[15]], data_asyl_15.iloc[[15]],
                               data_asyl_16.iloc[[15]], data_asyl_17.iloc[[15]],
                               data_asyl_18.iloc[[15]], data_asyl_19.iloc[[15]],
                               data_asyl_20.iloc[[15]]])
table_Schaffhausen_asyl = table_Schaffhausen_asyl.drop('Canton', axis=1)

table_Schaffhausen = pd.merge(pd.merge(Schaffhausen_empl, Schaffhausen_unempl, on='Year'), Schaffhausen_unempl_rate, on='Year')
table_Schaffhausen = pd.merge(table_Schaffhausen, table_Schaffhausen_asyl, on='Year')

# Schwyz #
Schwyz_empl = data_swiss_pop[[0,64,65,66]]
Schwyz_empl = Schwyz_empl.drop([0,1])
Schwyz_empl.columns = Empl

Schwyz_unempl = data_swiss_unempl[[0,22]]
Schwyz_unempl = Schwyz_unempl.drop(0)
Schwyz_unempl.columns = Unempl

Schwyz_unempl_rate = data_swiss_unempl[[0,22]]
Schwyz_unempl_rate = Schwyz_unempl_rate.drop(0)
Schwyz_unempl_rate.columns = Unempl_rate

table_Schwyz_asyl = pd.concat([data_asyl_10.iloc[[16]], data_asyl_11.iloc[[16]], 
                               data_asyl_12.iloc[[16]], data_asyl_13.iloc[[16]],
                               data_asyl_14.iloc[[16]], data_asyl_15.iloc[[16]],
                               data_asyl_16.iloc[[16]], data_asyl_17.iloc[[16]],
                               data_asyl_18.iloc[[16]], data_asyl_19.iloc[[16]],
                               data_asyl_20.iloc[[16]]])
table_Schwyz_asyl = table_Schwyz_asyl.drop('Canton', axis=1)

table_Schwyz = pd.merge(pd.merge(Schwyz_empl, Schwyz_unempl, on='Year'), Schwyz_unempl_rate, on='Year')
table_Schwyz = pd.merge(table_Schwyz, table_Schwyz_asyl, on='Year')

# Solothurn #
Solothurn_empl = data_swiss_pop[[0,16,17,18]]
Solothurn_empl = Solothurn_empl.drop([0,1])
Solothurn_empl.columns = Empl

Solothurn_unempl = data_swiss_unempl[[0,6]]
Solothurn_unempl = Solothurn_unempl.drop(0)
Solothurn_unempl.columns = Unempl

Solothurn_unempl_rate = data_swiss_unempl[[0,6]]
Solothurn_unempl_rate = Solothurn_unempl_rate.drop(0)
Solothurn_unempl_rate.columns = Unempl_rate

table_Solothurn_asyl = pd.concat([data_asyl_10.iloc[[17]], data_asyl_11.iloc[[17]], 
                               data_asyl_12.iloc[[17]], data_asyl_13.iloc[[17]],
                               data_asyl_14.iloc[[17]], data_asyl_15.iloc[[17]],
                               data_asyl_16.iloc[[17]], data_asyl_17.iloc[[17]],
                               data_asyl_18.iloc[[17]], data_asyl_19.iloc[[17]],
                               data_asyl_20.iloc[[17]]])
table_Solothurn_asyl = table_Solothurn_asyl.drop('Canton', axis=1)

table_Solothurn = pd.merge(pd.merge(Solothurn_empl, Solothurn_unempl, on='Year'), Solothurn_unempl_rate, on='Year')
table_Solothurn = pd.merge(table_Solothurn, table_Solothurn_asyl, on='Year')

# St. Gallen #
StGallen_empl = data_swiss_pop[[0,49,50,51]]
StGallen_empl = StGallen_empl.drop([0,1])
StGallen_empl.columns = Empl

StGallen_unempl = data_swiss_unempl[[0,17]]
StGallen_unempl = StGallen_unempl.drop(0)
StGallen_unempl.columns = Unempl

StGallen_unempl_rate = data_swiss_unempl[[0,17]]
StGallen_unempl_rate = StGallen_unempl_rate.drop(0)
StGallen_unempl_rate.columns = Unempl_rate

table_StGallen_asyl = pd.concat([data_asyl_10.iloc[[18]], data_asyl_11.iloc[[18]], 
                               data_asyl_12.iloc[[18]], data_asyl_13.iloc[[18]],
                               data_asyl_14.iloc[[18]], data_asyl_15.iloc[[18]],
                               data_asyl_16.iloc[[18]], data_asyl_17.iloc[[18]],
                               data_asyl_18.iloc[[18]], data_asyl_19.iloc[[18]],
                               data_asyl_20.iloc[[18]]])
table_StGallen_asyl = table_StGallen_asyl.drop('Canton', axis=1)

table_StGallen = pd.merge(pd.merge(StGallen_empl, StGallen_unempl, on='Year'), StGallen_unempl_rate, on='Year')
table_StGallen = pd.merge(table_StGallen, table_StGallen_asyl, on='Year')

# Tessin #
Tessin_empl = data_swiss_pop[[0,76,77,78]]
Tessin_empl = Tessin_empl.drop([0,1])
Tessin_empl.columns = Empl

Tessin_unempl = data_swiss_unempl[[0,26]]
Tessin_unempl = Tessin_unempl.drop(0)
Tessin_unempl.columns = Unempl

Tessin_unempl_rate = data_swiss_unempl[[0,26]]
Tessin_unempl_rate = Tessin_unempl_rate.drop(0)
Tessin_unempl_rate.columns = Unempl_rate

table_Tessin_asyl = pd.concat([data_asyl_10.iloc[[19]], data_asyl_11.iloc[[19]], 
                               data_asyl_12.iloc[[19]], data_asyl_13.iloc[[19]],
                               data_asyl_14.iloc[[19]], data_asyl_15.iloc[[19]],
                               data_asyl_16.iloc[[19]], data_asyl_17.iloc[[19]],
                               data_asyl_18.iloc[[19]], data_asyl_19.iloc[[19]],
                               data_asyl_20.iloc[[19]]])
table_Tessin_asyl = table_Tessin_asyl.drop('Canton', axis=1)

table_Tessin = pd.merge(pd.merge(Tessin_empl, Tessin_unempl, on='Year'), Tessin_unempl_rate, on='Year')
table_Tessin = pd.merge(table_Tessin, table_Tessin_asyl, on='Year')

# Thurgau #
Thurgau_empl = data_swiss_pop[[0,55,56,57]]
Thurgau_empl = Thurgau_empl.drop([0,1])
Thurgau_empl.columns = Empl

Thurgau_unempl = data_swiss_unempl[[0,19]]
Thurgau_unempl = Thurgau_unempl.drop(0)
Thurgau_unempl.columns = Unempl

Thurgau_unempl_rate = data_swiss_unempl[[0,19]]
Thurgau_unempl_rate = Thurgau_unempl_rate.drop(0)
Thurgau_unempl_rate.columns = Unempl_rate

table_Thurgau_asyl = pd.concat([data_asyl_10.iloc[[20]], data_asyl_11.iloc[[20]], 
                               data_asyl_12.iloc[[20]], data_asyl_13.iloc[[20]],
                               data_asyl_14.iloc[[20]], data_asyl_15.iloc[[20]],
                               data_asyl_16.iloc[[20]], data_asyl_17.iloc[[20]],
                               data_asyl_18.iloc[[20]], data_asyl_19.iloc[[20]],
                               data_asyl_20.iloc[[20]]])
table_Thurgau_asyl = table_Thurgau_asyl.drop('Canton', axis=1)

table_Thurgau = pd.merge(pd.merge(Thurgau_empl, Thurgau_unempl, on='Year'), Thurgau_unempl_rate, on='Year')
table_Thurgau = pd.merge(table_Thurgau, table_Thurgau_asyl, on='Year')

# Uri #
Uri_empl = data_swiss_pop[[0,61,62,63]]
Uri_empl = Uri_empl.drop([0,1])
Uri_empl.columns = Empl

Uri_unempl = data_swiss_unempl[[0,21]]
Uri_unempl = Uri_unempl.drop(0)
Uri_unempl.columns = Unempl

Uri_unempl_rate = data_swiss_unempl[[0,21]]
Uri_unempl_rate = Uri_unempl_rate.drop(0)
Uri_unempl_rate.columns = Unempl_rate

table_Uri_asyl = pd.concat([data_asyl_10.iloc[[21]], data_asyl_11.iloc[[21]], 
                               data_asyl_12.iloc[[21]], data_asyl_13.iloc[[21]],
                               data_asyl_14.iloc[[21]], data_asyl_15.iloc[[21]],
                               data_asyl_16.iloc[[21]], data_asyl_17.iloc[[21]],
                               data_asyl_18.iloc[[21]], data_asyl_19.iloc[[21]],
                               data_asyl_20.iloc[[21]]])
table_Uri_asyl = table_Uri_asyl.drop('Canton', axis=1)

table_Uri = pd.merge(pd.merge(Uri_empl, Uri_unempl, on='Year'), Uri_unempl_rate, on='Year')
table_Uri = pd.merge(table_Uri, table_Uri_asyl, on='Year')

# Waadt #
Waadt_empl = data_swiss_pop[[0,1,2,3]]
Waadt_empl = Waadt_empl.drop([0,1])
Waadt_empl.columns = Empl

Waadt_unempl = data_swiss_unempl[[0,1]]
Waadt_unempl = Waadt_unempl.drop(0)
Waadt_unempl.columns = Unempl

Waadt_unempl_rate = data_swiss_unempl[[0,1]]
Waadt_unempl_rate = Waadt_unempl_rate.drop(0)
Waadt_unempl_rate.columns = Unempl_rate

table_Waadt_asyl = pd.concat([data_asyl_10.iloc[[22]], data_asyl_11.iloc[[22]], 
                               data_asyl_12.iloc[[22]], data_asyl_13.iloc[[22]],
                               data_asyl_14.iloc[[22]], data_asyl_15.iloc[[22]],
                               data_asyl_16.iloc[[22]], data_asyl_17.iloc[[22]],
                               data_asyl_18.iloc[[22]], data_asyl_19.iloc[[22]],
                               data_asyl_20.iloc[[22]]])
table_Waadt_asyl = table_Waadt_asyl.drop('Canton', axis=1)

table_Waadt = pd.merge(pd.merge(Waadt_empl, Waadt_unempl, on='Year'), Waadt_unempl_rate, on='Year')
table_Waadt = pd.merge(table_Waadt, table_Waadt_asyl, on='Year')

# Wallis #
Wallis_empl = data_swiss_pop[[0,4,5,6]]
Wallis_empl = Wallis_empl.drop([0,1])
Wallis_empl.columns = Empl

Wallis_unempl = data_swiss_unempl[[0,2]]
Wallis_unempl = Wallis_unempl.drop(0)
Wallis_unempl.columns = Unempl

Wallis_unempl_rate = data_swiss_unempl[[0,2]]
Wallis_unempl_rate = Wallis_unempl_rate.drop(0)
Wallis_unempl_rate.columns = Unempl_rate

table_Wallis_asyl = pd.concat([data_asyl_10.iloc[[23]], data_asyl_11.iloc[[23]], 
                               data_asyl_12.iloc[[23]], data_asyl_13.iloc[[23]],
                               data_asyl_14.iloc[[23]], data_asyl_15.iloc[[23]],
                               data_asyl_16.iloc[[23]], data_asyl_17.iloc[[23]],
                               data_asyl_18.iloc[[23]], data_asyl_19.iloc[[23]],
                               data_asyl_20.iloc[[23]]])
table_Wallis_asyl = table_Wallis_asyl.drop('Canton', axis=1)

table_Wallis = pd.merge(pd.merge(Wallis_empl, Wallis_unempl, on='Year'), Wallis_unempl_rate, on='Year')
table_Wallis = pd.merge(table_Wallis, table_Wallis_asyl, on='Year')

# Zug #
Zug_empl = data_swiss_pop[[0,73,74,75]]
Zug_empl = Zug_empl.drop([0,1])
Zug_empl.columns = Empl

Zug_unempl = data_swiss_unempl[[0,25]]
Zug_unempl = Zug_unempl.drop(0)
Zug_unempl.columns = Unempl

Zug_unempl_rate = data_swiss_unempl[[0,25]]
Zug_unempl_rate = Zug_unempl_rate.drop(0)
Zug_unempl_rate.columns = Unempl_rate

table_Zug_asyl = pd.concat([data_asyl_10.iloc[[24]], data_asyl_11.iloc[[24]], 
                               data_asyl_12.iloc[[24]], data_asyl_13.iloc[[24]],
                               data_asyl_14.iloc[[24]], data_asyl_15.iloc[[24]],
                               data_asyl_16.iloc[[24]], data_asyl_17.iloc[[24]],
                               data_asyl_18.iloc[[24]], data_asyl_19.iloc[[24]],
                               data_asyl_20.iloc[[24]]])
table_Zug_asyl = table_Zug_asyl.drop('Canton', axis=1)

table_Zug = pd.merge(pd.merge(Zug_empl, Zug_unempl, on='Year'), Zug_unempl_rate, on='Year')
table_Zug = pd.merge(table_Zug, table_Zug_asyl, on='Year')

# Zürich #
Zürich_empl = data_swiss_pop[[0,34,35,36]]
Zürich_empl = Zürich_empl.drop([0,1])
Zürich_empl.columns = Empl

Zürich_unempl = data_swiss_unempl[[0,12]]
Zürich_unempl = Zürich_unempl.drop(0)
Zürich_unempl.columns = Unempl

Zürich_unempl_rate = data_swiss_unempl[[0,12]]
Zürich_unempl_rate = Zürich_unempl_rate.drop(0)
Zürich_unempl_rate.columns = Unempl_rate

table_Zürich_asyl = pd.concat([data_asyl_10.iloc[[25]], data_asyl_11.iloc[[25]], 
                               data_asyl_12.iloc[[25]], data_asyl_13.iloc[[25]],
                               data_asyl_14.iloc[[25]], data_asyl_15.iloc[[25]],
                               data_asyl_16.iloc[[25]], data_asyl_17.iloc[[25]],
                               data_asyl_18.iloc[[25]], data_asyl_19.iloc[[25]],
                               data_asyl_20.iloc[[25]]])
table_Zürich_asyl = table_Zürich_asyl.drop('Canton', axis=1)

table_Zürich = pd.merge(pd.merge(Zürich_empl, Zürich_unempl, on='Year'), Zürich_unempl_rate, on='Year')
table_Zürich = pd.merge(table_Zürich, table_Zürich_asyl, on='Year')

###### End of regional data preparation ###### 