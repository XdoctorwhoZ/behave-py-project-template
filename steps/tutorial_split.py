
from behave import *

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False

