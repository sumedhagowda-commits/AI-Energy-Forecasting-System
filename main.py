# ================================
# AI Energy Forecasting Main File
# ================================

# Import modules
from src.data_loader import load_data
from src.preprocess import preprocess_data
from src.features import create_features
from src.train import train_model
from src.predict import make_predictions
from src.evaluate import evaluate_model
from src.visualize import plot_results, plot_error, plot_distribution


def main():
    print("\n🚀 Starting Energy Forecasting Pipeline...\n")

    # -------------------------------
    # Step 1: Load Data
    # -------------------------------
    print("📥 Loading Data...")
    df = load_data("data/energy.csv")

    # -------------------------------
    # Step 2: Preprocess Data
    # -------------------------------
    print("\n🧹 Preprocessing Data...")
    df = preprocess_data(df)

    # -------------------------------
    # Step 3: Feature Engineering
    # -------------------------------
    print("\n⚙️ Creating Features...")
    df = create_features(df)

    # -------------------------------
    # Step 4: Train Model
    # -------------------------------
    print("\n🤖 Training Model...")
    model, X_test, y_test = train_model(df)

    # -------------------------------
    # Step 5: Make Predictions
    # -------------------------------
    print("\n📊 Generating Predictions...")
    predictions = make_predictions(model, X_test)

    # -------------------------------
    # Step 6: Evaluate Model
    # -------------------------------
    print("\n📈 Evaluating Model...")
    rmse, r2 = evaluate_model(y_test, predictions)

    # -------------------------------
    # Step 7: Visualization
    # -------------------------------
    print("\n📉 Creating Visualizations...")
    plot_results(y_test, predictions)
    plot_error(y_test, predictions)
    plot_distribution(y_test, predictions)

    # -------------------------------
    # Final Summary
    # -------------------------------
    print("\n✅ Pipeline Completed Successfully!")
    print(f"\n📌 Final Metrics:")
    print(f"RMSE: {rmse}")
    print(f"R² Score: {r2}")
    print("\n📁 Check 'images/' folder for graphs.\n")


# Run the pipeline
if __name__ == "__main__":
    main()
