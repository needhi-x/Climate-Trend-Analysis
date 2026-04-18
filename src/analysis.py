def analyze_trends(df):
    df['temp_ma'] = df['temperature'].rolling(window=30).mean()
    print("Trend analysis done")