import pandas as pd

def clean_data(df_input):
    # 1. Xử lý thiếu: Xóa dòng thiếu thời gian, điền median cho số
    df = df_input.copy()
    df = df.dropna(subset=["pickup_datetime", "dropoff_datetime"])
    if "trip_distance" in df.columns:
        df["trip_distance"] = df["trip_distance"].fillna(df["trip_distance"].median())
    if "fare_amount" in df.columns:
        df["fare_amount"] = df["fare_amount"].fillna(df["fare_amount"].median())

    # 2. Xóa trùng lặp
    df = df.drop_duplicates()

    # 3. Loại bỏ giá trị không hợp lệ (<= 0)
    df = df[(df["trip_distance"] > 0) & (df["fare_amount"] > 0)]

    # 4. Xử lý ngoại lệ (Outliers) bằng IQR
    for col in ["trip_distance", "fare_amount"]:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        df = df[(df[col] >= (Q1 - 1.5 * IQR)) & (df[col] <= (Q3 + 1.5 * IQR))]
    
    return df