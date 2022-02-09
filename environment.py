from behave import *
from behave.fixture import use_fixture_by_tag


@fixture
def custom_fixture_1(context, timeout=30, **kwargs):
    """
    Use fixture to inject your variables across tests
    """
    try:
        context.my_fixture = "foo_value_1"
        yield
        # -- NORMAL FIXTURE-CLEANUP PART: NOT_REACHED due to setup-error.
    finally:
        print("END OF FIXTURE", "\n")
        context.my_fixture=None  # -- CLEANUP: When generator-function is left.


fixture_registry = {
    "fixture.custom.one": custom_fixture_1
}


def before_tag(context, tag):
    if tag.startswith("fixture."):
        return use_fixture_by_tag(tag, context, fixture_registry)

