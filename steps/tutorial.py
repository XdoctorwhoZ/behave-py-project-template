from behave import *



@given('we have behave installed')
def step_impl(context):
    # print("print visible", "\n")
    pass

@when('we implement a test')
def step_impl(context):
    # print(context, "\n")
    context.attach("text/plain", "je suis un log")
    assert True is not False



