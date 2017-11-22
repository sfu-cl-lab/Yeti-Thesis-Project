# by Yeti 11/21/2017 python 2.7.3
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import cross_val_score
import operator


df = pd.read_csv('/Users/YejiaLiu/Documents/AHL_NHL_norm_0.csv')
df_metrics = df.iloc[:, 6:24]
df_target = df.iloc[:, 24]
X_train, X_test, y_train, y_test = train_test_split(
...     df_metrics, df_target, test_size=0.4, random_state=0)


def fine_tune_network(X_train, y_train):
    train_res = {}
    for solver in ['sgd', 'adam']:
        for learning_rate_init in [0.001, 0.01, 0.1]:
            for max_iter in [100, 1000, 2000]:
                for random_state in [0, 9]:
                    nn = MLPRegressor(
                                      hidden_layer_sizes=(11,),  activation='relu', solver=solver, alpha=0.005, batch_size='auto',
                                      learning_rate='constant', learning_rate_init= learning_rate_init, power_t=0.5, max_iter= max_iter, shuffle=True,
                                      random_state=random_state, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True,
                                      early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08)
                                      res = nn.fit(X_train, y_train)
                                      scores = cross_val_score(nn, X_train, y_train, cv=5)
                                      train_res[nn] = scores
    return train_res

def nn_max(train_res):
    avgs = []
    for x in train_res.values():
        avg = np.sum(x)/5
        avgs.append(avg)
    return np.argmax(avgs)

train_res = fine_tune_network(X_train, y_train)
max_nn = train_res.keys()[nn_max(train_res)]

max_nn.score(X_test, y_test) # score = 0.37
y_predicted = nn_max.predict(X_test)
rms = sqrt(mean_squared_error(y_test, y_predicted)) # RMS = 7.04

# max_nn = MLPRegressor(activation='relu', alpha=0.005, batch_size='auto', beta_1=0.9,
#        beta_2=0.999, early_stopping=False, epsilon=1e-08,
#        hidden_layer_sizes=(11,), learning_rate='constant',
#        learning_rate_init=0.01, max_iter=100, momentum=0.9,
#        nesterovs_momentum=True, power_t=0.5, random_state=0, shuffle=True,
#        solver='sgd', tol=0.0001, validation_fraction=0.1, verbose=False,
#        warm_start=False)



