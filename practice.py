from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
import sklearn.linear_model
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn import model_selection
import pandas as pd

data = load_diabetes()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.DataFrame(data.target, columns=["Y"])

print(X)
#test_size = 0.33
#X_train, X_test, y_train, y_test = model_selection.train_test_split(X,y,test_size = test_size)

#model =LinearRegression()
#model.fit(X_train,y_train)
#result = model.score(X_test,y_test)
#print ("Regression coefficients", model.coef_)



#print ("Accuracy = %.3f%%(%.3f%%)" % (result.mean()*100.0,result.std()*100.0) )
#print("Accuracy = %.3f%%" % (result*100.0))








#dataset = pd.DataFrame(data=data.data, columns=data.feature_names)
#target = pd.DataFrame (data=data.target, columns = ['Y'])










#x = dataset
#y = target["Y"]

#lm = LinearRegression()
#lm.fit(x,y)

#lg = LogisticRegression()
#lg.fit(x,y)

#ridge = Ridge(alpha=0.1)
#ridge.fit(x,y)

#polynomial = LinearRegression()
#poly = PolynomialFeatures(degree = 2)
#x_poly = poly.fit_transform(x)
#polynomial.fit(x_poly,y)



#trial=np.array([0.231, -0.044642,-0.231, 0.124,0.324,-0.23,-0.13,0.42,0.-32,0.11 ])
#trial=trial.reshape(1,-1)

#predictionLinear = lm.predict(trial)
#predictionLogistic = lg.predict(trial)
#predictionRidge= ridge.predict(trial)
#predictionPolynomial = polynomial.predict(trial) #


#print("Linear Prediction is : " + str(predictionLinear))
#print("Logistic Prediction is : " + str(predictionLogistic))
#print("Ridge Prediction is : " + str(predictionRidge))
#print("Polynomial Prediction is : " + str(predictionPolynomial))

