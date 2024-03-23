from models.ping_result import PingResult
import datetime
import time
from network import ping
from network import dns
from logger import csv
import logging

def network_check():
    """
    ネットワークチェックのFacade関数
    """
    try:
        init_logging()

        logging.info("ネットワークチェックを開始します...")
        log_file = csv.initialize_csv("./logs")
        logging.info(f"ログファイルを作成しました: {log_file}")

        # DNSチェック用
        last_dns_server = ""
        while True:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            logging.info("--------------------------------------------------")
            logging.info("pingテストします")

            current_dns_server = dns.get_dns_server(force_google=True)
            if current_dns_server != last_dns_server:
                logging.info("DNSサーバーが変更されました。ターゲットを更新しています...")
                last_dns_server = current_dns_server

            if not current_dns_server:
                result = PingResult(timestamp, current_dns_server, False, None, "DNSサーバーが見つかりません")
                logging.info("DNSサーバーが見つかりません。60秒後に再試行します...")
            else:
                result = ping.ping_test(timestamp, current_dns_server)

            csv.log(log_file, result)
            logging.info("pingテスト完了")
            time.sleep(60)

    except KeyboardInterrupt:
        logging.info("ネットワークチェックを終了します")

def init_logging():
    """
    ロギングの初期化
    """
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    network_check()
