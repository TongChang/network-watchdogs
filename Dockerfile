# 基本イメージとしてPythonの公式イメージを使用
FROM python:3.8-slim

# タイムゾーンの設定
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 必要なパッケージのインストール
RUN apt-get update && \
    apt-get install -y iputils-ping && \
    rm -rf /var/lib/apt/lists/*

# 作業ディレクトリの設定
WORKDIR /app

# 必要なファイルをコンテナ内にコピー
COPY app/ .

# スクリプトの実行
CMD ["python", "./main.py"]