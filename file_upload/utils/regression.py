import pandas as pd
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error
import numpy as np

def regression(df, y, x):
    independent = df[x]
    dependent = df[y]

    independent = sm.add_constant(independent, has_constant='add')
    model = sm.OLS(dependent, independent)
    results = model.fit()

    predictions = results.predict(independent)
    mse = mean_squared_error(dependent, predictions)
    rmse = np.sqrt(mse)
    nrmse = rmse / (dependent.max() - dependent.min())
    
    regression_summary = {
        "coefficient_names": results.params.index.to_list(),
        "coefficient_values": results.params.to_list(),
        "p_values": results.pvalues.to_list(),
        "r_squared": results.rsquared,
        "adj_r_squared": results.rsquared_adj,
        "mse": mse,
        "rmse": rmse,
        "nrmse": nrmse
    }
    return regression_summary