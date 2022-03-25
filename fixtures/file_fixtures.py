from behave import fixture



@fixture
def file_steeve(context, timeout=30, **kwargs):
    # -- SETUP-FIXTURE PART:
    # context.browser = FirefoxBrowser(timeout, **kwargs)
    # yield context.browser
    # -- CLEANUP-FIXTURE PART:
    # context.browser.shutdown()
    pass


@fixture
def file_john(context, timeout=30, **kwargs):
    pass
