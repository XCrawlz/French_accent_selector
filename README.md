# French accent selector

This is a simple script to insert into your system's clipboard the required letter with an accent. It's designed to reproduce the layout of the classic AZERTY keyboard.

A provided Makefile allow for simple installation of required dependencies and use of the program.

## Usage:

Run 'make install' to create a dedicated virtual environment for the program and install the required dependencies, ie: pyperclip and getkey

Run 'make run-gui' to run the program with the gui.

Run 'make run' to run the program without the gui.

The selected character will be inserted in your clipboard to then be used in any writing use case.

### Layout

The layout used is designed to be as close as possible to the classic french AZERTY keyboard layout. Allowing you tu use your muscle memory from azerty while using a us qwerty keyboard.

### Similar projects

A much more complete project exist at : https://github.com/qwerty-fr/qwerty-fr
But it requires that you learn a new layout.

### licence

This software is distributed under the GNU GPL V3 license

The use of a python class and dedicated method for each character is so that you can use this as a module in a more complete interface or keyboard matrix if you need to.
