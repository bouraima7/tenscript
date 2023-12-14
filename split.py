import pandas as pd

# Read the Excel file
df = pd.read_excel('matched.xlsx')

# Get unique values from the specific column
unique_values = df['POC 1'].unique()
output_folder = r'Reports'

#un2 = df['POC 2'].unique()
# This is POC2 but I dont know how to implement algo to filter in a combo of POC1 and POC2.


#Split the data into different dataframes based on the column values
dataframes = {}
for value in unique_values:
    dataframes[value] = df[df['POC 1'] == value]

# Save each dataframe as a separate Excel file
for value, dataframe in dataframes.items():
    dataframe.to_excel(f'{output_folder}/PCI_Assets_{value}.xlsx', index=False)


