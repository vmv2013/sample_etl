import pandas as pd
from pandas import json_normalize

def flatten_columns(df, column_paths):
    """
    Flatten multiple columns with nested JSON data in a DataFrame.

    Parameters:
    - df: DataFrame
    - column_paths: dict
        A dictionary where keys are the original column names and values are the JSON paths for the flattened columns.

    Returns:
    - DataFrame
        A new DataFrame with the specified columns flattened.
    """
    # Check if all specified columns exist in the DataFrame
    for column_name in column_paths.keys():
        if column_name not in df.columns:
            raise ValueError(f"Column '{column_name}' not found in the DataFrame.")

    # Use json_normalize to flatten each specified column with the JSON path as the prefix
    for column_name, json_path in column_paths.items():
        flattened_df = json_normalize(df[column_name], record_path=json_path)
        flattened_df.columns = [f"recordpath_{col}" for col in flattened_df.columns]
        df = pd.concat([df.drop([column_name], axis=1), flattened_df], axis=1)

    return df

# Example usage:
# Assuming df is your DataFrame and {'col2': 'json_path_col2', 'col3': 'json_path_col3'} are the JSON paths
# Replace {'col2': 'json_path_col2', 'col3': 'json_path_col3'} with the actual JSON paths in your DataFrame
df = flatten_columns(df, {'col2': 'json_path_col2', 'col3': 'json_path_col3'})

# Display the flattened DataFrame
print(df)
