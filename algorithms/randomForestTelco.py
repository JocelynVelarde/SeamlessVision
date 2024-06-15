import pickle

pickled_model = pickle.load(open('assets/files/telcoRandomForestModel.pkl', 'rb'))
x_test = [[2481, 1501.75, 25.0, 1, 61, 1, 1, 0, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 0]]
import numpy as np

x_test = np.array([[2481, 1501.75, 25.0, 1, 61, 1, 1, 0, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 0]])

prediction = pickled_model.predict(x_test)

print(prediction)
