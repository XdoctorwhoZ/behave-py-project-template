Feature: blenders outlines

    Scenario Outline: Blenders
        Given I put "<thing>" in a blender
        when I switch the blender on
        then it should transform into "<other thing>"

        Examples: Amphibians
        | thing         | other thing |
        | Red Tree Frog | mush        |

        Examples: Consumer Electronics
        | thing         | other thing |
        | iPhone        | toxic waste |
        | Galaxy Nexus  | toxic waste |

