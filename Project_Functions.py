"""

## SOFTWARE ENGINEERING ##
      ### GROUP 3 ###

Berenice Flumenbaum & Fabienne Belet
    
          Functions

"""

# import modules

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# create function to get overview over datasets
def my_summary_stats(data):
    """
    Summary stats: missing values, unique values, maximum and minimum.

    Parameters
    ----------
    data : TYPE: pd.DataFrame
        DESCRIPTION: dataframe for which descriptives will be computed
    Returns

    -------
    None. Prints descriptive table od the data
    """
    # generate storage for the stats as an empty dictionary
    my_descriptives = {}
    # loop over columns
    for col_id in data.columns:
        # fill in the dictionary with descriptive values by assigning the
        # column ids as keys for the dictionary
        my_descriptives[col_id] = [sum(data[col_id].isna()),          # missing
                                   sum(data[col_id].isnull()),
                                   len(data[col_id].unique()),  # unique values
                                   data[col_id].shape[0]]      # number of obs.
    # convert the dictionary to dataframe for a nicer output and name rows
    # pandas dataframe will automatically take the keys as columns if the
    # data input is a dictionary. Transpose for having the stats as columns
    my_descriptives = pd.DataFrame(my_descriptives,
                                   index=['na', 'null', 'unique', 'obs']).transpose()
    # define na, unique and obs as integers such that no decimals get printed
    ints = ['na', 'null', 'unique', 'obs']
    # use the .astype() method of pandas dataframes to change the type
    my_descriptives[ints] = my_descriptives[ints].astype(int)
    # print the descriptives, (\n inserts a line break)
    print('Descriptive Statistics:', '-' * 80,
          round(my_descriptives, 2), '-' * 80, '\n\n', sep='\n')
    
# define function to organize datasets
def organize(data, value, drop_values, column_names):
    """
    Organize function: delete rows, drop nan values and drop row 0.
    
    Parameters
    -----------------
    data: TYPE: pd.dict
        DESCRIPTION: contains dataframes with information
    value: contains value 0 or 1 for the two relevant dataframes (keys of dictionaries)
    drop_values: values to be dropped
    column_names: names for columns to be selected
    -----------------
    
    """
    
    variable = data[value] # decide which key of dictionary to use
    variable = variable.head(2) # only keep first two rows
    variable = variable.dropna(axis = 1) # drop all columns with nan values
    variable = variable.drop(variable[drop_values], axis = 1) # drop unnecessary columns
    variable = variable.drop(0) # drop row 0
    variable.columns = column_names # define column names
    return variable

# loop over keys in dictionary to organize the data in the dataframes
def organize_Bundesländer(name, data, drop_values, column_names):
    
    for key in data:
        variable = data[key] # decide which key of dictionary to use
        variable = variable.head(2) # only keep first two rows
        variable = variable.dropna(axis = 1) # drop all columns with nan values
        variable = variable.drop(variable.columns[drop_values], axis = 1) # drop unnecessary columns
        variable = variable.drop(0) # drop row 0
        variable.columns = column_names # define column names
        name[key] = pd.DataFrame(variable)

def create_table(data):
    variable = pd.concat([data[5], data[7], data[9], data[11], data[13], data[15], data[17], data[19]])
    return variable
        
def create_table2(data2):
    variable = pd.concat([data2[6], data2[8], data2[10], data2[12], data2[14], data2[16], data2[18], data2[20]])
    return variable

def extract_values(land, data, names):
    variable = data[['Year', land]]
    variable.columns = names
    return variable

# define function to organize datasets
def organize_unempl(data, value, column_names):
    """
    Organize function: delete rows, drop nan values and drop row 0.
    
    Parameters
    -----------------
    data: TYPE: pd.dict
        DESCRIPTION: contains dataframes with information
    value: contains value 2 or 3 for the two relevant dataframes (keys of dictionaries)
    drop_values: values to be dropped
    column_names: names for columns to be selected
    -----------------
    
    """
    
    variable = data[value] # decide which key of dictionary to use
    variable = variable.drop(0) # drop row 0
    variable = variable.dropna(axis = 1) # drop all columns with nan values
    variable.columns = column_names # define column names
    return variable
 
