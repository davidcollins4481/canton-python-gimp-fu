#!/bin/python

from gimpfu import *
 
def first_plugin(timg, tdrawable):
  print "Hello, world!"
 
register(
  "hello_world",
  "Hello, World! message",
  "Hello, World! message",
  "Dave Collins",
  "Dave Collins",
  "2018",
  "<Image>/Image/Hello, World!",
  "RGB*, GRAY*",
  [],
  [],
  first_plugin)
 
main()
