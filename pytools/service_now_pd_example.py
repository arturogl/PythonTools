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
file_path = 'incident.csv'

# Read the CSV file and convert it to a DataFrame
df = read_csv_to_dataframe(file_path)

# Read the CSV file using pandas
df2 = pd.read_csv('incident.csv')

# Display the DataFrame
print(df)
print(df2)

# Cuenta el número de active incidents
num_incidents = df['number'].count()

num_active_incidents = df[df['active'] == "true"].count()

# Imprime el resultado
print("Number of incidents", num_incidents)

# Imprime el resultado
print("Number of active incidents", num_active_incidents)

# Add separate columns for year and month extracted from the timestamp
active_incidents_df = df[df['active'] == "true"]

# Perform aggregation based on the year_month column
agg_active_incidents_df = active_incidents_df.groupby(['location','assignment_group'])['number'].count()
print(agg_active_incidents_df)
