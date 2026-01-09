import psycopg2
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from psycopg2.extras import RealDictCursor
import redis

REDIS_HOST = os.getenv("REDIS_HOST", "cache")
redis_client = redis.Redis(host=REDIS_HOST, port=6379, db=0, decode_responses=True)

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
def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "db"),
        port=5432,
        user=os.getenv("POSTGRES_USER", "user_ynov"),
        password=os.getenv("POSTGRES_PASSWORD"),
        database=os.getenv("POSTGRES_DB", "mydb")
    )


@app.get("/")
async def get_students():
    try:
        views = redis_client.incr("views", 1)
    except:
        views = 0
    
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT nom, promo FROM students;")
        row = cur.fetchall()
        cur.close()
        conn.close()
        for r in row:
            r["views"] = views
        return row
    except Exception as e:
        return {"error": str(e)}