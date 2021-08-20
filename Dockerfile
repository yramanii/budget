FROM python:3.8-slim-buster

WORKDIR /app

ENV PYTHONUNBUFFERED=1

ADD . /app/

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]