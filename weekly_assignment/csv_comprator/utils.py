import pandas as pd
from datetime import datetime

def find_corrections(a_csv, b_csv):
    try:
        # Read CSV files into pandas DataFrames
        dataframe_of_reference = pd.read_csv(a_csv)
        dataframe_of_input = pd.read_csv(b_csv)

        # Find differences between the two DataFrames
        differences = []
        for row in range(len(dataframe_of_reference)):
            for column in range(len(dataframe_of_reference.columns)):
                if dataframe_of_reference.iloc[row, column] != dataframe_of_input.iloc[row, column]:
                    differences.append(((row+1, column+1), dataframe_of_reference.iloc[row, column], dataframe_of_input.iloc[row, column]))

        # Return the list of differences
        return differences

    except FileNotFoundError as e:
        print(f"File not found error: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

