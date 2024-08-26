FROM python:3.8

WORKDIR /app

COPY . .

RUN apt update && \
    apt install -y vim libmagic1 gettext && \
    apt-get install -y python3-dev && \
    pip install --upgrade pip && \
    pip install -r ./requirements.txt

CMD ["python", "main.py"]
