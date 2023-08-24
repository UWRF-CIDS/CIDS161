import image_processing_solution as ips
import numpy as np


c = np.random.rand(10, 12, 3)

expected = ips.redify(c)
actual = redify(c)

if np.array_equal(expected, actual):
	print("redify")

