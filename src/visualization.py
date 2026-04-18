import os
import matplotlib.pyplot as plt

def plot_data(df):
    os.makedirs("outputs/graphs", exist_ok=True)

    # 1️⃣ Temperature Trend
    plt.figure(figsize=(12,6))
    plt.plot(df['date'], df['temperature'], alpha=0.5)
    plt.plot(df['date'], df['temp_ma'], color='red')
    plt.title("Temperature Trend")
    plt.savefig("outputs/graphs/temp_trend.png")
    plt.close()

    # 2️⃣ Rainfall Trend
    plt.figure(figsize=(12,6))
    plt.plot(df['date'], df['rainfall'], color='blue')
    plt.title("Rainfall Trend")
    plt.savefig("outputs/graphs/rainfall_trend.png")
    plt.close()

    # 3️⃣ Humidity Trend
    plt.figure(figsize=(12,6))
    plt.plot(df['date'], df['humidity'], color='green')
    plt.title("Humidity Trend")
    plt.savefig("outputs/graphs/humidity_trend.png")
    plt.close()

    # 4️⃣ Seasonal Analysis
    df.groupby('season')['temperature'].mean().plot(kind='bar')
    plt.title("Avg Temperature by Season")
    plt.savefig("outputs/graphs/season_temp.png")
    plt.close()

    print("✅ All graphs generated!")