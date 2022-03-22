import os
from behave import *
from xdocz_helpers import AttachTextLog, AttachPngImage, PathToRsc

###############################################################################
###############################################################################

# Required to parse arguments in steps, for example "{thing}"
use_step_matcher("parse")

###############################################################################
###############################################################################

@Given('an image in the rsc directory')
def step(context):
    context.path = PathToRsc(context.IMAGE_NAME)
    AttachTextLog(context, f"Path: {context.path}")

###############################################################################
###############################################################################

@Then('the image can be attached to the report')
def step(context):
    AttachPngImage(context, context.path)

