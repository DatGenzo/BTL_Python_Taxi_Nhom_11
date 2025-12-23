import pandas as pd
from modules.cleaning import clean_data
from modules.preprocessing import preprocess_data
from modules.visualization import plot_data

def main():
    # 1. Đọc dữ liệu
    path = "data/taxi_data.csv" # Thay bằng file của bạn
    try:
        df = pd.read_csv(path)
        print("Đã tải dữ liệu thành công!")
    except Exception as e:
        print(f"Lỗi đọc file: {e}")
        return

    # 2. Làm sạch (SV3)
    df_cleaned = clean_data(df)

    # 3. Tiền xử lý (SV4)
    df_preprocessed = preprocess_data(df_cleaned)

    # 4. Trực quan hóa (SV5)
    plot_data(df_preprocessed)

    # 5. Lưu kết quả cuối cùng
    df_preprocessed.to_csv("data/final_processed_data.csv", index=False)
    print("Hoàn thành! Dữ liệu sạch đã được lưu.")

if __name__ == "__main__":
    main()