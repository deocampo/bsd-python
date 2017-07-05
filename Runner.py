"""
This module is used to execute others in this project.

Thank you for the good startin point:
https://coderwall.com/p/w78iva/give-your-python-program-a-shell-with-the-cmd-module

"""
import sys

def function_installation_exit(msg=""):
    print ("\nInstallation will now exit: " + msg + "\n")
    sys.exit()

menu_item = 0
option_inst = ""

while True:

    print("")
    print("1. Sorting")
    print("2. Sum")

    print("")
    option_input = str(raw_input("Select an option from the list above, or type 'q' to quit: " + option_inst))

    if option_input == 'q':
        function_installation_exit(" You selected to end the installation.")

    try:
        int(option_input)
        menu_item = int(option_input)
    except ValueError:
        menu_item = 0

    # Pre-installation checks: admin flag, and upgrade validation
    if menu_item == 1:
        print("Executing 1")
    if menu_item == 2:
        print("Executing 2")
    else:
        option_inst = "(select a number from list) "
        continue
