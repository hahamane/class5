| Name | Date |
|:-------|:---------------|
|Dae Hun Park| 2019-03-20|

-----

### Resources
Your repository should include the following:

- Python script for your analysis: `analysis.py`
- Results figure/saved file: `multiplegraph` 
- Dockerfile for your experiment: `Dockerfile`
- runtime-instructions in a file named RUNME.md

-----

## Research Question

Using the data colleted, is it possible to 
1. understand how variables would correlate to diabetes progression
2. predict the progression of diabetes.

### Abstract

The data of 442 patients were collected to understand the progresss of diabetes after 1 year. Using the data collected, it may be possible to understand the relationship between sex, age, body mass index, average blood pressure and 6 different blood serum, noted as s1, s2, s3, s4, s5 and s6; and the progress of diabete. Here we tried to understand whether each of these variables would affect the progress of diabetes. From the comparison of different regression model, it was found that linear regression is the model with the highest R2 value. After the evaluating the coefficients and using p-value test, it was found that only 5 variables, namely sex, body mass index, average blood pressure, s1 and s5 were the variable with significant correlation to the progress of diabetes. However, even after only considering the 5 variables it was found that the model does not provide adequate prediction.

### Introduction

The data used are ten baseline variables, age, sex, body mass index, average blood pressure, and six blood serum measurements obtained for each of 442 diabetes patients, as well as the response of interest, a quantitative measure of disease progression one year after baseline. It was taken from the publicly available BNU1 dataset([https://scikit-learn.org/stable/datasets/index.html#toy-datasets](https://scikit-learn.org/stable/datasets/index.html#toy-datasets)).

### Methods

The methods compared for modelling this data were linear regression, polynomial regression and the Ridge Regressor built into scikit-learn. Pseudocode for Ridge regressor can be found [here](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html) and for linear regression [here](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html) and for 2 degree polynomial regression [here](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html). 

Each models was cross-validated and its score were calculated. The method can be found [here](https://machinelearningmastery.com/evaluate-performance-machine-learning-algorithms-python-using-resampling/). Once the model with highest score is found, p value test was performed to see which variables had significant impact on the model. The statmodel library was used to perform the p-value test found [here](https://stackoverflow.com/questions/27928275/find-p-value-significance-in-scikit-learn-linearregression). 

Once the significant variables were found, the regression model is reevaluated to understand the accuracy of the model.

### Results

After the cross validation of models, it was found that linear regression (46%) had highest score compared to that of Ridge (41%) and that of polynomial (38%). Therefore the linear regression model was chosen. The figure below shows the p-values with alpha > 0.1
[P-value Test] (./P-value_test.PNG)

It was found that only 5 variables, namely sex, body mass index, average blood pressure, s1 and s5 were the variable with significant correlation to the progress of diabetes. For example, as seen in the graph below, we can see that as bp and bmi increases, so does y.
[bp vs bmi vs y graph](./MultipleGraph/bp_vs_bmi_vs_Y.html)

The performance of the regression model using only 5 variable mentioned above was 46%.

### Discussion

Since the score of the modified method is still too low, it is not possible to predict the progress of the diabetes using this method. However, this method shows that there are relationship between 5 variables and the diabete progress. 


### References
1. https://scikit-learn.org/stable/datasets/index.html#toy-datasets
2. https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html
3. https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
4. https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html)
5. https://machinelearningmastery.com/evaluate-performance-machine-learning-algorithms-python-using-resampling/
6. https://stackoverflow.com/questions/27928275/find-p-value-significance-in-scikit-learn-linearregression 

-------
