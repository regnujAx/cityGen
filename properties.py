import bpy


# ------------------------------------------------------------------------
#    Properties
# ------------------------------------------------------------------------


class CG_CityProperties(bpy.types.PropertyGroup):
  graph_seed : bpy.props.IntProperty(
    name="Graph Seed",
    description="Seed for graph generation (between 10000 and 100000000)",
    soft_min=10000,
    soft_max=100000000,
    default=12345678
  )

  crossroad_offset : bpy.props.FloatProperty(
    name="Crossroad Offset",
    description="Offset for crossroads (between 2.0 and 1000.0 in meters)",
    soft_min=2.0,
    soft_max=1000.0,
    default=8.0
  )
