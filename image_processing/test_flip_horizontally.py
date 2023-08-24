import image_processing_solution as ips
import numpy as np


c = np.random.rand(10, 12, 3)

expected = ips.flip_horizontally(c)
actual = flip_horizontally(c)

if np.array_equal(expected, actual):
	print("flip_horizontally")

