#!/bin/bash
gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 10 app:app --bind 0.0.0.0:8000