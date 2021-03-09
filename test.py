#!/usr/bin/env python
# coding=utf-8

import argparse
import time
import msgpack
from enum import Enum, auto

import numpy as np

from planning_utils import a_star, heuristic, create_grid
from udacidrone import Drone
from udacidrone.connection import MavlinkConnection
from udacidrone.messaging import MsgID
from udacidrone.frame_utils import global_to_local

# TODO: read lat0, lon0 from colliders into floating point values
lat0 = 37.792480
lon0 = -122.397450
# TODO: set home position to (lon0, lat0, 0)
current_home = [self.global_position[lon0], self.global_position[lat0], self.global_position[0]]
self.set_home_position(current_home)
# TODO: retrieve current global position
current_global = self.global_position
# TODO: convert to current local position using global_to_local()
current_local = global_to_local(current_global, current_home)
print('global home {0}, position {1}, local position {2}'.format(self.global_home, self.global_position, self.local_position))
