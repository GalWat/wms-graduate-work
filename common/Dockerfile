# syntax=docker/dockerfile:1
FROM python:3.11-alpine

WORKDIR /common
COPY . ./

RUN apk add curl &&\
    pip install -r requirements.txt &&\
    curl -fsSL -o /usr/local/bin/dbmate \
    https://github.com/amacneil/dbmate/releases/latest/download/dbmate-linux-amd64 &&\
    chmod +x /usr/local/bin/dbmate

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--app-dir", "app"]