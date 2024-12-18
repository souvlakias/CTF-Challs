#!/bin/sh

# Generate global variables
export APP_SECRET_KEY=$(python3 -c 'import secrets;print(secrets.token_hex(32))' 2>&1)

# Serve application
mitmdump -q --listen-host 127.0.0.1 --listen-port 8080 -s proxy.py &
python3 -m gunicorn --bind 0.0.0.0:$APP_PORT app:app --workers 4
