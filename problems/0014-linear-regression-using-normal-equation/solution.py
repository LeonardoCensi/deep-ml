import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	X_transpose = np.transpose(X)
	inverse_XT_X = np.linalg.inv(np.dot(X_transpose, X))
	theta = np.dot(inverse_XT_X, np.dot(X_transpose, y))
	return theta