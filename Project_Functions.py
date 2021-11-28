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
import os

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
    

def organize(data, value, drop_values, column_names):
    test = data[value] # decide which key of dictionary to use
    test = test.head(2) # only keep first two rows
    test = test.dropna(axis = 1) # drop all columns with nan values
    test = test.drop(test[drop_values], axis = 1) # drop unnecessary columns
    test = test.drop(0) # drop row 0
    test.columns = column_names # define column names
    return test
 


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

