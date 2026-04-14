def create_features(df):
    df['hour'] = df['date'].dt.hour
    df['day'] = df['date'].dt.day
    df['month'] = df['date'].dt.month
    df['weekday'] = df['date'].dt.weekday
    df['year'] = df['date'].dt.year

    print("✅ Features Created")
    return df