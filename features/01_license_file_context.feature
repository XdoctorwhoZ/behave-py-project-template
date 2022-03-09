Feature: The project must have a LICENSE file with context

    Scenario: Check the file existence with context
        Given we are in the working directory
        When we join the filename to the directory path
        Then the file must exist