# define function to organize datasets Swiss data
def organize_CH(data, drop_rows, drop_values, column_names):
    """
    Organize function: delete rows, drop nan values and drop row 0.
    
    Parameters
    -----------------
    data: TYPE: pd.dict
        DESCRIPTION: contains dataframes with information
    drop_values: values to be dropped
    column_names: names for columns to be selected
    -----------------
    
    """

    data = data.drop(drop_rows) # drop unnecessary rows
    data = data.drop(drop_values, axis=1) # drop unnecessary columns
    data.columns = column_names # define column names
    return data

def organize_CH_asyl(data, drop_rows, drop_values, column_names):
    """
    Organize function: delete rows, drop nan values and drop row 0.
    
    Parameters
    -----------------
    data: TYPE: pd.dict
        DESCRIPTION: contains dataframes with information
    drop_values: values to be dropped
    column_names: names for columns to be selected
    -----------------
    
    """

    data = data.drop(drop_rows) # drop unnecessary rows
    data = data.drop(drop_values, axis=1) # drop unnecessary columns
    data = data.dropna(axis = 1) # drop all columns with nan values
    data.columns = column_names # define column names
    return data

def organize_CH1(data, drop_rows, drop_values):
    """
    Organize function: delete rows, drop nan values and drop row 0.
    
    Parameters
    -----------------
    data: TYPE: pd.dict
        DESCRIPTION: contains dataframes with information
    drop_values: values to be dropped
    column_names: names for columns to be selected
    -----------------
    
    """

    data = data.drop(drop_rows) # drop unnecessary rows
    data = data.drop(drop_values, axis=1) # drop unnecessary columns
    return data

def organize_CH_2(data, drop_values, column_names):
    """
    Organize function: delete rows, drop nan values and drop row 0.
    
    Parameters
    -----------------
    data: TYPE: pd.dict
        DESCRIPTION: contains dataframes with information
    drop_values: values to be dropped
    column_names: names for columns to be selected
    -----------------
    
    """

    data = data.head(4) # drop unnecessary rows
    data = data.drop(drop_values, axis=1) # drop unnecessary columns
    data = data.drop([0,1,2]) # drop the first 3 rows
    data.columns = column_names # define column names
    return data

def organize_regional(data, drop_values, column_names):
    """
    Organize function: delete rows, drop nan values and drop row 0.
    
    Parameters
    -----------------
    data: TYPE: pd.dict
        DESCRIPTION: contains dataframes with information
    value: contains value 0 or 1 for the two relevant dataframes (keys of dictionaries)
    drop_values: values to be dropped
    column_names: names for columns to be selected
    -----------------
    
    """

    data = data.drop(data.columns[drop_values], axis=1) # drop unnecessary columns
    data = data.drop(0) # drop the first row
    data.columns = column_names # define column names
    return data



def my_chart(data1, data2, varname, label1, label2, location):
    """
    Plot line chart.

    Parameters
    ----------
    data : TYPE: pd.DataFrame
        DESCRIPTION: dataframe containing variables of interest
    varname : TYPE: string
        DESCRIPTION: variable name for which line chart should be plotted
    year: TYPE: string
        DESCRIPTION: years for which the line chart should be plotted
    label: TYPE: string
        DESCRIPTION: Label for the legend
    Returns
    -------
    None. Prints line chart.
    """
    plt.plot(data1['Year'], data1[varname], color='blue', label=label1)
    plt.plot(data2['Year'], data2[varname], color='orange', label=label2)
    # add legend
    plt.legend(loc=location)
    plt.show
    # add title
    plt.title(varname + ' in Germany and Switzerland over time')
    # add labels
    plt.xlabel(data1['Year'])
    plt.ylabel(varname)
    plt.show()
    
    
    

