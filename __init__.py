# To use this add-on you have to zip the directory containing this file (cityGen)
# and install the zip in the .blend file.
# To install the add-on open your .blend file and go to Edit -> Preferences -> Add-ons -> Install.
# Navigate to the directory where the zip-file is located that contains the cityGen directory and select it.
# The add-on should now listed and you have to enable it by clicking the checkbox.
# If you don't see it, select User in the dropdown.
# When enabled, you can use it in the 3D Viewport Object Mode.


bl_info = {
    "name": "CityGen",
    "author": "Alexander Junger",
    "version": (1, 0),
    "blender": (3, 6, 12),
    "location": "View3D > Toolbar > CityGen",
    "category": "Object",
    "description": "Generate a procedural city."
}


# ------------------------------------------------------------------------
#    Imports
# ------------------------------------------------------------------------


import bpy
import os
import sys


# Make sure imports work even when main folder is named differently
if __name__ != "cityGen":
    sys.modules["cityGen"] = sys.modules[__name__]

dir = os.path.dirname(os.path.abspath(__file__))

if dir not in sys.path:
    sys.path.append(dir)

from . import roadGen, roadNetGen

from .operators import CG_CreateAll, CG_DeleteAll
from .properties import CG_CityProperties


# ------------------------------------------------------------------------
#    Panel in Object Mode
# ------------------------------------------------------------------------


class CG_CityGenPanel(bpy.types.Panel):
    bl_label = "City Generation"
    bl_idname = "cityGen_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "CityGen"
    bl_context = "objectmode"

    def draw(self, context):
        city_props = context.scene.city_props
        layout = self.layout

        layout.prop(city_props, "graph_width")
        layout.prop(city_props, "graph_height")
        layout.prop(city_props, "graph_seed")
        layout.prop(city_props, "crossroad_offset")
        layout.operator("cg.create_all")
        layout.operator("cg.delete_all")


# ------------------------------------------------------------------------
#    Registration of Operators and Panel
# ------------------------------------------------------------------------


classes = (
    CG_CityGenPanel,
    CG_CityProperties,
    CG_CreateAll,
    CG_DeleteAll
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.city_props = bpy.props.PointerProperty(type=CG_CityProperties)


def unregister():
    del bpy.types.Scene.city_props

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
