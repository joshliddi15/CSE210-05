import os
from os import sep, linesep

import __main__

class FSUtils():
    
    # Gets the current base folder (using os.getcwd()):
    def get_cwd(self):
        return os.getcwd()
    
    # Gets the default path seperator for the current OS (\ on PowerShell on Windows, / on Linux):
    def get_os_path_sep(self):
        return sep
    
    # Gets the line seperator for files depending on the OS:
    def get_os_linesep(self):
        return linesep