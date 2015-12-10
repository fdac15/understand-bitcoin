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




data = (83, 47, 37, 36, 25, 24, 24, 24, 22, 21, 19, 19, 18, 17, 16, 16, 16, 14, 13, 12, 12, 11, 11, 11, 11, 11, 11, 10, 9, 9)
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
plt.title('Files modified in 2013')
plt.xticks(index+bar_width, ('src/main.cpp', 'src/init.cpp', 'src/bitcoinrpc.cpp', 'src/net.cpp', 'src/wallet.cpp', 'src/qt/locale/bitcoin_en.ts', 'configure.ac', 'bitcoin-qt.pro', 'src/qt/paymentserver.cpp', 'src/qt/bitcoingui.cpp', 'src/qt/bitcoin.cpp', 'src/util.h', 'src/net.h', 'src/test/transaction_tests.cpp', 'src/util.cpp', 'src/miner.cpp', 'src/rpcwallet.cpp', 'src/qt/guiutil.cpp', 'doc/release-process.md', 'README.md', 'src/qt/bitcoinamountfield.cpp', 'src/test/data/script_valid.json', 'src/bitcoind.cpp', 'src/main.h', 'doc/build-unix.md', 'src/key.cpp', 'src/qt/walletview.cpp', 'src/walletdb.cpp', 'src/core.h', 'src/qt/locale/bitcoin_fa_IR.ts'), rotation='vertical')
plt.legend()

plt.tight_layout()
plt.show()