import matplotlib.pyplot as plt
import pandas as pd

def plot_data(df_input):
    df = df_input.copy()

    fig, axes = plt.subplots(2, 2, figsize=(16, 10))
    plt.subplots_adjust(hspace=0.4)

    # 1. Biểu đồ Histogram: Phân phối giá cước (Fare Amount)
    axes[0, 0].hist(df["fare_amount"], bins=30, color='skyblue', edgecolor='black')
    axes[0, 0].set_title("1. Phân phối giá cước (Histogram)")
    axes[0, 0].set_xlabel("Giá tiền")
    axes[0, 0].set_ylabel("Số lượng chuyến")

    # 2. Biểu đồ Scatter: Mối quan hệ giữa Quãng đường và Giá tiền
    axes[0, 1].scatter(df["trip_distance"], df["fare_amount"], alpha=0.5, color='orange')
    axes[0, 1].set_title("2. Quãng đường vs Giá cước (Scatter Plot)")
    axes[0, 1].set_xlabel("Quãng đường (miles)")
    axes[0, 1].set_ylabel("Giá tiền")

    # 3. Biểu đồ Bar: Số lượng chuyến đi theo Thứ trong tuần
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    trips_per_day = df['day_of_week'].value_counts().reindex(day_order)
    
    axes[1, 0].bar(trips_per_day.index, trips_per_day.values, color='green')
    axes[1, 0].set_title("3. Số chuyến theo ngày trong tuần (Bar Chart)")
    axes[1, 0].set_ylabel("Số lượng chuyến")
    axes[1, 0].tick_params(axis='x', rotation=45)

    # 4. Biểu đồ Line: Xu hướng chuyến đi theo Giờ trong ngày
    trips_per_hour = df.groupby('hour').size()
    
    axes[1, 1].plot(trips_per_hour.index, trips_per_hour.values, marker='o', color='red', linestyle='-')
    axes[1, 1].set_title("4. Xu hướng chuyến đi theo giờ (Line Chart)")
    axes[1, 1].set_xlabel("Giờ trong ngày (0-23h)")
    axes[1, 1].set_ylabel("Số lượng chuyến")
    axes[1, 1].grid(True, linestyle='--', alpha=0.6)
    
    plt.show()