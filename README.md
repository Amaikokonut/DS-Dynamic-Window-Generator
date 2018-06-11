# Dynamic Window Generator

Dynamic Window Generator is a modification for Creatures Docking Station. It sets up a CAOS function that can be called to generate a window of any size that can be used as a background to display text, options, etc.

After setup, it can be called with the line:
`sets va00 caos 0 0 200 200 game "f_DWG" 0 0 va99`
This will set va00 to the string name of an EAME variable pointing to the newly created 200x200 px window with the default skin and default classifier (1 6 22901).

This is the simplest form of usage, but additional parameters may be passed through if you first set them in NAME variables of the agent that you are calling the function from. **THESE ARE CURRENTLY UNTESTED and probably don't work yet.**  

* dwg-fmly (integer): Specify the family classification of the window
* dwg-gnus (integer): Specify the genus classification of the window
* dwg-spcs (integer): Specify the species classification of the window
* dwg-skin (string): Specify the name of the skin you wish to use. The default skin is "Default". Other skins can be added via the Skins Manager agent.
* dwg-border (string): Specify the name of the border skin you wish to use, if it is different than the skin. Note that if these are incompatible, the default skin will be used. You may also specify "none" **This is not yet implemented**
* dwg-tolerance (integer): Specify from 0 to any number, how many px the generator is allowed to round up to. If you don't need your window to be a perfectly exact size, setting this higher will result in a more quickly generated window that is easier on system resources. The actual resulting dimensions will be found in NAME variables of the returned agent: dwg-height/dwg-width. Note that skins and borders may have forced tolorance. Forced tolorance will also happen if your window has too many parts.
* dwg-remake (integer): If this is set to 1, the function will remake the current ownr/targ instead of creating a new agent. Used if you just need to resize a background instead of making a whole new one.