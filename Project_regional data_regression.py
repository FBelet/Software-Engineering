"""

## SOFTWARE ENGINEERING ##
      ### GROUP 3 ###
      
# analysis and regression of regional data #

Berenice Flumenbaum & Fabienne Belet


"""

# import modules
import sys
import pandas as pd
import matplotlib.pyplot as plt



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
PATH2 = '/Users/bereniceflumenbaum/Documents/GitHub/Software Engineering/Final Datasets/'

table_thüringen= pd.read_csv(PATH2 + 'table_thüringen.csv')
table_schleswig_holstein= pd.read_csv(PATH2 + 'table_schleswig_holstein.csv')
table_sachsen_anhalt= pd.read_csv(PATH2 + 'table_sachsen_anhalt.csv')
table_sachsen= pd.read_csv(PATH2 +'table_sachsen.csv')
table_saarland= pd.read_csv(PATH2 +'table_saarland.csv')
table_rheinland_pfalz= pd.read_csv(PATH2 + 'table_rheinland_pfalz.csv')
table_NRW= pd.read_csv(PATH2 +'table_NRW.csv')
table_niedersachsen= pd.read_csv(PATH2 +'table_niedersachsen.csv')
table_mecklenburg_vorpommern= pd.read_csv(PATH2 +'table_mecklenburg_vorpommern.csv')
table_hessen= pd.read_csv(PATH2 +'table_hessen.csv')
table_HH= pd.read_csv(PATH2 + 'table_HH.csv')
table_bremen= pd.read_csv(PATH2 +'table_bremen.csv')
table_brandenburg= pd.read_csv(PATH2 +'table_brandenburg.csv')
table_berlin= pd.read_csv(PATH2 +'table_berlin.csv')
table_bayern= pd.read_csv(PATH2 +'table_bayern.csv')
table_BaWü= pd.read_csv(PATH2 +'table_BaWü.csv')

groupDF= [table_thüringen, table_schleswig_holstein, table_sachsen_anhalt, table_sachsen, 
            table_saarland, table_rheinland_pfalz, table_NRW, table_niedersachsen, 
            table_mecklenburg_vorpommern, table_hessen, table_HH, table_bremen, 
            table_brandenburg, table_berlin, table_bayern, table_BaWü]

for i in groupDF:
    i = i.drop('Unnamed: 0', axis=1, inplace=True)
    

# adding a column for the number of refugees relative to the population
for i in groupDF:
    i['Refugees/Pop'] = (i['Foreigners']/i['Population'])*100
    
    
# analysing the development of employment and unemployment in the Bundesländer
bundesländer = ['Thüringen', 'Schleswig Holstein', 'Sachsen Anhalt', 'Sachsen', 'Saarland', 'Rheinland Pfalz',
                'NRW', 'Niedersachsen', 'Mecklenburg Vorpommern', 'Hessen', 'Hamburg', 'Bremen', 'Brandenburg',
                'Berlin', 'Bayern', 'Baden Württemberg']

for i, land in zip(groupDF, bundesländer):
    plt.plot(i['Year'], i['Total Empl'])
    plt.ylabel('Total Employment')
    plt.title(land)
    plt.show()
# we can already see here that many Bundesländer are affected by the wave of refugees in 2015:
    # the level of employment in a geringfügige Beschäftigung is increasing

for i, land in zip(groupDF, bundesländer):
    plt.plot(i['Year'], i['Unemployment Rate'])
    plt.ylabel('Unemployment Rate')
    plt.title(land)
    plt.show()
    
    
# analysing the development of the number of refugees in the Bundesländer
for i, land in zip(groupDF, bundesländer):
    plt.plot(i['Year'], i['Refugees/Pop'])
    plt.ylabel('Refugees rel. to Population')
    plt.title(land)
    plt.show()
# create a table for the change in Refugees/Pop between 2014 and 2016
li16 = []
for i in groupDF:
    outcome_16 = pd.DataFrame(i.loc[(i['Year'] == 2016),'Refugees/Pop']).reset_index(drop=True)
    outcome_14 = pd.DataFrame(i.loc[(i['Year'] == 2014),'Refugees/Pop']).reset_index(drop=True)  
    outcome_diff = outcome_16 - outcome_14
    li16.append(outcome_diff)

outcome_diff16 = pd.concat(li16, ignore_index=True)
outcome_diff16 = outcome_diff16.drop(outcome_diff16.index[[15]], axis=0).reset_index(drop=True)
outcome_diff16['Bundesland'] = bundesländer
outcome_diff16 = outcome_diff16.sort_values(by=['Refugees/Pop']).reset_index(drop=True)
# save as excel
outcome_diff16.to_excel(PATH + 'Refugees_Diff16_Bundesländer.xlsx')

# do the same for the years 2014 and 2015
li15 = []
for i in groupDF:
    outcome_15 = pd.DataFrame(i.loc[(i['Year'] == 2015),'Refugees/Pop']).reset_index(drop=True)
    outcome_14 = pd.DataFrame(i.loc[(i['Year'] == 2014),'Refugees/Pop']).reset_index(drop=True)  
    outcome_diff = outcome_15 - outcome_14
    li15.append(outcome_diff)

outcome_diff15 = pd.concat(li15, ignore_index=True)
outcome_diff15['Bundesland'] = bundesländer
outcome_diff15 = outcome_diff15.sort_values(by=['Refugees/Pop']).reset_index(drop=True)
# save as excel
outcome_diff15.to_excel(PATH + 'Refugees_Diff15_Bundesländer.xlsx')


# next: choose a control and treatment bundesland and get the atet, do the same for cantons
# next: also look at geringfügige beschäftigung


