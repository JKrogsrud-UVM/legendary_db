FROM python:3.8

LABEL org.opencontainers.image.source=https://github.com/jkrogsrud/legendary_db

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY db/main.py ./
COPY db/parse.py ./
COPY db/data.py ./
COPY data/characters.csv ./

CMD [ "python", "./main.py" ]