
# portfolio-api

FastAPI + SQLAlchemy + PostgreSQL によるシンプルなAPIサーバーです。

## 主な機能

- `/` : サーバーの動作確認（Hello, FastAPI!）
- `/health` : ヘルスチェック
- `/items` : アイテムのCRUD（作成・取得・更新・削除）

## ディレクトリ構成

```
app/
  main.py         # FastAPIエントリポイント
  models.py       # SQLAlchemyモデル定義
  schemas.py      # Pydanticスキーマ定義
  db.py           # DB接続・初期化
  settings.py     # 環境変数・設定
  routers/
    items.py      # /items ルーター
```

## 環境変数

`.env` ファイルに下記を記載してください。

```
DATABASE_URL=postgresql+psycopg://postgres:パスワード@ホスト:5432/postgres?sslmode=require
```

## セットアップ

1. 仮想環境の作成・有効化
   ```zsh
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. 依存パッケージのインストール
   ```zsh
   pip install -r requirements.txt
   ```

3. DB初期化
   ```zsh
   python -c "from app.db import init_db; init_db()"
   ```

4. サーバー起動
   ```zsh
   uvicorn app.main:app --reload
   ```

## API例

- **GET /items**  
  アイテム一覧取得

- **POST /items**  
  アイテム新規作成  
  ```json
  {
    "name": "サンプル",
    "description": "説明"
  }
  ```

- **GET /items/{item_id}**  
  アイテム詳細取得

- **PUT /items/{item_id}**  
  アイテム更新

- **DELETE /items/{item_id}**  
  アイテム削除
