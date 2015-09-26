import numpy as np
class FeatureExtractor(object):

    def __init__(self):
        pass

    def fit(self, temperatures_xray, n_burn_in, n_lookahead):
        pass

    def transform(self, temperatures_xray, n_burn_in, n_lookahead, skf_is):
        """Use world temps as features."""
        # Set all temps on world map as features
        lat_bottom = -80
        lat_top = 80
        lon_left = 80
        lon_right = 320
        #all_temps = temperatures_xray['tas'].values
        all_temps = temperatures_xray['tas'].loc[:, lat_bottom:lat_top, lon_left:lon_right].values
        print all_temps.shape
        time_steps, lats, lons = all_temps.shape
        all_temps = all_temps.reshape((time_steps,lats*lons))
        all_temps = all_temps[n_burn_in:-n_lookahead,:]
        all_diffs = np.zeros_like(all_temps)
        all_diffs[1:-1,:] = all_temps[:-2,:] - all_temps[2:,:]
        all_diffs[1,:] = all_temps[0,:] - all_temps[1,:]
        all_diffs[-1,:] = all_temps[-2,:] - all_temps[-1,:]
        return np.hstack((all_temps, all_diffs))
