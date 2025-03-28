import requests
import argparse
import json


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("topic", type=str, help="リサーチしたいトピック")
    parser.add_argument("--model-id", type=str, default="o1")
    parser.add_argument("--api-url", type=str, default="http://localhost:8000/research")
    return parser.parse_args()


def main():
    args = parse_args()

    # リクエストの準備
    payload = {"topic": args.topic, "model_id": args.model_id}

    # APIへリクエスト
    print(f"リクエスト送信中: {args.topic}")
    try:
        response = requests.post(args.api_url, json=payload)
        response.raise_for_status()  # エラーがあれば例外を発生

        # レスポンスの処理
        result = response.json()
        print("\n=== リサーチ結果 ===\n")
        print(result["result"])

    except requests.exceptions.RequestException as e:
        print(f"エラーが発生しました: {e}")
        if hasattr(e, "response") and e.response:
            try:
                error_detail = e.response.json()
                print(f"エラー詳細: {error_detail}")
            except:
                print(f"レスポンス: {e.response.text}")


if __name__ == "__main__":
    main()
