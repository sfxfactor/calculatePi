import numpy as np
import sys
import time

n=int(sys.argv[1])
m=int(sys.argv[2])
N=m*n

nhits=0

st=time.clock()
for i in range(m):
    #progress bar
    percent = float(i) / m
    hashes = '#' * int(round(percent * 20))
    spaces = ' ' * (20 - len(hashes))
    sys.stdout.write("\rPercent: [{0}] {1}%".format(hashes + spaces, int(round(percent * 100))))
    sys.stdout.flush()
    #if (i % (m/100) == 0):
    #    print i/(m/100),'%'

    thetas=np.random.random_sample(size=n)*180.
    Ds=np.random.random_sample(size=n)*0.5

    hits=np.where(Ds<=0.5*np.sin(np.radians(thetas)))[0]
    nhits+=len(hits)

et=time.clock()
pi=2.*m*n/nhits

print 'pi~=',pi
print 'calculated pi to ',np.abs((pi-np.pi)/np.pi)*100.,'%'
print 'calculation took ',(et-st),' seconds.'
print 'used 10^',np.log10(n*m),' trials.'
