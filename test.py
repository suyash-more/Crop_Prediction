import pickle
import numpy as np
import joblib
# model = pickle.load(open('kmeans_model.pkl','rb'))

with open('./model/kmeans_model.pkl', 'rb') as f:
    model = pickle.load(f)
    
prediction = model.predict((np.array([[107,
                                       34,
                                       32,
                                       26,
                                       66,
                                       7,
                                       180]])))
print("The suggested Crop for Given Climatic condition is :", prediction)