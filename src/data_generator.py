import pandas as pd
import numpy as np

def generate_climate_data():
    dates = pd.date_range(start="2010-01-01", periods=3650)
    time = np.arange(len(dates))

    # Temperature
    trend = 0.02 * time
    season = 5 * np.sin(2 * np.pi * time / 365)
    noise = np.random.normal(0, 1, len(time))
    temperature = 25 + trend + season + noise

    # Rainfall (seasonal pattern)
    rainfall = 50 + 20 * np.sin(2 * np.pi * time / 365 + 1) + np.random.normal(0, 5, len(time))

    # Humidity (inverse of temperature slightly)
    humidity = 70 - 0.1 * temperature + np.random.normal(0, 2, len(time))

    df = pd.DataFrame({
        "date": dates,
        "temperature": temperature,
        "rainfall": rainfall,
        "humidity": humidity
    })

    df.to_csv("data/raw/climate_data.csv", index=False)

    print("✅ Advanced climate dataset generated!")
    

if __name__ == "__main__":
    generate_climate_data()