"""
This module is used to execute others in this project.

Thank you for the good startin point:
https://coderwall.com/p/w78iva/give-your-python-program-a-shell-with-the-cmd-module

"""
import sys
import time

# Dependency Check for Python Version - at the very beginning before hitting any code that is not supported in 3.x
req_python_version = (2, 7, 3)
cur_python_version = sys.version_info

print ("\nVerifying core dependency - Python ...\n")
time.sleep(1)

if cur_python_version >= req_python_version and cur_python_version.major == 2:
    print ("Python Version" + sys.version + "\n\nVerified you are running a supported Python version.")
    time.sleep(1)
else:
    print("You are running an unsupported version of Python. Supported version is Python 2.7.3. " +
                                "\nPlease visit : http://www.python.org/download/releases/2.7/")
    print("\nInstall the supported version and try again ... Exiting installation.\n")
    sys.exit()

#Import Python Libraries in this section 



################################################################################
###### Utility functions #######################################################
################################################################################

def function_installation_exit(msg=""):
    print ("\nInstallation will now exit: " + msg + "\n")
    sys.exit()
    
    

################################################################################
###### Selection functions ##################################################
################################################################################
def selection_sorting_uniqueness():

    print ('\nYou selected sorting uniqueness. Function will run here ... \n')

def selection_sum_numbers():

    print ('\nYou selected sum of numbers. Function will run here ... \n')

#############################################################################
##    MAIN
#############################################################################

### Processing user interaction commands ###
options = {
    1: selection_sorting_uniqueness,
    2: selection_sum_numbers,
}

menu_item = 0
option_inst = ""
while True:

    print("")
    print("1. Sorting")
    print("2. Sum of Numbers")

    print("")
    option_input = str(raw_input("Select an option from the list above, or type 'q' to quit: " + option_inst))

    if option_input == 'q':
        function_installation_exit(" You selected to end the installation.")

    try:
        int(option_input)
        menu_item = int(option_input)
    except ValueError:
        menu_item = 0

    if menu_item in (1, 2):
        options[menu_item]()
        sys.exit()
    else:
        option_inst = "(select a number from list) "
        continue
