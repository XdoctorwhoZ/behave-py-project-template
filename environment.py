from behave import *
from behave.fixture import use_fixture_by_tag

from .fixtures.file_fixtures import file_john, file_steeve

#
fixture_registry = {
    "fixture.file.john":  file_john,
    "fixture.file.steeve": file_steeve,
}


def before_all(context):
    context.IMAGE_NAME = "test.png"


def before_tag(context, tag):
    if tag.startswith("fixture."):
        return use_fixture_by_tag(tag, context, fixture_registry)
