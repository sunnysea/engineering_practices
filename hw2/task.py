import numpy as np



# Task 1

def mse(y_true:np.ndarray, y_predicted:np.ndarray):
    return 1/len(y_true) * np.sum((y_true - y_predicted) ** 2)

def r2(y_true:np.ndarray, y_predicted:np.ndarray):
    y = 1/len(y_true) * np.sum(y_true)
    return 1 - (mse(y_true, y_predicted) / mse(y_true, y))

# Task 2

class NormalLR:
    def __init__(self):
        self.weights = None # Save weights here
    
    def fit(self, X:np.ndarray, y:np.ndarray):
        X = np.append(X, np.ones(X.shape[0]).reshape(-1, 1), axis=1)
        self.weights = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T), y)
    
    def predict(self, X:np.ndarray) -> np.ndarray:
        return X.dot(self.weights[:-1]) + self.weights[-1]
    
# Task 3

class GradientLR:
    def __init__(self, alpha:float, iterations=10000, l=0.):
        self.weights = None # Save weights here
        self.w = None
        self.b = None
        self.iterations = iterations
        self.l = l
        self.alpha = alpha
        
    
    def fit(self, X:np.ndarray, y:np.ndarray):
        X = np.append(X, np.ones(X.shape[0]).reshape(-1, 1), axis=1)  # add b to the end of array
        #self.w = np.dot(np.linalg.inv(X.T.dot(X)), X.T).dot(y)
        self.weights = np.zeros(X.shape[1])
        
        for n_iter in range(self.iterations):
            w_grad = np.dot(2 * (X.dot(self.weights) - y), X)
            #b_grad = np.dot(2 * (X.dot(self.w) + self.b - y), np.ones(X.shape[0]).reshape(-1, 1))
            
            self.weights -= self.alpha * (w_grad / y.size + self.l * np.sign(self.weights))
            #self.b -= self.alpha * b_grad
            

    def predict(self, X:np.ndarray):
        #X = np.append(X, np.ones(X.shape[0]).reshape(-1, 1), axis=1)
        return X.dot(self.weights[:-1]) + self.weights[-1]

# Task 4

def get_feature_importance(linear_regression):
    return np.abs(linear_regression.weights[:-1])

def get_most_important_features(linear_regression):
    return np.argsort(np.abs(linear_regression.weights[:-1]))[::-1]














