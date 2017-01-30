import numpy as np
import pandas as pd
import scipy.stats as stats
from sklearn import svm
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import cross_validation


#load data
def load_unicef_data():
   
    fname_train = '/home/yejial/Desktop/code_WHL_NHL/training_data_edit.csv'
    fname_test='/home/yejial/Desktop/code_WHL_NHL/test_data_edit.csv'
    # Uses pandas to help with string-NaN-numeric data.
    train_data = pd.read_csv(fname_train, na_values='_')
    test_data = pd.read_csv(fname_test, na_values='_')
    # Strip countries title from feature names.
    #features = data.axes[1][1:]
    # Separate country names from feature values.
    #players = data.values[:,0]
    train_values =train_data.values[1:,1:]
    # Convert to numpy matrix for real.
    train_values = np.asmatrix(train_values,dtype='float64')
    
    test_values =test_data.values[1:,1:]
    # Convert to numpy matrix for real.
    test_values = np.asmatrix(test_values,dtype='float64')
    # Modify NaN values (missing values).
    #mean_vals = stats.nanmean(values, axis=0)
    #inds = np.where(np.isnan(values))
    #values[inds] = np.take(mean_vals, inds[1])
    return train_values,test_values

train_values,test_values=load_unicef_data()

#normalize data
train_target=np.array(train_values[:,-1])
train_features=np.array(train_values[:,0:8])
test_target=np.array(test_values[:,-1])
test_features=np.array(test_values[:,0:8])
values=normalize_data(np.concatenate((train_features,test_features),axis=0))
train_fea_norm=values[:1730,:]
test_fea_norm=values[1730:,:]

print train_features.shape
print test_features.shape
print values.shape
print train_fea_norm.shape
print test_fea_norm.shape


#using cross validation to select model, guassian kernel 
accuracy=[]
C_2d_range = [1e-2, 1, 1e2]
gamma_2d_range = [1e-1, 1, 1e1]
for C in C_2d_range:
    for gamma in gamma_2d_range:
        clf1= svm.SVC(C=C,gamma=gamma)
        print clf1
        cv = cross_validation.ShuffleSplit(train_target.size, n_iter=5,test_size=0.4, random_state=None)
        scores = cross_validation.cross_val_score(clf1,train_fea_norm,train_target,cv = cv)
        accuracy_train=np.mean(scores)
        accuracy.append(accuracy_train)

#calculate accuracy on test data 
clf1=svm.SVC(C=1, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=1,
  kernel='rbf', max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)

clf1.fit(test_fea_norm, test_target)  
clf1.score(test_fea_norm, test_target)


