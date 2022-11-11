# syntax=docker/dockerfile:1
FROM python:3.9-alpine

WORKDIR /compose
COPY . ./

RUN apk add curl &&\
    pip install -r requirements.txt &&\
    curl -fsSL -o /usr/local/bin/dbmate \
    https://github.com/amacneil/dbmate/releases/latest/download/dbmate-linux-amd64 &&\
    chmod +x /usr/local/bin/dbmate

CMD ["python", "app/main.py"]