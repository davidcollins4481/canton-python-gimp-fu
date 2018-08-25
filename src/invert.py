#!/usr/bin/python

from gimpfu import *

def invert(image, glayer):
    pdb.gimp_undo_push_group_start(image)
    map(lambda layer: pdb.gimp_invert(layer), image.layers)
    pdb.gimp_undo_push_group_end(image)

register(
    "dave_invert_layer",
    "A trivial plugin to Invert all of the layers in an image",
    "A trivial plugin to Invert all of the layers in an image",
    "Dave Collins",
    "No copyright",
    "2018",
    "<Image>/Image/Invert All Layers",
    "RGB*,GRAY*",
    [],
    [],
    invert
)

main()
