## パッケージのインストール
```shell script
pip install -r requirements.txt
```

## 環境設定

```shell script
export CREDENTIAL_FILE=${サービスアカウントファイル:./xxxx.json} 
export STORAGE_BUCKET=${バケット名:xxxx.appspot.com}
```

## 実行
### ファイル一覧取得

```shell script
python3 main.py list2file ${output_local_path}
```

### ファイルコピー

```shell script
python3 main.py copy ${src_path} ${dest_path}
```

### ファイル削除

```shell script
python3 main.py copy ${target_path}
```

## API reference

* Python Client for Google Cloud Storage
    * https://googleapis.dev/python/storage/latest/index.html