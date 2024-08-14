import bpy

from .roadGen.generators.road_net_generator import RG_RoadNetGenerator
from .roadGen.utils.collection_management import delete_collections_with_objects, hide_collection
from .roadGen.utils.curve_management import visible_curves
from .roadNetGen.roadNetGen import generate


# ------------------------------------------------------------------------
#    Operators
# ------------------------------------------------------------------------


class CG_CreateAll(bpy.types.Operator):
    """Create a road net and its roads, kerbs, crossroads and sidewalks"""
    bl_label = "Create All"
    bl_idname = "cg.create_all"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        generate()

        curves = visible_curves()
        road_net_generator = RG_RoadNetGenerator(curves)
        road_net_generator.generate()

        hide_collection("Markers")

        return {"FINISHED"}


class CG_DeleteAll(bpy.types.Operator):
    """Delete the road net, all created meshes and the collections themselves"""
    bl_label = "Delete All"
    bl_idname = "cg.delete_all"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        collections = ["Crossroad Curves", "Crossroads", "Edges", "Kerbs", "Line Meshes", "Markers", "Road Lanes", "Sidewalks"]

        delete_collections_with_objects(collections)

        return {"FINISHED"}

    def invoke(self, context, event):
        wm = context.window_manager

        return wm.invoke_confirm(self, event)


# ------------------------------------------------------------------------
#    Helper Methods
# ------------------------------------------------------------------------


def show_message_box(title: str = "Message Box", message: str = "", icon: str = "INFO"):
    def draw(self, context):
        self.layout.label(text=message)

    bpy.context.window_manager.popup_menu(draw, title=title, icon=icon)
