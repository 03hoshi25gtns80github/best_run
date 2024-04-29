FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /src

WORKDIR /src

COPY requirements.txt /src/

RUN pip install --upgrade pip\
    && pip install --upgrade setuptools\
    && pip install -r requirements.txt

RUN mkdir -p /var/run/gunicorn

CMD ["gunicorn", "config.wsgi", "--bind=unix:/var/run/gunicorn/gunicorn.sock"]