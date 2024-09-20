"""Log random points and the corresponding covariance ellipsoid."""

import rerun
from numpy import array, random

rerun.init("rerun_example_ellipsoid_simple", spawn=True)

center = array([0, 0, 0])
sigmas = array([5, 3, 1])
point_locations = random.randn(50_000, 3) * sigmas.reshape(1, -1)
points = rerun.Points3D(point_locations, radii=0.02, colors=[188, 77, 185])

rerun.log("points", points)
rerun.log(
    "ellipsoid",
    rerun.Ellipsoids3D(centers=[center, center], half_sizes=[sigmas, 3 * sigmas], colors=[[255, 255, 0], [64, 64, 0]])
)
