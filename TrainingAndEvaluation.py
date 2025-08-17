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
