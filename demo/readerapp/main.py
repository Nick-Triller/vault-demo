import psycopg2
from psycopg2.extras import RealDictCursor
import configparser
import logging
import os
import json
import datetime
from flask import Flask, escape, request

log = logging.getLogger(__name__)
app = Flask(__name__)
config_section = "database"

def read_conf():
  config = configparser.ConfigParser()
  config.read("./creds/creds.txt")
  if config_section not in config:
      config[config_section] = {}
  config[config_section]["host"] = os.environ.get("DB_HOST") or "postgres"
  return config

def connect(host, username, password):
  conn_str = f"dbname='postgres' user='{username}' host='{host}' password='{password}'"
  conn = psycopg2.connect(conn_str)
  return conn

@app.route('/')
def hello():
  config = read_conf()
  username = config[config_section]["username"]
  password = config[config_section]["password"]
  host = config[config_section]["host"]
  with connect(host, username, password) as conn:
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
      cur.execute("SELECT * FROM record ORDER BY created_on DESC LIMIT 100")
      result = cur.fetchall()
      return "<pre>" + json.dumps(result, sort_keys=True, indent=2, default=default) + "</pre>"

def default(o):
  if isinstance(o, (datetime.date, datetime.datetime)):
    return o.isoformat()

if __name__ == '__main__':
  logging.basicConfig(level=logging.DEBUG)
  app.run(host='0.0.0.0', port=8000)
