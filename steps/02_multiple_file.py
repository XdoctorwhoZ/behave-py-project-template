import os
from behave import *

###############################################################################
###############################################################################

# Required to parse arguments in steps, for example "{thing}"
use_step_matcher("parse")

###############################################################################
###############################################################################

@when('we join the filename "{file}" to the directory path')
def foo_1(context, file):
    # Create the file path using the path provided by the first step
    context.filepath = os.path.join(context.cwd, file)

###############################################################################
###############################################################################

