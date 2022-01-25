
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

dataset = pd.read_csv('cybercrimestatewise.csv')

x = dataset.iloc[:, :3]

y = dataset.iloc[:,3:4]


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(x, y)

pickle.dump(regressor, open('cycrmodel.pkl','wb'))

model = pickle.load(open('cycrmodel.pkl','rb'))
print(model.predict([[4, 300, 500]]))