FROM python:3.6.9-alpine

WORKDIR /app

COPY requirements.txt .
# Dependencies for psycopg2 compilation
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt

COPY main.py .

CMD [ "python", "./main.py" ]
