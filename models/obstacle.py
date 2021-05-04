import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.boundary_detection import *
from src.geometry import *
import yaml

params = yaml.load(open('params.yaml'), Loader=yaml.FullLoader)

obstacle = Shape()


# length = 0.4m, width = 0.1m
obstacle_points = [Point(-0.2, 0.05), Point(0.2, 0.05), Point(0.2, -0.05), Point(-0.2, -0.05)]

obstacle.set_center(Point(0, 0))
obstacle.set_points(obstacle_points)
obstacle = interpolate_shape(obstacle, params['model_settings']['model_interpolation'])