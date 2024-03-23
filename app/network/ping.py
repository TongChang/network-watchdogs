from models.ping_result import PingResult
import subprocess
import re

def ping_test(timestamp, address, timeout=2):
    """
    指定されたアドレスに対してPingテストを実行し、結果を返す。
    成功時は応答時間を、失敗時は失敗の理由を含む辞書を返す。

    :param address: Pingテストを行うアドレス
    :return: 結果を含む辞書。キーには'success', 'response_time', 'remark'が含まれる。
    """
    try:
        output = subprocess.check_output(["ping", "-c", "1", "-W", str(timeout), address], stderr=subprocess.STDOUT, universal_newlines=True)

        # 応答時間を抽出する
        response_time_match = re.search(r"time=(\d+\.?\d*) ms", output)
        if response_time_match:
            response_time = response_time_match.group(1)
            return PingResult(timestamp, address, True, response_time, "")

    except subprocess.CalledProcessError as e:
        # 失敗理由（エラーメッセージ）を抽出
        error_message = str(e)
        return PingResult(timestamp, address, False, None, error_message)

    except subprocess.TimeoutExpired:
        # タイムアウト
        return PingResult(timestamp, address, False, None, "タイムアウトしました")

    # その他の理由でのエラー
    return PingResult(timestamp, address, False, None, "処理が失敗しました")
