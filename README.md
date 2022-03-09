# Python Behave: Tests Project Template

This repository aims to provides a template and a cheat sheet for tests project using python behave.

## Dependencies

```bash
# Install from the github to get the lastest cool features
pip install git+https://github.com/behave/behave
# Install the html formater, for your bosses :-)
pip install behave-html-formatter
```

## Just run behave

This project is already prepared to be used like this. To check that your setup is correct, let's just run the project.

```bash
# just run the command behave
behave

# To get the html report
source html.sh
# which is in fact behave command with args 'behave -f html -o report.html'
```

## 00 License File

This feature is the most basic feature you can create.

It is composed of the feature declaration.

```gherkin
Feature: The project must have a LICENSE file
```

And the scenario to test the feature. The scenario is composed of 2 steps.

```gherkin
    Scenario: Check the file existence
        Given we are in a directory
        Then the LICENSE file exists
```

Behave links step texts to python functions in 00_LICENSE_file.py.

```python
@given('we are in a directory')
def we_are_in_a_directory(context):
    # Just get the current path
    cwd = os.getcwd()

    # To print do not forget the "\n" at the end
    print(f"Current directory: {cwd}", "\n")
    
    # Check if the path is a directory, else the test fails
    assert os.path.isdir(cwd) == True
```

Notes:

- @given is the decorator used by behave to link step text and python function
- The keywords (given/then) are not part of the step text
- To print inside a step do not forget the \n
- To perform verification use asserts

## 01 License File Context

The second example is the same as the first but it introduces the use of the 'context'.
The context can hold variables across steps of the same scenario.

For example, the first step stores the current working dir path into the context.

```python
@given('we are in the working directory')
def foo_0(context):
    # Store the current directory into the scenario context
    context.cwd = os.getcwd()
```

And the second step use it.

```python
@when('we join the filename to the directory path')
def foo_1(context):
    # Here you can use the context.cwd of the first step
    context.filepath = os.path.join(context.cwd, 'LICENSE')
```

## 02 Multiple Files Check

Now we are in the case we want to check if multiple files are in the working directory.
But all the actions of the steps are the same at the exception of the name of the file.
It would be painful to create a new scenario for each file.

```gherkin
    Scenario: Check the existence of the file LICENSE
        Given we are in the working directory
        When we join the filename LICENSE to the directory path
        Then the file must exist

    Scenario: Check the existence of the file README.md
        Given we are in the working directory
        When we join the filename README.md to the directory path
        Then the file must exist

    ...
```

To solve this problem you can use **Scenario Outline**. With this tool, you can create *variables* into your scenarios and steps.

```gherkin
    Scenario Outline: Check the existence of the file "<file>"
        Given we are in the working directory
        When we join the filename "<file>" to the directory path
        Then the file must exist

        Examples: Basic files
        | file          |
        | LICENSE       |
        | README.md     |
```

Then you can create a step that can adapt itself to the input file name.

```python
# Required to parse arguments in steps, for example "{thing}"
use_step_matcher("parse")

@when('we join the filename "{file}" to the directory path')
def foo_1(context, file):
    # Create the file path using the path provided by the first step
    context.filepath = os.path.join(context.cwd, file)
```

**Warning** The scenario will be entirely run for each line of the table

