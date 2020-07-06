FROM python:3.4-alpine
RUN apk update
RUN apk add bash
RUN pip install selenium pytest pytest-html
