import pandas as pd

print(pd.__version__)

# Dataframe
# Series - Represents a single column
print(pd.Series(['San Francisco', 'Chicago', 'New York']))

city_names = pd.Series(['San Francisco', 'Chicago', 'New York'])
population = pd.Series([100, 200 , 300])

print(pd.DataFrame({'city_name ': city_names, 'population ': population}))

california_housing_dataframe = pd.read_csv('/Users/biplabkumardas/google-tensorflow/california_housing_train.csv', sep=",")
print(california_housing_dataframe.describe())
print(type(california_housing_dataframe['housing_median_age']))
