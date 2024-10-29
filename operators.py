import bpy

from cityGen import config
from cityGen.roadGen.generators.road_net_generator import RG_RoadNetGenerator
from cityGen.roadGen.utils.collection_management import delete_collections_with_objects, switch_collections_visibility
from cityGen.roadGraphGen.roadGraphGen import RNG_GraphGenerator


# ------------------------------------------------------------------------
#    Operators
# ------------------------------------------------------------------------


class CG_CreateAll(bpy.types.Operator):
    """Create a road net and its roads, kerbs, crossroads and sidewalks"""
    bl_label = "Create All"
    bl_idname = "cg.create_all"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        city_props = context.scene.city_props
        graph_width = city_props.graph_width
        graph_height = city_props.graph_height
        graph_seed = city_props.graph_seed

        graph_generator = RNG_GraphGenerator(graph_width, graph_height, graph_seed)
        graph_generator.generate()

        graph = graph_generator.graph

        config.road_net_generator = RG_RoadNetGenerator(graph)
        config.road_net_generator.generate()

        collection_names = ["Crossing Points", "Crossroad Curves", "Line Meshes"]

        switch_collections_visibility(collection_names)

        return {"FINISHED"}


class CG_DeleteAll(bpy.types.Operator):
    """Delete the road net, all created meshes and the collections themselves"""
    bl_label = "Delete All"
    bl_idname = "cg.delete_all"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        collection_names = ["Crossing Points", "Crossroad Curves", "Crossroads", "Curves", "Kerbs", "Line Meshes", "Road Lanes",
                            "Sidewalks", "Street Lamps", "Street Name Signs", "Traffic Lights", "Traffic Signs", "Vehicles"]

        delete_collections_with_objects(collection_names)

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
