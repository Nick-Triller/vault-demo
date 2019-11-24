CREATE TABLE record(
   id serial PRIMARY KEY,
   content TEXT NOT NULL,
   created_on TIMESTAMP NOT NULL DEFAULT NOW()
)
