# Python Behave: Tests Project Template

This repository aims to provides a template and a cheat sheet for tests project using python behave.

## Dependencies

```bash
# Install from the github to get the lastest cool features
pip install git+https://github.com/behave/behave
# Install the html formater, for your bosses :-)
pip install behave-html-formatter
```

## Simple getting started

- Write your features in the **features** directory
- Write your python steps in the **steps** directory (DO NOT REMOVE **xdocz_helpers.py** USE IT !!!)

Features and steps can be splitted in multiple files.

```bash
# just run the command behave
behave

# To get the html report
source html.sh
# behave -f html -o report.html
```

