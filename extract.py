import pandas as pd
from datetime import datetime

def read_csv_file(file_path):
    """
    Reads a CSV file and returns a DataFrame.
    Includes error handling for file reading issues.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Path to the CSV file
file_path = r'vulnerabilities-verified.csv'  

# Read the CSV file
data = read_csv_file(file_path)

# Check if data is available
if data is not None:
    # Print entire contents of each column
    print("Display IPv4 Address:")
    print(data['asset.display_ipv4_address'])
    print("\nAsset Name:")
    print(data['asset.name'])
    print("\nAsset Operating System:")
    print(data['asset.operating_system'])
    print("\nAsset Tags:")
    print(data['asset.tags'])
    print("\nDefinition Description:")
    print(data['definition.description'])
    print("\nDefinition Name:")
    print(data['definition.name'])
    print("\nDefinition Solution:")
    print(data['definition.solution'])
    print("\nID:")
    print(data['id'])
    print("\nOutput:")
    print(data['output'])
    print("\nSeverity:")
    print(data['severity'])

    # Define the path for the Excel file with a timestamp
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    excel_file_path = rf'C:\Users\00833346\Documents\TenabelScript\vulnerabilities_export_{timestamp}.xlsx'

    # Export to Excel
    try:
        data.to_excel(excel_file_path, index=False)
        print(f"Data exported successfully to {excel_file_path}")
    except Exception as e:
        print(f"An error occurred while exporting to Excel: {e}")
else:
    print("No data available to export.")
