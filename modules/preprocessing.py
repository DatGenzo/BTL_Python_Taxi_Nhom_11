import pandas as pd

def preprocess_data(df):
    # 1. Chuyển đổi kiểu dữ liệu thời gian
    df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])
    df["dropoff_datetime"] = pd.to_datetime(df["dropoff_datetime"])

    # 2. Trích xuất đặc trưng (Feature Engineering)
    df["hour"] = df["pickup_datetime"].dt.hour
    df["day_of_week"] = df["pickup_datetime"].dt.day_name()
    df["duration_min"] = (df["dropoff_datetime"] - df["pickup_datetime"]).dt.total_seconds() / 60

    # 3. Chuẩn hóa Min-Max cho trip_distance và fare_amount
    for col in ["trip_distance", "fare_amount"]:
        min_val = df[col].min()
        max_val = df[col].max()
        if max_val != min_val:
            df[f"{col}_normalized"] = (df[col] - min_val) / (max_val - min_val)
    
    return df