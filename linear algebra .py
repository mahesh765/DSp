import numpy as np
x=np.array([[2,1],[22,98]]);
y=np.array([[3,4],[2,1]])
print "matrix x is",x;
print "matrix y is",y;
#linear algebric opration on matrices
#determinent
s1=np.linalg.det(x);
print "determinent of given matrices",s1;
#inverse
s2=np.linalg.inv(y);
print "inverse of given matrice",s2;
#trace
s3=np.trace(x);
print "trace of given matrice",s3;
#eign values
s4=np.linalg.eig(x);
print "eign values",s4;
#maximum
s5=np.max(x);
print "maximum value of given list",s5;
#minimum
s6=np.min(x);
print "minimum value",s6
#shape of matrix
s7=np.shape(x);
print "the shape of the matrix is",s7;
#mathematical operations on lists
#addition
z1=np.add(x,y);
print "sum of array's is ",z1;
z2=np.subtract(x,y);	
#subtraction
print "subtraction of array's gives",z2;
z3=np.multiply(x,y);	
#multiplication
print "multiplied value of array's is",z3;
z4=np.divide(x,y); 
#division
print "division of array's gives",z4;
z5=np.sqrt(x);
print "square root of array elements",z5;
#inner product/dot product
a1=np.dot(x,y);
print "inner product of vectors",a1;







