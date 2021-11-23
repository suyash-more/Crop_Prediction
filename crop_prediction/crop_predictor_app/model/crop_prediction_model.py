# Importing Libraries

import numpy as np
import pandas as pd

# For data visualization
import matplotlib.pyplot as plt
import seaborn as sns

# For interactivity
from ipywidgets import interact

# For warnings
import warnings
warnings.filterwarnings('ignore')

# For Clustering Analysis
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

import pickle                                                                                               

def give_prediction():
    #Loading Dataset
    # data = pd.read_csv('./Crop_recommendation.csv')
    # data

    # crops = list(data['label'].value_counts().index)
    # x = data[data['label'] == crops]
        
    # x = data.drop(['label'], axis=1)

    # #Selecting all values of data
    # x = x.values

    # wcss = []
    # for i in range(1,11):
    #     km = KMeans(n_clusters = i,init = 'k-means++',max_iter = 300, n_init = 10, random_state = 0)
    #     km.fit(x)
    #     wcss.append(km.inertia_)

    # km = KMeans(n_clusters = 4,init = 'k-means++',max_iter = 300, n_init = 10, random_state = 0)
    # y_means = km.fit_predict(x)

    # y = data['label']
    # x = data.drop(['label'],axis = 1)

    # x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 0)

    # model = LogisticRegression(solver='liblinear')
    # model.fit(x_train, y_train)
    # print("model trained and tested")
    with open('./model/kmeans_model.pkl', 'rb') as f:
        model = pickle.load(f)
    prediction = model.predict((np.array([[90,
                                        40,
                                        40,
                                        20,
                                        80,
                                        7,
                                        200]])))
    return prediction
