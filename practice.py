from sklearn.datasets import load_diabetes
import numpy as np 
import pandas as pd 
from sklearn.linear_model import LinearRegression
import sklearn.linear_model
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
data = load_diabetes()
dataset = pd.DataFrame(data=data.data, columns=data.feature_names)
target = pd.DataFrame (data=data.target, columns = ['Y'])

x = dataset
y = target["Y"]

lm = LinearRegression()
lm.fit(x,y)

lg = LogisticRegression()
lg.fit(x,y)

ridge = Ridge(alpha=0.1)
ridge.fit(x,y)

polynomial = LinearRegression()
poly = PolynomialFeatures(degree = 2)
x_poly = poly.fit_transform(x)
polynomial.fit(x_poly,y)



trial=np.array([0.231, -0.044642,-0.231, 0.124,0.324,-0.23,-0.13,0.42,0.-32,0.11 ])
trial=trial.reshape(1,-1)

predictionLinear = lm.predict(trial)
predictionLogistic = lg.predict(trial)
predictionRidge= ridge.predict(trial)
predictionPolynomial = polynomial.predict(trial) 


print("Linear Prediction is : " + str(predictionLinear))
print("Logistic Prediction is : " + str(predictionLogistic))
print("Ridge Prediction is : " + str(predictionRidge))
print("Polynomial Prediction is : " + str(predictionPolynomial))

