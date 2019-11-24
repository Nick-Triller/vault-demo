FROM python:3.6.9-alpine

WORKDIR /app

# Dependencies for psycopg2 compilation
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .
CMD [ "python", "./main.py" ]
