FROM python:3.8.7-alpine3.12
WORKDIR /app
COPY ./requirements.txt .
COPY ./application /app
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip3 install -r requirements.txt
CMD ["python", "manage.py", "runserver"]
