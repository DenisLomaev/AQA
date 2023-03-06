FROM python:3.9-alpine
WORKDIR /tests_project/
COPY requirements.txt .
RUN apk add chromium-chromedriver
RUN pip install -r requirements.txt
RUN apk add chromium

