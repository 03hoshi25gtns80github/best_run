### 開発概要：
Webアプリケーション
毎日のベスランとコメントをカレンダーに記録する

### 使用技術：
Django
Python
HTML
CSS
js
Docker
Git
GitHub

### Dockerコマンド：
   docker-compose up -d
コンテナをバックグラウンドで実行
   docker-compose exec django bash
コンテナ内のbashシェルにアクセス
   docker-compose down
コンテナの停止
   python manage.py runserver 0.0.0.0:8000
http://localhost:8000/
コンテナ内でrunserverするとこのページがフロントになる
