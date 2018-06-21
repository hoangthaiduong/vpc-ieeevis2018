import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import sys

if len(sys.argv) != 3:
  print(sys.argv)
  print('Args: [text file with data] [output text file]')
  exit()

#arr = np.loadtxt(sys.argv[1], dtype='float64')
arr = np.fromfile(sys.argv[1], dtype='float64')
#minval = np.amin(arr)
#maxval = np.amax(arr)
#print(minval, maxval)
clipmin = 2.35119856917e-09
clipmax = 0.137855529785
cliparr = np.clip(arr, clipmin, clipmax)

# the histogram of the data
fig, ax = plt.subplots()
n, bins, patches = ax.hist(cliparr, 64, edgecolor='black', linewidth=0.5, color='#B2DF89', alpha=1)

# add a 'best fit' line
#y = mlab.normpdf( bins, mu, sigma)
#l = plt.plot(bins, y, 'r--', linewidth=1)

#plt.xlabel('Smarts')
#plt.ylabel('', fontsize=20)
plt.setp(ax.get_yticklabels(), fontsize=18)
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off
#plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
#plt.axis([40, 160, 0, 0.03])
#plt.grid(True)
fig.tight_layout()
fig.savefig(sys.argv[2]+'.pdf')

plt.show()
