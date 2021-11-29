#!/bin/bash
cd /var/www/AulaTaller
# source venv/bin/activate
gunicorn aulaTaller.wsgi -t 600 -b 127.0.0.1:8001 -w 6 --user=root --log-file=/var/www/AulaTaller/gunicorn.log 2>>/var/www/AulaTaller/gunicorn.log
