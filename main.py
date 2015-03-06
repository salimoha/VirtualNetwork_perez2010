import numpy as np
from __future__ import division  
from random import *
n = 60;
N = 6
vc = n*1.0/N;
#x = rand
randBinlist = lambda n: [randint(0,1) for b in range(1,n+1)] 
k0 = randBinlist(n)

k = k0[-int(vc):]
k1 = k0[:int(vc)]


