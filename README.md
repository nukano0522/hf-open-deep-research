# リサーチ API

このプロジェクトは、smolagentsを使用したリサーチ機能をAPI化したものです。

## セットアップ

### 必要な依存関係

以下のパッケージをインストールする必要があります：

```bash
pip install -r requirements.txt
pip install 'smolagents[litellm]'
pip install fastapi uvicorn pydantic
```

また、smolagentsプロジェクトの依存関係も必要です。

### 環境変数

`.env`ファイルを作成し、必要な環境変数を設定してください：

```
HF_TOKEN=your_huggingface_token
SERPAPI_API_KEY=your_serpapi_key
```

## 使い方

### APIサーバーの起動

```bash
python api.py
```

サーバーは`http://localhost:8000`で起動します。

### APIエンドポイント

- `GET /`: ウェルカムメッセージを表示
- `POST /research`: リサーチAPIエンドポイント

### リクエスト例

```json
{
  "topic": "2023年の世界的な気候変動による影響",
  "model_id": "o1"
}
```

### クライアントの使用方法

付属のクライアントスクリプトを使用してAPIをテストできます：

```bash
python client.py "2023年の世界的な気候変動による影響" --model-id "o1"
```

### Swagger UI

APIサーバー起動後、ブラウザで`http://localhost:8000/docs`にアクセスすると、Swagger UIからAPIをテストできます。

## 注意事項

- リサーチには時間がかかる場合があります。タイムアウト設定を適切に調整してください。
- 複雑なリサーチトピックの場合、より長い処理時間が必要になります。