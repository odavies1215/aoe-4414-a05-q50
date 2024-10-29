# ray_ellipsoid_intersection.py
#
# Usage: python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z
# Finds the intersection point (if it exists) between a ray and the Earth reference ellipsoid
#
# Parameters:
# d_l_x: x-component of origin-referenced ray direction
# d_l_y: y-component of origin-referenced ray direction
# d_l_z: z-component of origin-referenced ray direction
# c_l_x: x-component offset of ray origin
# c_l_y: y-component offset of ray origin
# c_l_z: z-component offset of ray origin
#
# Output:
# l_d[0] # x-component of intersection point
# l_d[1] # y-component of intersection point
# l_d[2] # z-component of intersection point
#
# Written by Owen Davies
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

import sys  # argv
import math  # math module

# "constants"
R_E = 6378.1363  # Earth radius in km
E_E = 0.081819221456  # Earth eccentricity

# initialize script arguments
d_l_x = float('nan')  # x-component of origin-referenced ray direction
d_l_y = float('nan')  # y-component of origin-referenced ray direction
d_l_z = float('nan')  # z-component of origin-referenced ray direction
c_l_x = float('nan')  # x-component offset of ray origin
c_l_y = float('nan')  # y-component offset of ray origin
c_l_z = float('nan')  # z-component offset of ray origin

# parse script arguments
if len(sys.argv) == 7:
    d_l_x = float(sys.argv[1])
    d_l_y = float(sys.argv[2])
    d_l_z = float(sys.argv[3])
    c_l_x = float(sys.argv[4])
    c_l_y = float(sys.argv[5])
    c_l_z = float(sys.argv[6])
else:
    print("Usage: python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z")
    exit()

# calculate intersection parameters
a = d_l_x**2 + d_l_y**2 + (d_l_z**2) / (1 - E_E**2)
b = 2 * (d_l_x * c_l_x + d_l_y * c_l_y + (d_l_z * c_l_z) / (1 - E_E**2))
c = c_l_x**2 + c_l_y**2 + (c_l_z**2) / (1 - E_E**2) - R_E**2

discriminant = b**2 - 4 * a * c

if discriminant >= 0:
    d = (-b - math.sqrt(discriminant)) / (2 * a)
    if d < 0:
        d = (-b + math.sqrt(discriminant)) / (2 * a)

    if d >= 0:
        l_d = [d * d_l_x + c_l_x, d * d_l_y + c_l_y, d * d_l_z + c_l_z]
        print(l_d[0])  # x-component of intersection point
        print(l_d[1])  # y-component of intersection point
        print(l_d[2])  # z-component of intersection point
    else:
        print("No intersection: d < 0.")
else:
    print("No intersection: discriminant < 0.")
