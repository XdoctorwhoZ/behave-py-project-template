import os
from behave import *

###############################################################################
###############################################################################

@given('we are in the working directory')
def foo_0(context):
    # Store the current directory into the scenario context
    context.cwd = os.getcwd()

###############################################################################
###############################################################################

@when('we join the filename to the directory path')
def foo_1(context):
    # Create the file path using the path provided by the first step
    context.filepath = os.path.join(context.cwd, 'LICENSE')

###############################################################################
###############################################################################

@then('the file must exist')
def foo_2(context):
    # Check if the path is a file, else the test fails
    assert os.path.isfile(context.filepath) == True

    # Attach text to the final report with context
    context.attach("text/plain", context.filepath)
