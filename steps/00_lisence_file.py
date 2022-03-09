import os
from behave import *

###############################################################################
###############################################################################

@given('we are in a directory')
def we_are_in_a_directory(context):
    # Just get the current path
    cwd = os.getcwd()

    # To print do not forget the "\n" at the end
    print(f"Current directory: {cwd}", "\n")
    
    # Check if the path is a directory, else the test fails
    assert os.path.isdir(cwd) == True

###############################################################################
###############################################################################

@then('the LICENSE file exists')
def the_LICENSE_file_exists(context):
    # Create the file path
    filepath = os.path.join(os.getcwd(), 'LICENSE')

    # To print do not forget the "\n" at the end
    print(f"Path of the file LICENSE: {filepath}", "\n")
    
    # Check if the path is a file, else the test fails
    assert os.path.isfile(filepath) == True


