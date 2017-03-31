from sklearn.mixture import GaussianMixture as gmm
import numpy as np
import pandas as pd
import scipy.stats as stats
from sklearn import preprocessing

datasets='/Users/YejiaLiu/Downloads/cleaned_schucker_wilson_table.csv'
data=pd.read_csv(datasets)
x_train_set1=preprocessing.scale(train_data_set1[:,0:5])
x_test_set1=preprocessing.scale(test_data_set1[:,0:5])

lowest_bic = np.infty
bic = []
n_components_range = range(1, 7)
cv_types = ['spherical', 'tied', 'diag', 'full']
for cv_type in cv_types:
    for n_components in n_components_range:
        # Fit a Gaussian mixture with EM
        gmm = mixture.GaussianMixture(n_components=n_components,
                                      covariance_type=cv_type)
        gmm.fit(x_train_set1)
        bic.append(gmm.bic(x_train_set1))
        if bic[-1] < lowest_bic:
            lowest_bic = bic[-1]
            best_gmm = gmm
#best_gmm            
model=mixture.GaussianMixture(covariance_type='full', init_params='kmeans', max_iter=100,
        means_init=None, n_components=4, n_init=1, precisions_init=None,
        random_state=None, reg_covar=1e-06, tol=0.001, verbose=0,
        verbose_interval=10, warm_start=False, weights_init=None).fit(x_train_set1)

model.score(x_train_set1)
model.score(x_test_set1)

#each_test_player_score
scores=[]
for i in range(0,194):
    scores.append(model.score(x_test_set1[i]))
