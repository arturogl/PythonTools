import csv
import pandas as pd

def read_csv_to_dataframe(file_path):
    # Initialize an empty list to store rows
    rows = []

    # Open the CSV file
    with open(file_path, 'r', encoding='utf-8') as file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(file)
        
        # Read each row from the CSV file
        for row in csv_reader:
            # Append the row to the list of rows
            rows.append(row)

    # Create a DataFrame from the list of rows
    df = pd.DataFrame(rows)

    return df

# Path to the CSV file
file_path = 'file.csv'

# Read the CSV file and convert it to a DataFrame
df = read_csv_to_dataframe(file_path)

# Display the DataFrame
print(df)
