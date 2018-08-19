# Automating GIMP with Python

## Outline
- GIMP-Python (Python-Fu) and Script-Fu
- What is possible with Python in GIMP?
    - automating actions
    - interfacing with GIMPs internal procedures
    - interfacing with other plugins
- PDB
- Hello World
- Automating multiple actions
    - Grouping and Multiple undos
- Effects
- Batch processing
    - watermark many issues


## Script-Fu vs Python-Fu

GIMP-Python is a scripting extension for GIMP, similar to Script-Fu. The main difference is in what is called first. In Script-Fu, the script-fu plug-in executes the script, while in GIMP-Python the script is in control.

Differences between the two:
- In Script-Fu the Script-Fu plug-in executes the script while in GIMP-Python (Python-Fu) the script is in control
- GIMP-Python (Python-Fu) and Script-Fu is that GIMP-Python stores images, layers, channels and other types as objects rather than just storing their ID. This allows better type checking that is missing from Script-Fu, and allows those types to act as objects, complete with attributes and methods.
- GIMP-Python is not limited to just calling procedures from the PDB. It also implements the rest of libgimp , including tiles and pixel regions, and access to other lower level functions.





### Resources
[Script-Fu vs Python-Fu](https://www.gimp.org/docs/python/index.html)
[GIMP PDB](https://www.gimp.org/docs/scheme_plugin/)
