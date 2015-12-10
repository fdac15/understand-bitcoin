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




data = (142, 118, 71, 56, 52, 48, 43, 38, 37, 32, 29, 25, 25, 24, 22, 21, 19, 17, 16, 15, 15, 15, 14, 13, 13, 12, 12, 12, 11, 11)
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
plt.title('Files modified in 2012')
plt.xticks(index+bar_width, ('src/main.cpp', 'src/bitcoinrpc.cpp', 'src/net.cpp', 'src/db.cpp', 'src/init.cpp', 'src/qt/bitcoingui.cpp', 'bitcoin-qt.pro', 'src/netbase.cpp', 'src/util.cpp', 'src/util.h', 'src/qt/bitcoin.cpp', 'src/qt/optionsmodel.cpp', 'src/qt/qtipcserver.cpp', 'src/wallet.cpp', 'src/qt/locale/bitcoin_en.ts', 'src/net.h', 'src/rpcwallet.cpp', 'src/qt/optionsdialog.cpp', 'src/main.h', 'src/script.cpp', 'src/qt/rpcconsole.cpp', 'doc/release-process.txt', 'src/qt/bitcoingui.h', 'src/makefile.osx', 'src/qt/forms/rpcconsole.ui', 'src/qt/locale/bitcoin_eu_ES.ts', 'src/serialize.h', 'src/qt/guiutil.cpp', 'src/qt/walletmodel.cpp', 'doc/release-notes.txt'), rotation='vertical')
plt.legend()

plt.tight_layout()
plt.show()