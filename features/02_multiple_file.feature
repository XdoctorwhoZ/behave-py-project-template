Feature: The project must have mutiple files

    Scenario Outline: Check the existence of the file "<file>"
        Given we are in the working directory
        When we join the filename "<file>" to the directory path
        Then the file must exist

        Examples: Basic files
        | file          |
        | LICENSE       |
        | README.md     |

        Examples: Behave files
        | file              |
        | behave.ini        |
        | environment.py    |
