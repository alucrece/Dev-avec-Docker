import mysql.connector
import os
import psycopg2
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

#create a connection to the database
conn = psycopg2.connect(
    host="localhost",
    port=3306,
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)

@app.get("/users")
async def get_users():
    cursor = conn.cursor()
    sql_select_Query = "SELECT * from users;"
    cursor.execute(sql_select_Query)
    #get all records
    records = cursor.fetchall()
    print("Total number of rows in users is: ", cursor.rowcount)
    #renvoyer les résultats
    return {"users": records}

@app.get("/")
async def get_version():
    cur = conn.cursor()
    cur.execute("SELECT VERSION();")
    row = cur.fetchone()
    print(row[0])
    return {"version": row[0]}