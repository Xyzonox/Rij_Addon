# Rij_Addon
A blender addon that quickly sets an array to whatever selected and on command separates by loose parts, moves origin to volume on each part, and applies a rigid body
For the code, it's not too complicated 

For Use"

  install the Addon
 
  Select an object (only something that can use the Array Modifier)

  Press f3 and search "Rij Array"

  Edit offsets and count

  Press Execute and click somewhere on 3d viewport

  The code can also work backwards by unapplying the array modifiers and joining the geometry by unchecking execute but that was an accident and might now work properly in certain scenarios


For the Code:

  Specifically, it adds 3 array modifiers to a selected object named "Rad Mod1" "Rad Mod2" "Rad Mod3".
The values for the x offset for Rad Mod1, y offset for Rad Mod2, and z offset for Rad Mod3 are connected to properties x y z respectively.
Then there is an if statement to where a variable equals True then run apply, separate, and add rigid body commands.

Notice how each modifier equals its variable with side. in front? That's just a way to connected those values to the pop up properties menu
In the beginning of the code.
