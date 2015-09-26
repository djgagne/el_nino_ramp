from sklearn.ensemble import GradientBoostingRegressor
from sklearn.base import BaseEstimator


class Regressor(BaseEstimator):
    def __init__(self):
        self.clf = GradientBoostingRegressor(n_estimators=200, max_features=300, max_depth=5)

    def fit(self, X, y):
        self.clf.fit(X, y.ravel())

    def predict(self, X):
        return self.clf.predict(X)
