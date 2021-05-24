## Chatbot powered by Flask-SocketIO

### Installation
    clone this project

    python3 -m venv venv

    source venv/bin/activate

    pip3 install --upgrade pip
    pip3 install -r requirements.txt


### Run 
    ./gunicorn-run.sh


### Configuration for Nginx
Listening 8000 port.
```nginx
server {
    listen 8000;
    server_name localhost;

    location / {
        include proxy_params;
        proxy_pass http://0.0.0.0:8000;
    }

    location /static {
        alias <path-to-your-application>/static;
        expires 30d;
    }

    location /socket.io/ws {
        proxy_redirect off;

    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_read_timeout 600;
    proxy_pass http://0.0.0.0:8000/socket.io/;
    }
}
```

