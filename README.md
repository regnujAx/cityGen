# CityGen - Procedural City Generation

## What is it?
CityGen was developed as a project for a master thesis to create a [Blender](https://www.blender.org/) add-on that generates a procedural city.

At the moment it generates a road net graph (submodule [roadNetGen](https://github.com/regnujAx/roadNetGen) forked from [ProceduralCityGenerator](https://github.com/panicmod-e/ProceduralCityGenerator)) and based on this a road net with Blender meshes (submodule [roadGen](https://github.com/regnujAx/roadGen)).

The road net graph is generated procedurally, but it is possible to use a seed to generate the same graph each time.

The implementation is written in Python to enable the integration of the generation with Blender's Python API.


## How can I use it as a Blender add-on?
To use this project as a Blender add-on, follow these steps:

1. Clone the repository:
```shell
git clone https://github.com/regnujAx/cityGen.git
```

2. Update the submodules:
```shell
git submodule update
```

3. Zip the whole cityGen directory.

4. Install the zip in a Blender file.
- Open your .blend file and go to Edit &rarr; Preferences &rarr; Add-ons &rarr; Install.
- Navigate to the directory where the zip-file is located that contains the cityGen directory and select it.
- The add-on should now listed.
- If you don't see it, select User in the dropdown and/or use the search function.
- If you see it and it is not enable, enable it by clicking on the checkbox.
- When enabled, you can use it in the 3D Viewport Object Mode.