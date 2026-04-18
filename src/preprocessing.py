import pandas as pd

def preprocess_data(df):
    df['date'] = pd.to_datetime(df['date'])
    df = df.dropna()
    
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month

    # Add seasons
    def get_season(month):
        if month in [12, 1, 2]:
            return "Winter"
        elif month in [3, 4, 5]:
            return "Summer"
        elif month in [6, 7, 8]:
            return "Monsoon"
        else:
            return "Post-Monsoon"

    df['season'] = df['month'].apply(get_season)

    return df