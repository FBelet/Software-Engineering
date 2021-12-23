"""

## SOFTWARE ENGINEERING ##
      ### GROUP 3 ###
      
# regression and analysis of national data #

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
OUTPUT_NAME = 'Project_Output_Regression'

# save the console output in parallel to a txt file
orig_stdout = sys.stdout
sys.stdout = pc.Output(path=PATH, name=OUTPUT_NAME)


# import data 
PATH2 = 'C:/Users/fabie/Universität St.Gallen/Software-Engineering/Final Datasets/'

table_germany = pd.read_csv(PATH2 + 'table_germany.csv')
table_germany = table_germany.drop('Unnamed: 0', axis=1)
table_switzerland = pd.read_csv(PATH2 + 'table_switzerland.csv')
table_switzerland = table_switzerland.drop('Unnamed: 0', axis=1)

# rename columns
table_germany.rename(columns = {'Total Empl Foreign':'Total Empl Foreigners', 'Total Empl German':
                                'Total Empl National (CH/DE)'}, 
                                 inplace = True)
table_switzerland.rename(columns = {'Population Total': 'Total Population',
                                   'Refugees Total':'Total refugees', 'Total Empl Swiss':
                                      'Total Empl National (CH/DE)'}, inplace = True)
# drop 2010 to 2012 so that datasets can be merged and compared
table_switzerland2 = table_switzerland.drop(table_switzerland.index[[0,1,2]], axis=0)


# checking the development of unemployment and employment for Germany and Switzerland 
pc.my_chart(data1=table_germany, data2=table_switzerland2, varname='Total Empl', label1= 'Germany', 
            label2='Switzerland', location='center left', title='Employment in DE and CH')
pc.my_chart(data1=table_germany, data2=table_switzerland2, varname='Total Empl Foreigners', label1= 'Germany', 
            label2='Switzerland', location='upper left', title='Employment of foreigners in DE and CH')
pc.my_chart(data1=table_germany, data2=table_switzerland2, varname='Unemployment Rate', label1='Germany', 
            label2='Switzerland', location='center left', title='Unemployment rate in DE and CH')


# checking the development of the number of refugees
    # create column for refugees in relation to population
table_germany['Refugees/Pop'] = (table_germany['Total refugees']/table_germany['Total Population'])*100
table_switzerland2['Refugees/Pop'] = (table_switzerland2['Total refugees']/table_switzerland2['Total Population'])*100

pc.my_chart(data1=table_germany, data2=table_switzerland2, varname='Refugees/Pop', label1= 'Germany', 
            label2='Switzerland', location='upper left', title= 'Refugees rel. to the pop. in DE and CH')


# checking the development of population in general
pc.my_chart(data1=table_germany, data2=table_switzerland2, varname='Total Population', label1='Germany', 
            label2='Switzerland', location='center left', title='Total Population in DE and CH')


# creating country dummies and merging the tables into one dataset
table_germany['Country'] = 1 #treatement
table_switzerland2['Country'] = 0 #control
table_all = pd.concat([table_germany, table_switzerland2]).reset_index(drop=True)

# next, we can define the treatment and outcome variable as well as the covariates
Y_NAME1= 'Total Empl'
Y_NAME2= 'Total Empl Foreigners'
Y_NAME3= 'Unemployment Rate'
D_NAME= 'Country' #treatment
T_NAME= 'Year'

# next, we drop all unneccessary columns and rows
table_all2 = table_all.drop(table_all.index[[0,2,4,5,6,7,8,10,12,13,14,15]])
table_all2 = table_all2.drop(['Helper', 'Skilled worker', 'Specialist', 'Expert', 'without educ',
                             'with educ', 'with academic educ', 'educ unknown',
                             'Total Sec.1', 'Total Sec.2', 'Total Sec.3', 'Total Swiss Sec.1', 
                             'Total Swiss Sec.2', 'Total Swiss Sec.3', 'Total Foreign Sec. 1', 
                             'Total Foreign Sec.2', 'Total Foreign Sec.3','Empl settled','Empl resident',
                             'Empl border', 'Empl shortterm','Empl other'], axis=1)


# estimate the ATET by difference of mean differences without covariates (for total employment)
pc.my_atet(data=table_all2, outcome=Y_NAME1, treat=D_NAME, time=T_NAME)

# estimate the ATET by difference of mean differences without covariates (for the employment level of foreigners)
pc.my_atet(data=table_all2, outcome=Y_NAME2, treat=D_NAME, time=T_NAME)

# estimate the ATET by difference of mean differences without covariates (for the unemployment rate)
pc.my_atet(data=table_all2, outcome=Y_NAME3, treat=D_NAME, time=T_NAME)


# since we also have data on the employment levels for low-wage jobs in Germany, it would be interesting
# to look at their development:
Y_NAME3= 'Total Empl (geringfügig)'
x_names= ('Total Population', 'Total refugees', 'without educ', 'Year')

pc.my_ols(exog=table_germany.loc[:, x_names], outcome= table_germany[Y_NAME3])

# closing the output file
sys.stdout.output.close()
sys.stdout = orig_stdout

######## End of national data regression ########