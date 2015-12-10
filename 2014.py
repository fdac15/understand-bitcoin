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




data = (153, 87, 57, 55, 42, 41, 39, 39, 36, 36, 33, 32, 24, 23, 23, 22, 21, 20, 20, 20, 20, 20, 19, 19, 18, 18, 18, 17, 17, 16)
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
plt.title('Files modified in 2014')
plt.xticks(index+bar_width, ('src/main.cpp', 'configure.ac', 'src/net.cpp', 'src/chainparams.cpp', 'src/init.cpp', 'src/rpcserver.cpp', 'src/qt/optionsmodel.cpp', 'src/netbase.cpp', 'src/wallet.cpp', 'doc/build-unix.md', 'src/rpcwallet.cpp', 'src/miner.cpp', 'src/net.h', 'doc/build-osx.md', 'src/qt/bitcoin.cpp', 'src/serialize.h', 'src/rpcblockchain.cpp', 'src/rpcnet.cpp', 'src/test/transaction_tests.cpp', 'qa/rpc-tests/util.py', 'doc/release-process.md', 'src/bitcoin-tx.cpp', 'src/qt/locale/bitcoin_en.ts', 'src/test/data/script_valid.json', 'src/rpcserver.h', 'src/qt/paymentserver.cpp', 'src/util.cpp', 'src/qt/walletmodel.cpp', 'src/rpcmisc.cpp', 'src/txmempool.cpp'), rotation='vertical')
plt.legend()

plt.tight_layout()
plt.show()