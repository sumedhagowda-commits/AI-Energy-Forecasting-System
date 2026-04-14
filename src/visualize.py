import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ✅ 1. Actual vs Predicted
def plot_results(actual, predicted):
    plt.figure()
    plt.plot(actual.values, label='Actual')
    plt.plot(predicted, label='Predicted')
    plt.legend()
    plt.title("Energy Forecast")
    plt.savefig("images/result.png")
    plt.show()

# ✅ 2. Error Plot
def plot_error(actual, predicted):
    errors = actual.values - predicted

    plt.figure()
    plt.plot(errors)
    plt.title("Prediction Error Over Time")
    plt.savefig("images/error.png")
    plt.show()

# ✅ 3. Error Distribution
def plot_distribution(actual, predicted):
    errors = actual.values - predicted

    plt.figure()
    sns.histplot(errors, kde=True)
    plt.title("Error Distribution")
    plt.savefig("images/error_distribution.png")
    plt.show()