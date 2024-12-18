FROM ubuntu:22.04

RUN apt-get update && apt-get install -y socat python3

WORKDIR /app
COPY . .

EXPOSE 1337
CMD ["socat", "-v","TCP-LISTEN:1337,reuseaddr,fork", "EXEC:'python3 /app/server.py'"]