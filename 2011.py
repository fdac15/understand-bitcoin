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




data = (41, 37, 31, 27, 23, 20, 17, 17, 16, 16, 14, 14, 13, 12, 12, 12, 11, 11, 10, 10, 9, 9, 9, 9, 9, 8, 8, 8, 8, 7)
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
plt.title('Files modified in 2011')
plt.xticks(index+bar_width, ('src/net.cpp', 'src/main.cpp', 'bitcoin-qt.pro', 'src/rpc.cpp', 'src/bitcoinrpc.cpp', 'src/qt/transactiontablemodel.cpp', 'src/ui.cpp', 'src/wallet.cpp', 'src/qt/bitcoingui.cpp', 'src/qt/bitcoinamountfield.cpp', 'src/util.h', 'src/db.cpp', 'src/net.h', 'src/qt/forms/sendcoinsdialog.ui', 'src/qt/bitcoin.cpp', 'doc/release-process.txt', 'src/headers.h', 'src/util.cpp', 'src/qt/transactionrecord.h', 'src/serialize.h', 'src/makefile.osx', 'doc/build-unix.txt', 'src/script.cpp', 'src/qt/clientmodel.h', 'src/makefile.unix', 'src/init.cpp', 'doc/assets-attribution.txt', 'contrib/gitian.yml', 'src/ui.h', 'src/makefile.mingw'), rotation='vertical')
plt.legend()

plt.tight_layout()
plt.show()