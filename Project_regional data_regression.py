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

groupDE= [table_thüringen, table_schleswig_holstein, table_sachsen_anhalt, table_sachsen, 
            table_saarland, table_rheinland_pfalz, table_NRW, table_niedersachsen, 
            table_mecklenburg_vorpommern, table_hessen, table_HH, table_bremen, 
            table_brandenburg, table_berlin, table_bayern, table_BaWü]

for i in groupDE:
    i = i.drop('Unnamed: 0', axis=1, inplace=True)
    

# adding a column for the number of refugees relative to the population
for i in groupDE:
    i['Refugees/Pop'] = (i['Foreigners']/i['Population'])*100
    
    
# analysing the development of employment and unemployment in the Bundesländer
bundesländer = ['Thüringen', 'Schleswig Holstein', 'Sachsen Anhalt', 'Sachsen', 'Saarland', 'Rheinland Pfalz',
                'NRW', 'Niedersachsen', 'Mecklenburg Vorpommern', 'Hessen', 'Hamburg', 'Bremen', 'Brandenburg',
                'Berlin', 'Bayern', 'Baden Württemberg']

for i, land in zip(groupDE, bundesländer):
    plt.plot(i['Year'], i['Total Empl'])
    plt.ylabel('Total Employment')
    plt.title(land)
    plt.show()
# we can already see here that many Bundesländer are affected by the wave of refugees in 2015:
    # the level of employment in a geringfügige Beschäftigung is increasing

for i, land in zip(groupDE, bundesländer):
    plt.plot(i['Year'], i['Unemployment Rate'])
    plt.ylabel('Unemployment Rate')
    plt.title(land)
    plt.show()
    
    
# analysing the development of the number of refugees in the Bundesländer
for i, land in zip(groupDE, bundesländer):
    plt.plot(i['Year'], i['Refugees/Pop'])
    plt.ylabel('Refugees rel. to Population')
    plt.title(land)
    plt.show()
# create a table for the change in Refugees/Pop between 2014 and 2016
li16 = []
for i in groupDE:
    outcome_16 = pd.DataFrame(i.loc[(i['Year'] == 2016),'Refugees/Pop']).reset_index(drop=True)
    outcome_14 = pd.DataFrame(i.loc[(i['Year'] == 2014),'Refugees/Pop']).reset_index(drop=True)  
    outcome_diff = outcome_16 - outcome_14
    li16.append(outcome_diff)

outcome_diffDE = pd.concat(li16, ignore_index=True)
outcome_diffDE = outcome_diffDE.drop(outcome_diffDE.index[[15]], axis=0).reset_index(drop=True)
outcome_diffDE['Bundesland'] = bundesländer
outcome_diffDE = outcome_diffDE.sort_values(by=['Refugees/Pop']).reset_index(drop=True)
outcome_diffDE.rename(columns = {'Refugees/Pop':'Change in Ref/Pop'}, inplace = True)
# save as excel
outcome_diffDE.to_excel(PATH + 'Refugees_Diff_Bundesländer.xlsx')


# ATET estimation with Mecklenburg-Vorpommern as the control and Schleswig-Holstein as the treatment
    # checking for the common trend for employment
plt.plot(table_mecklenburg_vorpommern['Year'], table_mecklenburg_vorpommern['Total Empl'], label='MV')
plt.plot(table_schleswig_holstein['Year'], table_schleswig_holstein['Total Empl'], label='SH')
plt.legend()
plt.title('Employment in MV and SH')
plt.show()
    # checking for the common trend for unemployment
plt.plot(table_mecklenburg_vorpommern['Year'], table_mecklenburg_vorpommern['Unemployment Rate'], label='MV')
plt.plot(table_schleswig_holstein['Year'], table_schleswig_holstein['Unemployment Rate'], label='SH')
plt.legend()
plt.title('Unemployment Rate in MV and SH')
plt.show()
   
table_mecklenburg_vorpommern['Treat'], table_schleswig_holstein['Treat'] = 0,1
table_MV_SH = pd.concat([table_mecklenburg_vorpommern, table_schleswig_holstein]).reset_index(drop=True)

Y_NAME1= 'Total Empl' # only geringfügige Verhältnisse
Y_NAME2= 'Unemployment Rate'
D_NAME= 'Treat'
T_NAME= 'Year'
    # getting the ATET
pc.my_atet(data= table_MV_SH, outcome= Y_NAME1, treat= D_NAME, time= T_NAME)
pc.my_atet(data= table_MV_SH, outcome= Y_NAME2, treat= D_NAME, time= T_NAME)


###############################################################################


