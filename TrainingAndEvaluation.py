from sklearn import neighbors
from sklearn.metrics import mean_squared_error
from math import sqrt

knn = neighbors.KNeighborsRegressor(n_neighbors=10,n_jobs=4)
knn.fit(x,y_train)
y_pred = knn.predict(test)
knn.score(test,y_test)
error = sqrt(mean_squared_error(y_test,y_pred)) #calculate rmse

from sklearn.ensemble import RandomForestRegressor
rfr = RandomForestRegressor()
rfr.fit(x,y_train)
pred=rfr.predict(test)
rfr.score(test,y_test)
err = sqrt(mean_squared_error(y_test,pred))

print(error,err)

#Make actual vs predicted graph

import matplotlib.pyplot as plt
import numpy as np

x_axis = np.arange(len(y_test))

# Take last 200 samples so it’s clear
plt.figure(figsize=(12, 6))
plt.plot(x_axis[-200:], y_test[-200:], color='red', label="Actual")
plt.plot(x_axis[-200:], pred[-200:], color='green', label="Predicted")

plt.title("Actual vs Predicted (Last 200 Samples)", fontsize=16)
plt.xlabel("Sample Index")
plt.ylabel("Value")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
