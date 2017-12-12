import numpy as np
import matplotlib.pyplot as plt

#error = ('isocontour', 'Error') 
error = ('histogram', 'EMD')
#error = ('rmse', 'PSNR')

for dataset in ['miranda-viscosity']:

    def Read_Two_Column_File(file_name):
        with open(file_name, 'r') as data:
            x = []
            y = []
            chunksStarted = False
            for line in data.readlines():
                if line.startswith('Bytes'):
                    chunksStarted = True
                elif chunksStarted:
                    p = line.split()
                    x.append(float(p[0]))
                    y.append(float(p[1]))

        return x, y

    fig, ax = plt.subplots()

    x, y = Read_Two_Column_File('error-' + error[0] + '-stream-' + error[0] + '-greedy-optimal-fine-to-coarse-' + dataset + '.txt')
    ax.plot(x, y, label='fine-to-coarse greedy')
    x, y = Read_Two_Column_File('error-' + error[0] + '-stream-'  + error[0] + '-greedy-optimal-' + dataset + '.txt')
    ax.plot(x, y, label='coarse-to-fine greedy')
    x, y = Read_Two_Column_File('error-' + error[0] + '-stream-'  + error[0] + '-greedy-' + dataset + '.txt')
    ax.plot(x, y, label='initial sort only')

    ax.legend(loc='lower right')
    ax.set_xlabel('Number of Streamed Bytes', fontsize=14)
    ax.set_ylabel(error[1], fontsize=14, rotation='horizontal', horizontalalignment='right') # the files are though named as RMSE

    # hide top and right axis
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

    fig.tight_layout()
    fig.savefig(error[0] + '-' + dataset + '.svg')
    fig.savefig(error[0] + '-' + dataset + '.pdf')
