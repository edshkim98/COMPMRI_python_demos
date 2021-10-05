
import numpy as np
import functions

# coordinates of slices to visualise
location = np.array([30, 40, 30])
# voxel sizes, x, y, z
spacings = np.array([1, 1, 1])
# image path
filename = 't1_icbm_normal_1mm_pn0_rf0.rawb'
# image dimensions, x, y, z
dimensions = [181, 217, 181]

# visualise slices
functions.ImageViewer(filename, dimensions, spacings, location)



