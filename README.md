# Ren-py-Monopolization
## Description
Ren'py module to provide methods for operating a Monopoly clone through Ren'py as part of gameplay
## Installation
1.Place Monopolization.py into the games root folder(Folder above the actual "game" folder containing the rpy files)
2.Put the following code at the start of the script.rpy file. (If there is already an init python at the start of the script put the "import Monopolization" inside of the init python chunk.)

init python:
    import Monopolization

3.Create a test line having a character say "[Monopolization.testme]", if the character in the script says "yup" when renpy interprets that line of code the module is loaded correctly and can be used as described in the Usage subheading
