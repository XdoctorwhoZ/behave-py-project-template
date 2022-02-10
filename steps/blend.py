import os
from behave import *
from xdocz_helpers import *

###############################################################################
###############################################################################

# Required to parse arguments in steps, for example "{thing}"
use_step_matcher("parse")

###############################################################################
###############################################################################

@given('I put "{thing}" in a blender')
def step_given_put_thing_into_blender(context, thing):
    print("this is a print => ", thing, "\n")

###############################################################################
###############################################################################

@when('I switch the blender on')
def step_when_switch_blender_on(context):
    print("current directory => ", os.getcwd(), "\n")
    img_path = os.path.join(os.getcwd() , "steps/test.png")
    context.attach("image/png", ImgToBase64String(img_path) )

###############################################################################
###############################################################################

@then('it should transform into "{other_thing}"')
def step_then_should_transform_into(context, other_thing):
    # do nothing
    pass

