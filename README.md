# Dynamic Window Generator

Dynamic Window Generator is a modification for Creatures Docking Station. It sets up a CAOS function that can be called to generate a window of any size that can be used as a background to display text, options, etc.

After setup, it can be called with the line:
`sets va00 caos 0 0 200 200 game "f_DWG" 0 0 va99`
This will set va00 to the string name of an EAME variable pointing to the newly created 200x200 px window with the default skin and default classifier.

This is the simplest form of usage, but additional parameters may be passed through if you first set them in NAME variables of the agent that you are calling the function from: 

* dwg-fmly (integer): Specify the family classification of the window
* dwg-gnus (integer): Specify the genus classification of the window
* dwg-spcs (integer): Specify the species classification of the window
* dwg-skin (string): Specify the name of the skin you wish to use. The default skin is "dwg_default". Other skins can be added via the Skins Manager agent.
* dwg-border (string): Specify the name of the border skin you wish to use, if it is different than the skin. Note that if these are incompatible, the default skin will be used. You may also specify "none"
* dwg-tint-red/green/blue/rotation/swap (integer): Specify a tint for the window. Please don't do this too much. Your world files will be so, so big.

The newly generated background agent will be created with script 1022 on it, the "binding" script. You can mesg writ this script from the agent that you wish to bind. Once bound, the background will float relative to that agent and also kill itself if that agent no longer exists.