import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


df = pd.read_csv('train.csv')
X = df.drop('x',axis=1)
Y= df['y']
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.15,random_state=3)

ml_model = LinearRegression()
ml_model.fit(X_train,Y_train)

Y_train_predict = ml_model.predict(X_train)
rmse = (np.sqrt(mean_squared_error(Y_train,Y_train_predict)))

print(f"Rmse : {rmse}")

Y_test_predict = ml_model.predict(X_test)
rmse1 = (np.sqrt(mean_squared_error(Y_test,Y_test_predict)))

print(f"Rmse : {rmse1}")

plt.figure(figsize=(5,5))
plt.grid()
plt.scatter(Y_test,Y_test_predict)
plt.plot([min(Y_test_predict),max(Y_test_predict)],[min(Y_test_predict),max(Y_test_predict)])
plt.show()
