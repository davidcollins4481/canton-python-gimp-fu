
from gimpfu import *
 
def rotate(timg, tdrawable, layer_count=10, blur_amount=.1):
    """
    :type timg: gimp.Image
    :type tdrawable: gimp.Layer
    """
    pdb.gimp_undo_push_group_start(timg)

    i = 0
    starting_opacity = 70.0
    rotation_increment = blur_amount
    current_rotation = .01
    tdrawable.opacity = 90.0
    while i < layer_count:
        new_layer = tdrawable.copy()  # type: gimp.Layer
        timg.add_layer(new_layer)
        new_layer.opacity = starting_opacity
        pdb.gimp_item_transform_rotate(new_layer, current_rotation, 1, 0, 0)
        i = i + 1
        current_rotation = current_rotation + rotation_increment

    timg.merge_visible_layers(1)
    pdb.gimp_undo_push_group_end(timg)


register(
  "rotator",
  "Blurb",
  "Here is my help text",
  "Dave collins",
  "copyright",
  "2018",
  "<Image>/Image/Rotate",
  "RGB*, GRAY*",
  [
    (PF_INT, "layer_count", "Layer Count", 10),
    (PF_FLOAT, "blur_amount", "Blur Amount", .1),
  ],
  [],
  rotate)
 
main()
