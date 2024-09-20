
import rerun
from numpy import linspace, uint8, zeros

rerun.init("rerun_example_my_data", spawn=True)

positions = zeros((10, 3))
positions[:, 0] = linspace(-10, 10, 10)

colors = zeros((10, 3), dtype=uint8)
colors[:, 2] = linspace(0, 255, 10)

points = rerun.Points3D(positions, colors=colors, radii=0.25)
rerun.log("my_points", points)
