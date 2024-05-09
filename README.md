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
Bootstrap
js
Docker
Git
GitHub
PostgreSQL
Azure
AWS
Nginx/Gunicorn
Let’s Encrypt

### Docker コマンド：

docker-compose up
コンテナを実行
docker-compose down
コンテナの停止
docker-compose exec gunicorn python manage.py collectstatic  
静的ファイルの移動

http://localhost:8000/

### テストユーザー

id：test1,test2,...,
pass：T11111111  
  
### DBコマンド  
docker-compose exec db psql -U ${DB_USER} ${DB_NAME}  
\dt
SELECT * FROM "テーブル名";  

### Branch  
main:デプロイできる状態  
dev:開発用
その他：機能ごと、更新事にmainとdevにマージ  

### EC2



