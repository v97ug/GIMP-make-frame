#!/usr/bin/python
# coding: UTF-8

from gimpfu import *

def frame(image, drawable, shrink_pixcel, fill_pattern):
    pdb.gimp_selection_all(image) #アンダーバー注意！！
    pdb.gimp_selection_shrink(image, shrink_pixcel)
    pdb.gimp_selection_invert(image)
    pdb.gimp_edit_fill(drawable, fill_pattern)


register(
        proc_name = "python_fu_make_frame",
        blurb = "写真のフレームを作る",
        help = "写真のフレームを作る",
        author = "v97ug",
        copyright = "v97ug",
        date = "2017",
        label = "<Image>/MyPlugin/make frame",
        imagetypes = "*",
        params = [
            (PF_SPINNER, "shrink_pixcel", "Shrink selection by", 10, (0, 255, 1)),
            (PF_RADIO, "fill_pattern", "How fill?", 0, (("FG color",0), ("BG color",1), ("Pattern",4)) ),
        ],
        results = [],
        function = frame)

main()