# Import pandas and cars.csv
import pandas as pd
cars = pd.read_csv('car-sales.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['Colour'])

# Print out country column as Pandas DataFrame
print(cars[['Colour']])

# Print out DataFrame with country and drives_right columns
print(cars[['Doors', 'Colour']])