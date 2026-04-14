from sklearn.ensemble import RandomForestRegressor

def train_model(df):
    features = ['hour', 'day', 'month', 'weekday', 'year']

    X = df[features]
    y = df['energy']  # ✅ updated column name

    split = int(len(df) * 0.8)

    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_train, y_train)

    print("✅ Model Trained")
    return model, X_test, y_test