import bpy


# ------------------------------------------------------------------------
#    Properties
# ------------------------------------------------------------------------


class CG_CityProperties(bpy.types.PropertyGroup):
  graph_width : bpy.props.IntProperty(
    name="Width",
    description="Width for graph generation in meters (between 1 and 100000)",
    soft_min=1,
    soft_max=100000,
    default=100
  )

  graph_height : bpy.props.IntProperty(
    name="Height",
    description="Height for graph generation in meters (between 1 and 100000)",
    soft_min=1,
    soft_max=100000,
    default=100
  )

  graph_seed : bpy.props.IntProperty(
    name="Seed",
    description="Seed for graph generation (between 10000 and 100000000)",
    soft_min=10000,
    soft_max=100000000,
    default=12345678
  )
