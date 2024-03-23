import csv
import datetime

def initialize_csv(file_path):
    start_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file_prefix = f"network_log_"
    log_file_path = f"{file_path}/{log_file_prefix}{start_time}.csv"

    # ヘッダー行の書き込み
    with open(log_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["タイムスタンプ", "アドレス", "ステータス", "時間(ms)", "備考"])

    return log_file_path

def log(file_path, ping_result):
    """
    PingResultのインスタンスを受け取り、CSVファイルに書き込む

    :param file_path: CSVファイルのパス
    :param ping_result: PingResultのインスタンス
    """
    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            [
                ping_result.timestamp,
                ping_result.address,
                "OK" if ping_result.success else "NG",
                ping_result.response_time,
                ping_result.note
            ]
        )
