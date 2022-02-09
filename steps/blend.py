from behave import *

import os


from xdocz_helpers import *

# Useful when using "Examples:" tables
use_step_matcher("parse")


@given('I put "{thing}" in a blender')
def step_given_put_thing_into_blender(context, thing):
    print("fooo => ", thing, "\n")
    pass

@when('I switch the blender on')
def step_when_switch_blender_on(context):
    print("getcwd => ", os.getcwd(), "\n")
    img_path = os.path.join(os.getcwd() , "steps/test.png")
    context.attach("image/png", ImgToBase64String(img_path) )


@then('it should transform into "{other_thing}"')
def step_then_should_transform_into(context, other_thing):
    pass

