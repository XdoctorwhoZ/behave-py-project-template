
from behave import *



@given('the given part print the fixture')
def step_given_put_thing_into_blender(context):
    print("fixture => ", context.my_fixture, "\n")

@when('I change here the fixture')
def step_when_switch_blender_on(context):
    context.my_fixture = 1


@then('It changes here')
def step_then_should_transform_into(context):
    assert context.my_fixture is 1


