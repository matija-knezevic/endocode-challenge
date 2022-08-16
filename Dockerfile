# syntax=docker/dockerfile:1

FROM python:3.8

ENV FLASK_APP=endo-app.py

WORKDIR /endo-app-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080"]