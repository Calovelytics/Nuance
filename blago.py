import pandas as pd
import sys

def filecombine(file_paths):
    # Check if file_paths is empty
    if not file_paths:
        raise ValueError("No file paths provided. Please provide at least one CSV file.")

    combined_df = pd.read_csv(file_paths[0])  # Start with the first file

    for file_path in file_paths[1:]:  # Loop over the remaining files
        df = pd.read_csv(file_path, header=0)
        combined_df = pd.concat([combined_df, df], ignore_index=True)  # Concatenate dataframes

    return combined_df  # Return the combined dataframe after the loop

if __name__ == "__main__":
    # Use command-line arguments or default to a hardcoded list
    if len(sys.argv) > 1:
        file_paths = sys.argv[1:]  # Reassign file_paths with command-line arguments
    else:
        # Raise an error or define a default set of files
        file_paths = ['1.csv', '2.csv']
        if not file_paths:  # This will be False if default file paths are provided
            raise ValueError("No file paths provided. Please provide at least one CSV file.")
    
    combined_df = filecombine(file_paths)  # Combine the files
    combined_df.to_csv('output.csv', index=False)  # Save the combined dataframe to a CSV file