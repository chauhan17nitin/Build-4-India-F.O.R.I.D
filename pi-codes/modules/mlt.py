import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

def mlt():
	data = np.random.rand(10, 4) * 20

	# create discrete colormap
	cmap = colors.ListedColormap(['green', 'red'])
	bounds = [0,10,20]
	norm = colors.BoundaryNorm(bounds, cmap.N)


	fig, ax = plt.subplots()
	ax.imshow(data, cmap=cmap, norm=norm)

	# draw gridlines
	ax.grid(which='major', axis='both', linestyle='-', color='w', linewidth=10)
	ax.set_xticks(np.arange(-0.5, 4, 1))
	ax.set_yticks(np.arange(-0.5, 10, 1))
	ax.xaxis.set_major_formatter(plt.NullFormatter())
	ax.yaxis.set_major_formatter(plt.NullFormatter())


	plt.savefig('map.png')
