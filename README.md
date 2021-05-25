## Chatbot powered by Flask-SocketIO

### Installation
```bash
clone this project

python3 -m venv venv

source venv/bin/activate

pip3 install --upgrade pip
pip3 install -r requirements.txt
```

### Run 
```bash
./gunicorn-run.sh
```
or manually
```bash
source venv/bin/activate
gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 10 app:app --bind 0.0.0.0:8000
```

### Configuration for Nginx
Listening 8000 port. Local 8002
```nginx
server {
    listen 8000;
    server_name localhost;

    location / {
        include proxy_params;
        proxy_pass http://0.0.0.0:8002;
    }
}
```

