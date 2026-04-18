import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import os

def forecast_temperature(df):
    os.makedirs("outputs/graphs", exist_ok=True)

    # Convert date to numeric
    df['date_ordinal'] = df['date'].map(lambda x: x.toordinal())

    X = df[['date_ordinal']]
    y = df['temperature']

    # Train model
    model = LinearRegression()
    model.fit(X, y)

    # Future dates (next 30 days)
    last_date = df['date'].max()
    future_dates = [last_date + pd.Timedelta(days=i) for i in range(1, 31)]

    future_ordinal = np.array([d.toordinal() for d in future_dates]).reshape(-1, 1)

    predictions = model.predict(future_ordinal)

    # Plot
    plt.figure(figsize=(12,6))
    plt.plot(df['date'], df['temperature'], label="Actual")
    plt.plot(future_dates, predictions, label="Forecast", color='red')

    plt.legend()
    plt.title("Temperature Forecast (Next 30 Days)")

    plt.savefig("outputs/graphs/forecast.png")
    plt.close()

    print("✅ Forecast generated!")