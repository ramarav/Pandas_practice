# Import cars data
import pandas as pd
cars = pd.read_csv('car-sales.csv', index_col = 0)

# Print out first 4 observations
print(cars[0:4])

# Print out fifth and sixth observation
print(cars[4:6])