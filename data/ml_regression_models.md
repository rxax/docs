## Machine Learning - Regression Algorithms

Commonly used: Linear Regression, Logistic Regression, Ridge Regression, Lasso Regression, Polynomial Regression, Bayesian Linear Regression

### Linear Regression

Linear regression performs the task to predict a dependent variable(target) based on the given independent variable(s).

```python
import numpy as np
from sklearn.linear_model import LinearRegression
X = np.array([[2, 1], [3, 2], [4, 2], [5, 3]])
# y = 1 * x_0 + 2 * x_1 + 3
y = np.dot(X, np.array([1, 2])) + 3
lr = LinearRegression().fit(X, y)
lr.predict(np.array([[1, 5]]))

# Output
# array([14.])
```

Pros:

* Linear Regression is simple to implement.
* Less complexity compared to other algorithms.
* Linear Regression may lead to over-fitting but it can be avoided using some dimensionality reduction techniques, regularization techniques, and cross-validation.

Cons:

* Outliers affect this algorithm badly.
* It over-simplifies real-world problems by assuming a linear relationship among the variables, hence not recommended for practical use-cases.


### Decision Tree

The decision tree models can be applied to all those data which contains numerical features and categorical features.

```python
rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(80, 1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - rng.rand(16))
# Fit regression model
regr = DecisionTreeRegressor(max_depth=2)
regr.fit(X, y)
# Predict
X_test = np.arange(0.0, 5.0, 1)[:, np.newaxis]
result = regr.predict(X_test)
print(result)

# Output:
# [ 0.05236068  0.71382568  0.71382568  0.71382568 -0.86864256]
```

Pros:

* Easy to understand and interpret, visually intuitive.
* It can work with numerical and categorical features.
* Requires little data preprocessing: no need for one-hot encoding, dummy variables, etc.

Cons:

* It tends to overfit.
* A small change in the data tends to cause a big difference in the tree structure, which causes instability.
Implementation
  
### Support Vector Regression

It tries to predict the real values. This algorithm uses hyperplanes to segregate the data.

```python
from sklearn.svm import SVR
import numpy as np
rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(80, 1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - rng.rand(16))
# Fit regression model
svr = SVR().fit(X, y)
# Predict
X_test = np.arange(0.0, 5.0, 1)[:, np.newaxis]
svr.predict(X_test)

# Output:
# array([-0.07840308,  0.78077042,  0.81326895,  0.08638149, -0.6928019 ])
```

Pros:

* Robust to outliers.
* Excellent generalization capability
* High prediction accuracy.

Cons:

* Not suitable for large datasets.
* They do not perform very well when the data set has more noise.

### Random Forest Regressor

Random Forests are an ensemble(combination) of decision trees. It is a Supervised Learning algorithm used for classification and regression.

```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
X, y = make_regression(n_features=4, n_informative=2, random_state=0, shuffle=False)
rfr = RandomForestRegressor(max_depth=3)
rfr.fit(X, y)
print(rfr.predict([[0, 1, 0, 1]]))

# Output:
# [33.2470716]
```

Pros:

* Good at learning complex and non-linear relationships
* Very easy to interpret and understand

Cons:

* They are prone to overfitting
* Using larger random forest ensembles to achieve higher performance slows down their speed and then they also need more memory.