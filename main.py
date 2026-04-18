from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.analysis import analyze_trends
from src.anomaly import detect_anomalies
from src.visualization import plot_data
from src.forecast import forecast_temperature

def main():
    df = load_data("data/raw/climate_data.csv")
    df = preprocess_data(df)
    
    analyze_trends(df)
    df = detect_anomalies(df)

    plot_data(df)
    forecast_temperature(df)

if __name__ == "__main__":
    main()