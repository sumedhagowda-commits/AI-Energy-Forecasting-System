import pandas as pd

def load_data(path):
    # Load dataset
    df = pd.read_csv(path)

    # Rename columns (CRITICAL STEP)
    df.columns = ['date', 'energy']

    # Convert to datetime
    df['date'] = pd.to_datetime(df['date'])

    print("✅ Data Loaded Successfully")
    print(df.head())

    return df