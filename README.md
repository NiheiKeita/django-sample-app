# DjangoサンプルAPIアプリケーション

このリポジトリは、Django REST Framework・PostgreSQL・Docker・GitHub Actionsを使ったAPI開発のサンプルです。
新人エンジニアでも同じ環境を再現できるよう、セットアップ手順や技術解説をまとめています。

## 技術スタック
- Python 3.11
- Django 5
- Django REST Framework
- PostgreSQL
- Docker / docker-compose
- GitHub Actions（CI/CD）
- Black, Flake8, isort, mypy（静的解析・型チェック）
- pytest, pytest-django（テスト）

## セットアップ手順

### 1. 必要なツールのインストール
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) をインストールしてください。
- Gitが必要です。

### 2. リポジトリのクローン
```sh
git clone <このリポジトリのURL>
cd <リポジトリ名>
```

### 3. 環境構築（初回のみ）
#### Dockerイメージのビルド
```sh
docker compose build
```

#### データベースのマイグレーション
```sh
docker compose run --rm web python manage.py makemigrations

docker compose run --rm web python manage.py migrate
```

#### 管理ユーザー作成（必要に応じて）
```sh
docker compose run --rm web python manage.py createsuperuser
```

### 4. 開発サーバーの起動
```sh
docker compose up
```
- http://localhost:8000/ でDjangoアプリが起動します。
- http://localhost:8000/admin/ で管理画面にアクセスできます。
- http://localhost:8000/api/ でAPIエンドポイントにアクセスできます。
- http://localhost:8000/docs/ でAPIドキュメントが見られます。

### 5. テストの実行
```sh
docker compose run --rm web pytest
```

### 6. 静的解析・型チェック
```sh
docker compose run --rm web black . --check

docker compose run --rm web flake8 .

docker compose run --rm web isort . --check-only

docker compose run --rm web mypy .
```

## ディレクトリ構成
```
├── api/                # アプリ本体（モデル・シリアライザ・ビュー・テスト）
├── config/             # プロジェクト設定
├── Dockerfile          # Dockerイメージ定義
├── docker-compose.yml  # サービス定義
├── requirements.txt    # Python依存パッケージ
├── .github/workflows/  # GitHub Actionsワークフロー
└── ...
```

## 主なAPIエンドポイント
- タスク一覧取得: `GET /api/tasks/`
- タスク作成: `POST /api/tasks/`
- タスク詳細: `GET /api/tasks/{id}/`
- タスク更新: `PATCH /api/tasks/{id}/`
- タスク削除: `DELETE /api/tasks/{id}/`
- ステータス変更: `POST /api/tasks/{id}/change_status/`

## CI/CDについて
- プッシュやプルリクエスト時にGitHub Actionsで自動的にテスト・静的解析が走ります。
- `.github/workflows/ci.yml` を参照してください。

## よくあるトラブル
- **依存パッケージを追加したら** `docker compose build` を再実行してください。
- **DBの接続エラー** → `docker compose up` でDBサービスが起動しているか確認。
- **マイグレーション忘れ** → `docker compose run --rm web python manage.py migrate` を実行。

## 参考
- [Django公式ドキュメント](https://docs.djangoproject.com/ja/5.0/)
- [Django REST Framework公式](https://www.django-rest-framework.org/)
- [Docker公式](https://docs.docker.com/)

---
何か不明点があれば、先輩やリーダーに気軽に質問してください！

