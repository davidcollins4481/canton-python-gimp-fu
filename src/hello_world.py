
from gimpfu import *
 
def first_plugin(timg, tdrawable):
  """
  :type timg: gimp.Image
  :type tdrawable: gimp.Layer
  """
  print "Hello, world!"
 
register(
  "hello_world",
  "Blurb",
  "Here is my help text",
  "Dave collins",
  "copyright",
  "2018",
  "<Image>/Image/Hello, World!",
  "RGB*, GRAY*",
  [],
  [],
  first_plugin)
 
main()
