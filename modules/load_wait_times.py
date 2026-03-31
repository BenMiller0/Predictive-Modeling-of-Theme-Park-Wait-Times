import pandas as pd
def load_wait_times():
    # This cell loads and cleans the wait times data. It removes unnecessary columns, converts the Average_Wait column to numeric, and standardizes the text in the Park and Name columns.
    # It also removes any rows where the Average_Wait is missing or negative, and averages wait times for duplicate rides.
    wait_times_df = pd.read_csv("data/raw/wait_times.csv")

    #copy of wait_df
    clean_wait_times_df = wait_times_df.copy()

    # Keep only needed columns
    clean_wait_times_df = clean_wait_times_df[["Park", "Name", "Average_Wait"]]

    # Average_Wait is numeric
    clean_wait_times_df["Average_Wait"] = pd.to_numeric(
        clean_wait_times_df["Average_Wait"],
        errors="coerce"
    )

    # Remove rides where Average_Wait is missing
    clean_wait_times_df = clean_wait_times_df.dropna(subset=["Average_Wait"])
    clean_wait_times_df = clean_wait_times_df[clean_wait_times_df["Average_Wait"] >= 0]

    # Standardize text 
    clean_wait_times_df["Park"] = clean_wait_times_df["Park"].str.strip().str.lower()
    clean_wait_times_df["Name"] = clean_wait_times_df["Name"].str.strip().str.lower()

    # Remove duplicate rides 
    clean_wait_times_df = clean_wait_times_df.groupby(
        ["Park", "Name"],
        as_index=False
    )["Average_Wait"].mean()

    return clean_wait_times_df