import rerun
from numpy import linspace, meshgrid, uint8, vstack, zeros

rerun.init("rerun_example_my_data", spawn=True)

SIZE = 10

position_grid = meshgrid(*[linspace(-10, 10, SIZE)] * 3)
positions = vstack([d.reshape(-1) for d in position_grid]).T

color_grid = meshgrid(*[linspace(0, 255, SIZE)] * 3)
colors = vstack([c.reshape(-1) for c in color_grid]).astype(uint8).T

points = rerun.Points3D(positions, colors=colors, radii=0.25)
rerun.log("my_points", points)
