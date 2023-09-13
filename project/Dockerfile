FROM python:3

WORKDIR /usr/src/app

USER root

COPY . .

RUN python -m pip install -U pip && pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

USER 1001

CMD ["python", "./app.py"]