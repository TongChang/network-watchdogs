# network watchdogs

家のネットワークが定期的に切れるので、ログを取りたかった。
セットアップが簡単で、後々Raspberry Piで動かせるようにしたかったので、小さいパッケージ+Dockerという構成にしました。

## コンテナのビルド手順

Dockerのビルドコマンドでビルドします。

```{zsh}
# ビルド
$ docker build -t network-watchdogs .
```

## コンテナの実行手順

ホストのディレクトリにログを吐く場合はマウントします

```{zsh}
# 実行
$ docker run -v "$(PWD)/logs:/app/logs" network-watchdogs
```

## フォルダ構成

```{plain text}
network-watchdogs/
│
├── Dockerfile
├── app/               # アプリケーション本体
│   ├── logger/        # 監視状況のロギングモジュール
│   ├── models/        # データ構造
│   └── network/       # ネットワーク操作モジュール
└── main.py            # 実行スクリプト
```

## やりたいこと

- 外部のデータストアにデータを保管して、いつでも状態が見れるようにしたい
- 待機時間を実行時に設定したい
