#!/usr/bin/env python3 
from numpy import * 
from matplotlib import *
import matplotlib.pyplot as plt
from numpy.random import *

"""
    Bar chart demo with pairs of bars grouped for easy comparison.
    """
import numpy as np
import matplotlib.pyplot as plt




data = (13480, 7503, 2301, 885, 826, 722, 487, 484, 435, 420, 348, 339, 337, 290, 233, 218, 216, 146, 145, 133, 132, 124, 113, 107, 94, 92, 87, 84, 72, 71)
n_groups = len(data)
fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.5

opacity = 0.4

rects1 = plt.bar(index, data, bar_width,
                 alpha=opacity,
                 color='b')

plt.xlabel('Files')
plt.ylabel('Number of files changed')
plt.title('Files modified 2009-2015')
plt.xticks(index+bar_width, ('.cpp', '.h', '.ts', '.png', '.md', '.py', '.yml', '.ui', '.txt', '.am', '.cc', '.json', '.sh', '.m4', '.mk', '.ac', '.pro', '.unix', '.gitignore', '.osx', '.mingw', '.xpm', '.linux', '.svg', '.c', '.qrc', '.bmp', '.test', '.nsi', '.qt'), rotation='vertical')
plt.legend()

plt.tight_layout()
plt.show()