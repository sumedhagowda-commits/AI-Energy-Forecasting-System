def preprocess_data(df):
    # Sort by time (VERY IMPORTANT for time-series)
    df = df.sort_values('date')

    # Drop missing values
    df = df.dropna()

    print("✅ Data Preprocessed")
    return df