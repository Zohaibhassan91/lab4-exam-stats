import numpy as np
import pandas as pd
from scipy import stats

# Input data
scores_data = [72, 65, 88, np.nan, 54, 91, 76, np.nan, 83, 69]
scores = pd.Series(scores_data)

# (a) Descriptive statistics
print("Descriptive Statistics:")
print(scores.describe())
print("-" * 40)

# (b) Skewness and Kurtosis (dropping missing values)
clean_scores = scores.dropna()
skewness = stats.skew(clean_scores)
kurt = stats.kurtosis(clean_scores)

print(f"Skewness: {skewness:.4f}")
print(f"Kurtosis: {kurt:.4f}")
print("-" * 40)

# (c) Count missing values
missing_count = scores.isnull().sum()
print(f"Missing values: {missing_count}")
print("-" * 40)

# (d) Fill missing scores with column mean
mean_val = scores.mean()
filled_scores = scores.fillna(mean_val)

print("Filled scores:")
print(filled_scores)