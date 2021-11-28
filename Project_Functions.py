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

