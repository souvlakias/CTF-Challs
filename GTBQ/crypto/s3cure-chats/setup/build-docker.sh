#!/bin/bash
docker rm -f safe-chats
docker build -t safe-chats .
docker run --name=safe-chats --rm -p5000:5000 -it safe-chats