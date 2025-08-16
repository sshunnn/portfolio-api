# my-fastapi-backend

FastAPI + SQLAlchemy によるシンプルなバックエンドAPIのサンプルです。

## セットアップ

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 起動方法

```bash
uvicorn app.main:app --reload
```

## ディレクトリ構成

```
app/
  main.py
  db.py
  models.py
  schemas.py
  routers/
    items.py
  settings.py
.env
requirements.txt
README.md
```
