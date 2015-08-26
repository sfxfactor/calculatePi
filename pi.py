import numpy as np
import sys
import time

n=int(sys.argv[1])
m=int(sys.argv[2])

nhits=0

st=time.clock()
for i in range(m):

    thetas=np.random.random_sample(size=n)*180.
    Ds=np.random.random_sample(size=n)*0.5

    hits=np.where(Ds<=0.5*np.sin(np.radians(thetas)))[0]
    nhits+=len(hits)

et=time.clock()
pi=2.*m*n/nhits

print 'pi~=',pi
print 'calculated pi to ',np.abs((pi-np.pi)/np.pi)*100,'%'
print 'calculation took ',(et-st),' seconds.'
print 'used ',n*m,' trials.'
