#choose learning rate
import numpy as np
import scipy.special as sps
import matplotlib.pyplot as plt

  
  
# Maximum number of iterations.  Continue until this limit, or when error change is below tol.
max_iter = 500
tol = 0.00001
  
# Step size for gradient descent.
etas =np.array([0.5,0.3,0.1,0.05,0.01,0.001])

def normalize_data(x):
    mvec=x.mean(0)
    stdvec=x.std(axis=0)
    return (x-mvec)/stdvec
  
  
# Load data.
data = np.genfromtxt('/home/yejial/Desktop/code_WHL_NHL/pp.txt')
#data=np.random.shuffle(data)
data=np.random.permutation(data)
# Data matrix, with column of ones at end.
X = normalize_data(data[:,0:8])
# Target values, 0 for class 1, 1 for class 2.
t = data[:,8]
# For plotting data
class1 = np.where(t==0)
X1 = X[class1]
class2 = np.where(t==1)
X2 = X[class2]
  
  
# Initialize w.
w = np.array([0,0.1,0,0,0,0,0,0])
  
# Error values over all iterations.
e_all ={}
  
DATA_FIG = 1
  
# Set up the slope-intercept figure
#SI_FIG = 2
#plt.figure(SI_FIG)
#plt.rcParams.update({'font.size': 15})
#plt.title('Separator in slope-intercept space')
#plt.xlabel('slope')
#plt.ylabel('intercept')
#plt.axis([-5, 5, -10, 0])
  
  
for eta in etas:
 e_all[eta]=[]
 w=np.array([0,0.1,0,0,0,0,0,0])
 for iter in range (0,max_iter):
  for i in range(0,200):
  # Compute output using current w on all data X.
   y = sps.expit(np.dot(X,w))
   # Update w, *subtracting* a step in the error derivative since we're minimizing
   grad_e = np.multiply((y[i] - t[i]), X[i,:].T)
   #w_old = w
   w = w - eta*grad_e
  y=sps.expit(np.dot(X,w))  
  # e is the error, negative log-likelihood (Eqn 4.90)
  e = -np.mean(np.multiply(t,np.log(y+1e-6)) + np.multiply((1-t),np.log(1-y+1e-6)))
  
  # Add this error to the end of error vector.
  e_all[eta].append(e)
    
   
  # Gradient of the error, using Eqn 4.91
    
  # Gradient of the error, using Eqn 4.91
  #grad_e = np.mean(np.multiply((y - t), X.T), axis=1)
  
  
  
    
   
    
  # Stop iterating if error doesn't change more than tol.
  if iter>0:
    if np.absolute(e-e_all[eta][iter-1]) < tol:
      break
   
  
  
# Plot error over iterations
plt.figure()
for eta in etas:
 plt.plot(e_all[eta])
plt.ylabel('Negative log likelihood')
plt.title('Training logistic regression')
plt.legend(['eta 0.5','eta 0.3','eta 0.1','eta 0.05','eta 0.01','eta 0.001'])
#plt.legend(handles=[etas])
plt.show()


w=[-0.17319538,-0.57551455,0.16241183,0.41386914,0.32418731,-0.69535434,0.08766237,0.2382722 ]

data = np.genfromtxt('/home/yejial/Desktop/code_WHL_NHL/pt.txt')
x=normalize_data(data[:,0:8])
y=data[:,8]
predicted=sps.expit(np.dot(x,w))
acc=0
for i in range(0,len(pre)):
    if pre[i]==y[i]:
        acc+=1
    
res=(float(acc)/float(len(pre)))

