### 開発概要：

Web アプリケーション
毎日のベスランとコメントをカレンダーに記録する  
フレンド機能  
コメント機能  
送信側、受信側がどちらも匿名か非匿名のコメントを選択可能

### 使用技術：

Django
Python
HTML
CSS
js
Docker
Git
GitHub  
Azure

### Docker コマンド：

docker-compose up -d
コンテナをバックグラウンドで実行
docker-compose exec django bash
コンテナ内の bash シェルにアクセス
docker-compose down
コンテナの停止
python manage.py runserver 0.0.0.0:8000
http://localhost:8000/
コンテナ内で runserver するとこのページがフロントになる

### テストユーザー

id：test1,test2,...,
pass：T11111111  
  
### DBコマンド  
docker-compose exec db psql -U ${DB_USER} ${DB_NAME}  
\dt
SELECT * FROM "テーブル名";

