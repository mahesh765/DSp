import numpy as np
import scipy as sp
a=np.array([20,2,9,98,49]);
b=input("enter the array you want to append");
k=len(b);
i=0;
#appending array elements using while loop
while i<k:
	a=np.append(a,b[i]);
	i=i+1;
print "the final array is",a;
