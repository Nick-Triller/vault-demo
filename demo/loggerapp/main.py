import psycopg2
import configparser
from datetime import datetime
import time
import string
import random
import os
import logging

log = logging.getLogger(__name__)
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

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def main():
  while True:
    config = read_conf()
    username = config[config_section]["username"]
    password = config[config_section]["password"]
    host = config[config_section]["host"]
    with connect(host, username, password) as conn:
      with conn.cursor() as cur:
        data = randomString()
        cur.execute("INSERT INTO record (content) VALUES (%s)", (data,))
        conn.commit()
        log.debug("Saved record in DB, data:" + data)
    time.sleep(5)

if __name__ == "__main__":
  logging.basicConfig(level=logging.DEBUG)
  main()