# import data on the cantons
table_aargau= pd.read_csv(PATH2 + 'table_aargau.csv')
table_appenzellA= pd.read_csv(PATH2 + 'table_appenzellA.csv')
table_appenzellI= pd.read_csv(PATH2 + 'table_appenzellI.csv')
table_baselL= pd.read_csv(PATH2 + 'table_baselL.csv')
table_baselS= pd.read_csv(PATH2 + 'table_baselS.csv')
table_bern= pd.read_csv(PATH2 + 'table_bern.csv')
table_freiburg= pd.read_csv(PATH2 + 'table_freiburg.csv')
table_genf= pd.read_csv(PATH2 + 'table_genf.csv')
table_glarus= pd.read_csv(PATH2 + 'table_glarus.csv')
table_graubünden= pd.read_csv(PATH2 + 'table_graubünden.csv')
table_jura= pd.read_csv(PATH2 + 'table_jura.csv')
table_luzern= pd.read_csv(PATH2 + 'table_luzern.csv')
table_neuenburg= pd.read_csv(PATH2 + 'table_neuenburg.csv')
table_nidwalden= pd.read_csv(PATH2 + 'table_nidwalden.csv')
table_obwalden= pd.read_csv(PATH2 + 'table_obwalden.csv')
table_schaffhausen= pd.read_csv(PATH2 + 'table_schaffhausen.csv')
table_schwyz= pd.read_csv(PATH2 + 'table_schwyz.csv')
table_solothurn= pd.read_csv(PATH2 + 'table_solothurn.csv')
table_SG= pd.read_csv(PATH2 + 'table_SG.csv')
table_tessin= pd.read_csv(PATH2 + 'table_tessin.csv')
table_thurgau= pd.read_csv(PATH2 + 'table_thurgau.csv')
table_uri= pd.read_csv(PATH2 + 'table_uri.csv')
table_waadt= pd.read_csv(PATH2 + 'table_waadt.csv')
table_wallis= pd.read_csv(PATH2 + 'table_wallis.csv')
table_zug= pd.read_csv(PATH2 + 'table_zug.csv')
table_zürich= pd.read_csv(PATH2 + 'table_zürich.csv')


groupCH = [table_aargau, table_appenzellA, table_appenzellI, table_baselL,
            table_baselS, table_bern, table_freiburg, table_genf, table_glarus, 
            table_graubünden, table_jura, table_luzern, table_neuenburg, 
            table_nidwalden, table_obwalden, table_schaffhausen, table_schwyz,
            table_solothurn, table_SG, table_tessin, table_thurgau, table_uri,table_waadt, 
            table_wallis, table_zug, table_zürich]

for i in groupCH:
    i = i.drop('Unnamed: 0', axis=1, inplace=True)


# adding a column for the number of refugees relative to the population
for i in groupCH:
    i['Refugees/Pop'] = (i['Refugees Total']/i['Population'])*100

# analysing the development of employment and unemployment in the cantons
cantons = ['Aargau', 'Appenzell A', 'Appenzell I ', 'Basel L', 'Basel S', 'Bern', 
           'Freiburg', 'Genf', 'Glarus', 'Graubünden', 'Jura', 'Luzern', 'Neuenburg', 
           'Nidwalden','Obwalden', 'Schaffhausen', 'Schwyz', 'Solothurn', 'St. Gallen', 
           'Tessin', 'Thurgau', 'Uri', 'Waadt', 'Wallis', 'Zug', 'Zürich']


# analysing the development of unemployment in the cantons
for i, canton in zip(groupCH, cantons):
    plt.plot(i['Year'], i['Unemployment Rate'])
    plt.ylabel('Unemployment Rate')
    plt.title(canton)
    plt.show()
    
# analysing the development of the number of refugees in the cantona
for i, canton in zip(groupCH, cantons):
    plt.plot(i['Year'], i['Refugees/Pop'])
    plt.ylabel('Refugees rel. to Population')
    plt.title(canton)
    plt.show()

# create a table for the change in Refugees/Pop between 2014 and 2016
li16 = []
for i in groupCH:
    outcome_16 = pd.DataFrame(i.loc[(i['Year'] == 2016),'Refugees/Pop']).reset_index(drop=True)
    outcome_14 = pd.DataFrame(i.loc[(i['Year'] == 2014),'Refugees/Pop']).reset_index(drop=True)  
    outcome_diff = outcome_16 - outcome_14
    li16.append(outcome_diff)

outcome_diffCH = pd.concat(li16, ignore_index=True)
outcome_diffCH['Canton'] = cantons
outcome_diffCH = outcome_diffCH.sort_values(by=['Refugees/Pop']).reset_index(drop=True)
outcome_diffCH.rename(columns = {'Refugees/Pop':'Change in Ref/Pop'}, inplace = True)
#save as excel
outcome_diffCH.to_excel(PATH + 'Refugees_Diff_Cantons.xlsx')


# ATET estimation with Geneva as the control and Vaud as the treatment
    # checking for the common trend for unemployment
plt.plot(table_genf['Year'], table_genf['Unemployment Rate'], label='Geneva')
plt.plot(table_waadt['Year'], table_waadt['Unemployment Rate'], label='Vaud')
plt.title('Unemployment Rate in Geneva and Vaud')
plt.legend()
plt.show()
   
table_genf['Treat'], table_waadt['Treat'] = 0,1
table_genf_waadt = pd.concat([table_genf, table_waadt]).reset_index(drop=True)

Y_NAME= 'Unemployment Rate'
D_NAME= 'Treat'
T_NAME= 'Year'
    # getting the ATET
pc.my_atet(data= table_genf_waadt, outcome= Y_NAME, treat= D_NAME, time= T_NAME)


# ATET estimation with Aargau as the control and Solothurn as the treatment
    # checking for the common trend for unemployment
plt.plot(table_aargau['Year'], table_aargau['Unemployment Rate'], label='Aargau')
plt.plot(table_solothurn['Year'], table_solothurn['Unemployment Rate'], label='Solothurn')
plt.title('Unemployment Rate in Aargau and Solothurn')
plt.legend()
plt.show()
   
table_aargau['Treat'], table_solothurn['Treat'] = 0,1
table_aargau_solothurn = pd.concat([table_aargau, table_solothurn]).reset_index(drop=True)

Y_NAME= 'Unemployment Rate'
D_NAME= 'Treat'
T_NAME= 'Year'
    # getting the ATET
pc.my_atet(data= table_aargau_solothurn, outcome= Y_NAME, treat= D_NAME, time= T_NAME)

# get the ATET with unemployment instead of unemployment rate
# create function for the plots
    