def my_atet(data, outcome, treat, time):
    """
    Calculate the ATET.

    Parameters
    ----------
    data : TYPE: pd.DataFrame
        DESCRIPTION: dataframe containing variables of interest
    outcome : TYPE: string
        DESCRIPTION: outcome variable of interest
    treat: TYPE: string
        DESCRIPTION: treatment variable
    time: TYPE: string
        DESCRIPTION: time dimension before or after the treatment
    Returns
    -------
    None. Prints line chart.
    """
    # ATET = E[Y|X=x, T=1, D=1] - E[Y|X=x, T=0, D=1]
    #         - (E[Y|X=x, T=1, D=0] - E[Y|X=x, T=0, D=0])

    y1_1 = data.loc[(data[time] == 2016) & (data[treat] == 1), outcome]
    y1_0 = data.loc[(data[time] == 2014) & (data[treat] == 1), outcome]

    y0_1 = data.loc[(data[time] == 2016) & (data[treat] == 0), outcome]
    y0_0 = data.loc[(data[time] == 2014) & (data[treat] == 0), outcome]

    atet = round((y1_1.mean() - y1_0.mean()) - (y0_1.mean() - y0_0.mean()),0)
    atet = str(atet)
    print('The ATET is ' + atet)



def my_ols(exog, outcome, intercept=True, display=True):
    """
    OLS estimation.

    Parameters
    ----------
    exog : TYPE: pd.DataFrame
        DESCRIPTION: covariates
    outcome : TYPE: pd.Series
        DESCRIPTION: outcome
    intercept : TYPE: boolean
        DESCRIPTION: should intercept be included? The default is True.
    display : TYPE: boolean
        DESCRIPTION: should results be displayed? The default is True.

    Returns
    -------
    result: ols estimates with standard errors
    """
    # check if intercept should be included
    # the following condition checks implicitly if intercept == True
    if intercept:
        # if True, prepend a vector of ones to the covariate matrix
        exog = pd.concat([pd.Series(np.ones(len(exog)), index=exog.index,
                                    name='intercept'), exog], axis=1)
    # compute (x'x)-1 by using the linear algebra from numpy
    x_inv = np.linalg.inv(np.dot(exog.T, exog))
    # estimate betas according to the OLS formula b=(x'x)-1(x'y)
    betas = np.dot(x_inv, np.dot(exog.T, outcome))
    # compute the residuals by subtracting fitted values from the outcomes
    res = outcome - np.dot(exog, betas)
    # estimate standard errors for the beta coefficients
    # se = square root of diag((u'u)(x'x)^(-1)/(N-p))
    s_e = np.sqrt(np.diagonal(np.dot(np.dot(res.T, res), x_inv) /
                              (exog.shape[0] - exog.shape[1])))
    # compute the t-values
    tval = betas / s_e
    # compute pvalues based on the students t-distribution (requires scipy)
    # sf stands for the survival function (also defined as 1 - cdf)
    pval = stats.t.sf(np.abs(tval),
                      (exog.shape[0] - exog.shape[1])) * 2
    # put results into dataframe and name the corresponding values
    result = pd.DataFrame([betas, s_e, tval, pval],
                          index=['coef', 'se', 't-value', 'p-value'],
                          columns=list(exog.columns.values)).transpose()
    # check if the results should be printed to the console
    # the following condition checks implicitly if display == True
    if display:
        # if True, print the results (\n inserts a line break)
        print('OLS Estimation Results:', '-' * 80,
              'Dependent Variable: ' + outcome.name, '-' * 80,
              round(result, 2), '-' * 80, '\n\n', sep='\n')

    


# define an Output class for simultaneous console - file output
class Output():
    """Output class for simultaneous console/file output."""

    def __init__(self, path, name):

        self.terminal = sys.stdout
        self.output = open(path + name + ".txt", "w")

    def write(self, message):
        """Write both into terminal and file."""
        self.terminal.write(message)
        self.output.write(message)

    def flush(self):
        """Python 3 compatibility."""

