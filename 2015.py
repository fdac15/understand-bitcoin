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




data = (94, 49, 44, 36, 31, 27, 19, 18, 16, 15, 15, 14, 13, 13, 13, 13, 12, 12, 11, 11, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8)
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
plt.title('Files modified in 2015')
plt.xticks(index+bar_width, ('src/main.cpp', 'src/chainparams.cpp', 'configure.ac', 'src/net.cpp', 'src/init.cpp', 'src/miner.cpp', 'src/util.cpp', 'src/bitcoin-tx.cpp', 'src/netbase.cpp', 'src/rpcmining.cpp', 'src/net.h', 'qa/pull-tester/rpc-tests.sh', 'doc/release-notes.md', 'src/rpcserver.cpp', 'src/rpcmisc.cpp', 'src/rest.cpp', 'src/test/transaction_tests.cpp', 'src/Makefile.am', 'src/addrman.cpp', 'src/rpcserver.h', 'src/qt/paymentserver.cpp', 'src/test/util_tests.cpp', 'src/wallet/wallet.h', 'src/test/alert_tests.cpp', '.travis.yml', 'doc/README.md', 'doc/release-process.md', 'src/test/univalue_tests.cpp', 'src/wallet/wallet.cpp', 'src/qt/coincontroldialog.cpp'), rotation='vertical')
plt.legend()

plt.tight_layout()
plt.show()