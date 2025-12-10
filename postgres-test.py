import psycopg2
import os
import mysql.connector
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#connexion
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user=os.getenv("POSTGRES_USER", "user_ynov"),
    password=os.getenv("POSTGRES_PASSWORD"),
    database=os.getenv("POSTGRES_DB", "mydb")
)


@app.get("/")
async def get_version():
    cur = conn.cursor()
    cur.execute("SELECT VERSION();")
    row = cur.fetchone()
    print(row[0])
    return {"version": row[0]}

# Test
cur = conn.cursor()
cur.execute("SELECT * from users;")
print(cur.fetchall())

conn.close()