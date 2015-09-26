import numpy as np
import pandas as pd


class FeatureExtractor(object):

    def __init__(self):
        pass

    def fit(self, temperatures_xray, n_burn_in, n_lookahead):
        pass

    def transform(self, temperatures_xray, n_burn_in, n_lookahead, skf_is):
        """Use world temps as features."""
        # Set all temps on world map as features
        all_temps = temperatures_xray['tas'].values
        time_steps, lats, lons = all_temps.shape
        all_temps = all_temps.reshape((time_steps,lats*lons))
        wC = 15
        rolling_std = pd.rolling_std(pd.DataFrame(all_temps), window=wC, min_periods=1).values
        rolling_std = rolling_std[n_burn_in:-n_lookahead,:]
        rolling_quantileHigh = pd.rolling_quantile(pd.DataFrame(all_temps), window=wC, min_periods=1, quantile=0.99).values
        rolling_quantileHigh = rolling_quantileHigh[n_burn_in:-n_lookahead,:]
        rolling_quantileLow = pd.rolling_quantile(pd.DataFrame(all_temps), window=wC, min_periods=1, quantile=0.01).values
        rolling_quantileLow = rolling_quantileLow[n_burn_in:-n_lookahead,:]
        all_temps = all_temps[n_burn_in:-n_lookahead,:]
        return np.hstack((all_temps, rolling_std, rolling_quantileHigh, rolling_quantileLow))
