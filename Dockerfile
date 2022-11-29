FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py ./
COPY parse.py ./
COPY data.py ./
COPY characters.csv ./

CMD [ "python", "./main.py" ]